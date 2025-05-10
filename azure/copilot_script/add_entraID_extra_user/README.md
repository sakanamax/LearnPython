# Entra ID 外部用戶邀請與 ID 獲取程式

這個 Python 程式用於批量邀請外部用戶加入 Microsoft Entra ID (Azure AD)，並自動獲取這些用戶的 Object ID。

## 功能說明

- 批量邀請外部用戶加入 Entra ID
- 自動獲取已邀請用戶的 Object ID
- 生成包含用戶 ID 和顯示名稱的 CSV 檔案，方便後續操作
- 詳細的錯誤處理和日誌輸出

## 目錄結構

```
add_entraID_extra_user.py - 主程式
config.json - 配置文件
users.csv - 待邀請用戶清單
invited_users_with_ids.csv - 輸出的用戶 ID 檔案 (執行後生成)
```

## 配置文件

### config.json

這個文件包含了 Azure AD 應用程式的配置參數：

```json
{
    "tenant_id": "YOUR_TENANT_ID",
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
}
```

### users.csv

這個文件包含了要邀請的用戶資訊，格式如下：

```csv
email,display_name
user@example.com,用戶名稱
```

- **email**: 必填，用戶的電子郵件地址
- **display_name**: 必填，用戶在 Entra ID 中顯示的名稱

## 執行步驟

1. 安裝所需的 Python 套件：

    ```sh
    pip install requests
    ```

2. 編輯 `config.json` 檔案，填入您的 Azure AD 應用程式資訊

3. 編輯 `users.csv` 檔案，填入要邀請的用戶資訊

4. 執行 Python 程式：

    ```sh
    python add_entraID_extra_user.py
    ```

5. 執行完成後，程式會生成 `invited_users_with_ids.csv` 檔案，包含成功邀請並獲取到 ID 的用戶資訊

## 輸出檔案說明

程式執行後會生成 `invited_users_with_ids.csv` 檔案，格式如下：

```csv
user_id,display_name
00000000-0000-0000-0000-000000000001,用戶名稱
```

此檔案只包含成功獲取到 ID 的用戶資訊，可直接用於後續將用戶加入到企業應用程式等操作。

## 後續操作

您可以使用生成的 `invited_users_with_ids.csv` 檔案作為 `add_multiple_users_to_enterprise_application/users.csv` 的來源，將已邀請的外部用戶加入到企業應用程式中。

## 必要的 API 權限

此程式需要 Azure AD 應用程式具有以下 API 權限：
- `User.Invite.All` - 用於邀請外部用戶
- `User.Read.All` - 用於查詢用戶資訊

**重要**: 這些權限需要取得管理員同意才能正常使用。

## 注意事項

- 外部用戶需要接受邀請後才能完全啟用，某些情況下可能無法立即獲取用戶 ID
- 程式中有 2 秒的延遲來等待系統處理，如果仍無法獲取 ID，可能需要用戶接受邀請後再查詢
- 請妥善保管 `config.json` 中的憑證資訊，避免外洩

## 故障排除

- **無法獲取用戶 ID**: 確認用戶已接受邀請，或嘗試增加延遲時間
- **邀請失敗**: 檢查應用程式權限是否足夠，以及是否已獲得管理員同意
- **API 錯誤**: 查看終端機輸出的詳細錯誤訊息

## 聯絡方式

如有任何問題，請聯絡系統管理員
