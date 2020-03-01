# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
# SendGrid 發送 mail 測試, 要配合 sendgrid.env 裡面的 SENDGRID_API_KEY 變數
# Edit by Max 2020/1/19
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    # 更改寄件人爲要顯示的 e-mail
    from_email='from_email@example.com',
    # 更改收件人爲要收件的 e-mail
    to_emails='to@example.com',
    # 信件主旨
    subject='Sending with Twilio SendGrid is Fun',
    # 信件內容
    html_content='<strong>And easy to do anywhere, even with Python</strong>')
try:
    # 這邊有用到 SENDGRID_API_KEY, 所以要使用 API KEY 的變數, 可以看 sendgrid.env
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    # 使用 str() 將 response.status_code 轉型爲 String
    print("response.status_code: " + str(response.status_code))
    # 使用 str() 將 response.body 轉型爲 String
    print("response.body: " + str(response.body))
    # 使用 str() 將 response.headers 轉型爲 String
    print("response.headers: " + str(response.headers))
except Exception as e:
    print(e.message)