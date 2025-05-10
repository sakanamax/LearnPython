# 批量將 Entra ID 外部用戶加入到企業應用程式

這個程式可以批量將多個 Microsoft Entra ID 外部使用者加入到企業應用程式。

## 檔案說明

- `add_multiple_users_to_enterprise_application.py`: 主程式
- `config.json`: 配置檔案
- `users.csv`: 使用者清單

## 配置說明

### config.json 配置檔說明

```json
{
    "tenant_id": "您的租戶ID",
    "client_id": "您的應用程式ID",
    "client_secret": "您的應用程式密碼",
    "app_id": "企業應用程式的服務主體ID",
    "csv_file": "users.csv"
}
```

### users.csv 格式說明

CSV 檔案需包含以下欄位：
- `user_id`: 使用者的 Object ID (必須)
- `user_name`: 使用者名稱 (選擇性，用於顯示)

範例：
```
user_id,user_name
00000000-0000-0000-0000-000000000001,張三
```

## 使用方法

1. 編輯 `config.json` 填入您的租戶資訊和應用程式資訊
2. 編輯 `users.csv` 填入要加入的使用者 Object ID 和名稱
3. 執行指令：
   ```
   python add_multiple_users_to_enterprise_application.py
   ```

## 相關程式說明

### add_entraID_extra_user.py

如果您需要先邀請外部使用者加入您的 Entra ID，可以使用 `add_entraID_extra_user.py` 程式。該程式會將邀請的使用者 ID 和顯示名稱保存到 `invited_users_with_ids.csv` 檔案，方便您後續將這些使用者加入到企業應用程式中。

使用流程：
1. 使用 `add_entraID_extra_user.py` 邀請外部使用者
2. 取得生成的 `invited_users_with_ids.csv` 檔案
3. 使用此檔案內容建立 `users.csv`
4. 使用本程式將這些使用者加入企業應用程式

## 常見問題及解決方法

### 執行失敗的可能原因及解決方法

1. **app_id 不正確**: 確認 app_id 是服務主體的 Object ID，而不是應用程式 (客戶端) ID。您可以在 Azure Portal > 企業應用程式 > 您的應用程式 > 屬性中找到服務主體 ID。

2. **權限不足**: 確保您的應用程式有 `Directory.ReadWrite.All` 或 `Application.ReadWrite.All` 權限，並已獲得管理員同意。

3. **使用者 ID 不正確**: 確保 users.csv 中的 user_id 是真實存在的使用者 Object ID。

4. **使用者尚未接受邀請**: 外部使用者必須先接受邀請，才能被加入到企業應用程式中。

5. **API 呼叫失敗**: 程式會顯示詳細的 API 回應資訊，可以根據這些資訊來診斷問題。

## 如何取得所需 ID

1. **租戶 ID**: 在 Azure Portal > Azure Active Directory > 概觀中找到
2. **應用程式 ID 和密碼**: 在 Azure Portal > 應用程式註冊中建立應用程式
3. **企業應用程式 Object ID**: 在 Azure Portal > 企業應用程式 > 選擇您的應用程式 > 屬性，這裡的「物件識別碼」
4. **使用者 Object ID**: 在使用者屬性頁面找到，或從 `invited_users_with_ids.csv` 檔案中獲取

## 所需權限

應用程式需要具有 `Directory.ReadWrite.All` 或 `Application.ReadWrite.All` 權限，並取得管理員同意。

## 輸出說明

程式執行時會顯示每一步的操作結果，包括 API 呼叫詳情和錯誤訊息。執行完成後，會顯示成功和失敗的數量統計。
