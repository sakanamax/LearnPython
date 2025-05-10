import requests
import csv
import json  # 導入json模組來讀取配置文件

# 從配置文件中讀取配置參數
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

tenant_id = config['tenant_id']
client_id = config['client_id']
client_secret = config['client_secret']

# 獲取訪問令牌的函數
def get_access_token(tenant_id, client_id, client_secret):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"  # 令牌請求的URL
    data = {
        'grant_type': 'client_credentials',  # 授權類型為客戶端憑證
        'client_id': client_id,              # 客戶端ID
        'client_secret': client_secret,      # 客戶端秘鑰
        'scope': 'https://graph.microsoft.com/.default'  # 訪問範圍
    }
    response = requests.post(url, data=data)  # 發送POST請求以獲取訪問令牌
    response.raise_for_status()  # 如果請求失敗，拋出異常
    return response.json().get('access_token')  # 返回解析得到的訪問令牌

# 邀請單個用戶的函數
def invite_user(access_token, email, display_name, redirect_url):
    url = "https://graph.microsoft.com/v1.0/invitations"  # 邀請API的URL
    headers = {
        'Authorization': f'Bearer {access_token}',  # 使用訪問令牌進行授權
        'Content-Type': 'application/json'  # 請求內容類型為JSON
    }
    payload = {
        'invitedUserEmailAddress': email,           # 被邀請者郵箱地址
        'inviteRedirectUrl': redirect_url,          # 邀請接受後的重定向URL
        'invitedUserDisplayName': display_name,     # 被邀請者顯示名稱
        'sendInvitationMessage': True               # 發送邀請郵件
    }
    try:
        response = requests.post(url, headers=headers, json=payload)  # 發送POST請求以邀請用戶
        print(f"Status Code: {response.status_code}")
        if response.status_code != 200 and response.status_code != 201:
            print(f"Error details: {response.text}")
        response.raise_for_status()  # 如果請求失敗，拋出異常
        return response.json()  # 返回邀請操作的結果
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Response details: {e.response.text}")
        raise

# 從文件批量邀請用戶的函數
def invite_users_from_file(tenant_id, client_id, client_secret, filename, redirect_url):
    access_token = get_access_token(tenant_id, client_id, client_secret)  # 獲取訪問令牌
    results = []  # 用於存儲所有邀請結果的列表
    with open(filename, mode='r', encoding='utf-8') as file:  # 打開CSV文件
        reader = csv.DictReader(file)  # 創建一個字典格式的CSV讀取器
        for row in reader:  # 遍歷文件中的每一行
            email = row['email']  # 獲取郵箱地址
            display_name = row['display_name']  # 獲取顯示名稱
            try:
                result = invite_user(access_token, email, display_name, redirect_url)  # 邀請用戶
                results.append(result)  # 將結果添加到列表中
                status = result.get('status', 'No status in response')  # 獲取邀請狀態
                if 'error' in result:  # 如果有錯誤
                    error_message = result['error'].get('message', 'No error message')  # 獲取錯誤信息
                    print(f"Failed to invite {email} ({display_name}): {error_message}")  # 打印錯誤信息
                else:
                    print(f"Invited {email} ({display_name}): {status}")  # 打印成功信息
            except requests.exceptions.RequestException as e:  # 捕捉請求異常
                print(f"Failed to invite {email} ({display_name}): {e}")  # 打印異常信息
    return results  # 返回所有邀請結果

# 配置參數
filename = 'users.csv'  # CSV文件路徑
redirect_url = 'https://portal.azure.com/'  # 重定向URL - 使用Azure入口網站作為重定向

# 定義獲取用戶ID的函數
def get_user_id(access_token, email):
    url = f"https://graph.microsoft.com/v1.0/users?$filter=mail eq '{email}' or userPrincipalName eq '{email}'"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        users = response.json().get('value', [])
        if users:
            return users[0].get('id')
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error getting user ID for {email}: {e}")
        return None

# 定義將用戶ID寫入CSV的函數
def save_user_ids_to_csv(results, output_filename='invited_users_with_ids.csv'):
    # 獲取新的訪問令牌
    access_token = get_access_token(tenant_id, client_id, client_secret)
    
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['user_id', 'display_name'])  # 寫入標題行
        
        for result in results:
            if 'invitedUser' in result:
                invited_user = result['invitedUser']
                email = result.get('invitedUserEmailAddress', '')
                display_name = invited_user.get('displayName', '')
                
                print(f"Getting ID for {email}...")
                
                # 嘗試獲取用戶ID
                user_id = None
                if 'id' in invited_user:
                    user_id = invited_user['id']
                else:
                    # 如果邀請響應中沒有ID，嘗試使用Graph API獲取
                    import time
                    time.sleep(2)  # 等待2秒，讓系統有時間處理邀請
                    user_id = get_user_id(access_token, email)
                
                # 使用CSV中的display_name而不是API回傳的
                original_display_name = ''
                with open(filename, mode='r', encoding='utf-8') as infile:
                    reader = csv.DictReader(infile)
                    for row in reader:
                        if row['email'] == email:
                            original_display_name = row['display_name']
                            break
                
                if user_id:
                    writer.writerow([user_id, original_display_name])
                    print(f"Successfully saved ID for {email}: {user_id}")
                else:
                    print(f"Could not get ID for {email}. They may need to accept the invitation first.")

# 執行批量邀請
invite_results = invite_users_from_file(tenant_id, client_id, client_secret, filename, redirect_url)

# 保存用戶ID到CSV文件
print("\n正在獲取並保存用戶ID...")
save_user_ids_to_csv(invite_results)