"""
批量將多個 Microsoft Entra ID 外部使用者加入到企業應用程式
功能：
1. 從 CSV 檔案讀取使用者清單
2. 將這些使用者加入到指定的企業應用程式
"""

import requests
import json
import csv
import time

def get_access_token(tenant_id, client_id, client_secret):
    """
    從 Microsoft Graph API 獲取存取令牌
    
    參數:
        tenant_id (str): Azure AD 租戶 ID
        client_id (str): 應用程式 ID
        client_secret (str): 應用程式密碼
    
    回傳:
        str: 存取令牌
    """
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json().get('access_token')

def add_user_to_app(access_token, user_id, app_id):
    """
    將使用者加入到企業應用程式
    
    參數:
        access_token (str): Graph API 存取令牌
        user_id (str): 使用者的 Object ID
        app_id (str): 企業應用程式的 Object ID
    
    回傳:
        dict: API 回應結果
    """
    # 使用 servicePrincipals API 為正確端點
    url = f"https://graph.microsoft.com/v1.0/servicePrincipals/{app_id}/appRoleAssignments"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "principalId": user_id,
        "principalType": "User",
        "resourceId": app_id
    }
    
    # 增加錯誤診斷資訊
    print(f"正在呼叫 API: {url}")
    print(f"使用的 payload: {json.dumps(payload, indent=2)}")
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        # 列印完整的 API 回應以便診斷
        print(f"API 回應狀態碼: {response.status_code}")
        print(f"API 回應內容: {response.text}")
        response.raise_for_status()  # 如果狀態碼不是 2xx，拋出異常
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API 呼叫失敗: {str(e)}")
        if hasattr(e, 'response'):
            print(f"錯誤詳情: {e.response.text}")
        return {"error": {"message": str(e)}}

def add_users_from_csv(tenant_id, client_id, client_secret, csv_file, app_id):
    """
    從 CSV 檔案批量加入使用者到應用程式
    
    參數:
        tenant_id (str): Azure AD 租戶 ID
        client_id (str): 應用程式 ID
        client_secret (str): 應用程式密碼
        csv_file (str): 使用者列表 CSV 檔案路徑
        app_id (str): 企業應用程式的 Object ID
    """
    # 獲取訪問令牌
    access_token = get_access_token(tenant_id, client_id, client_secret)
    print("已獲取訪問令牌")
    
    # 讀取 CSV 檔案
    results = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = row['user_id']
            user_name = row.get('user_name', user_id)
            
            try:
                print(f"正在將用戶 {user_name} 加入到應用程式...")
                result = add_user_to_app(access_token, user_id, app_id)
                
                if 'error' in result:
                    print(f"加入用戶 {user_name} 失敗: {result['error'].get('message', '未知錯誤')}")
                else:
                    print(f"成功加入用戶 {user_name}")
                
                results.append({
                    'user_id': user_id,
                    'user_name': user_name,
                    'result': result
                })
                
                # 暫停一下，避免速率限制
                time.sleep(1)
                
            except Exception as e:
                print(f"處理用戶 {user_name} 時發生錯誤: {str(e)}")
                results.append({
                    'user_id': user_id,
                    'user_name': user_name,
                    'error': str(e)
                })
    
    return results

def main():
    """
    主程式：讀取設定並執行批量加入使用者
    """
    # 讀取配置
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    
    tenant_id = config['tenant_id']
    client_id = config['client_id']
    client_secret = config['client_secret']
    app_id = config['app_id']        # 企業應用程式的 Object ID
    csv_file = config.get('csv_file', 'users.csv')  # 使用者列表檔案
    
    # 執行批量加入
    results = add_users_from_csv(tenant_id, client_id, client_secret, csv_file, app_id)
    
    # 輸出摘要
    success_count = sum(1 for r in results if 'error' not in r and 'error' not in r.get('result', {}))
    print(f"\n加入完成: {success_count} 成功, {len(results) - success_count} 失敗")

if __name__ == "__main__":
    main()
