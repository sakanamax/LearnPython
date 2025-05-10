#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
確認 Azure AD/Entra ID 認證有效性的工具

此程式用於測試 Azure AD (Entra ID) 的認證是否有效，
通過嘗試獲取 Microsoft Graph API 的存取令牌來驗證。
正確的認證將返回 200 狀態碼和有效的令牌。
"""

import requests  # 用於發送 HTTP 請求
import json      # 用於處理 JSON 格式數據
import os        # 用於操作系統功能

# 讀取外部配置檔案
def load_config(config_file_path='config.json'):
    """
    從指定的 JSON 檔案讀取配置資訊
    
    參數:
        config_file_path (str): 配置檔案的路徑，預設為 'config.json'
    
    返回:
        dict: 包含配置資訊的字典
        
    異常:
        FileNotFoundError: 找不到配置檔案時拋出
        JSONDecodeError: JSON 格式無效時拋出
    """
    try:
        with open(config_file_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print(f"錯誤: 找不到配置檔案 {config_file_path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"錯誤: 配置檔案 {config_file_path} 格式無效")
        exit(1)

# 載入配置
config = load_config()

# 檢查必要的配置項是否存在
required_configs = ['tenant_id', 'client_id', 'client_secret']
for config_item in required_configs:
    if config_item not in config:
        print(f"錯誤: 配置檔案中缺少必要的項目 '{config_item}'")
        exit(1)

# 設定令牌請求的 URL 和數據
token_url = f"https://login.microsoftonline.com/{config['tenant_id']}/oauth2/v2.0/token"
token_data = {
    'grant_type': 'client_credentials',      # 授權類型: 客戶端憑證
    'client_id': config['client_id'],        # 客戶端 ID (應用程式 ID)
    'client_secret': config['client_secret'], # 客戶端密鑰
    'scope': 'https://graph.microsoft.com/.default'  # API 範圍 (Microsoft Graph)
}

# 嘗試獲取訪問令牌
try:
    # 發送 POST 請求以獲取訪問令牌
    token_response = requests.post(token_url, data=token_data)
    token_response.raise_for_status()  # 如果回應狀態碼不是 2xx，則拋出異常
    
    # 輸出回應資訊
    print(f"狀態碼: {token_response.status_code}")  # 200 表示成功
    print(f"回應: {token_response.json()}")         # 包含令牌的 JSON 回應
except requests.RequestException as e:
    # 處理請求異常
    print(f"發生錯誤: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"詳細錯誤: {e.response.text}")  # 輸出錯誤的詳細信息