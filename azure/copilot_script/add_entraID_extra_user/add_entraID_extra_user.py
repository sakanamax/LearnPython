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
    response = requests.post(url, headers=headers, json=payload)  # 發送POST請求以邀請用戶
    response.raise_for_status()  # 如果請求失敗，拋出異常
    return response.json()  # 返回邀請操作的結果

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
redirect_url = 'https://your-redirect-url.com'  # 重定向URL

# 執行批量邀請
invite_results = invite_users_from_file(tenant_id, client_id, client_secret, filename, redirect_url)