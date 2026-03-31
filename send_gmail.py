import os
import base64
from email.message import EmailMessage

from dotenv import load_dotenv

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 送信だけできればOKな最小スコープ
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def gmail_auth():
    """OAuth認証してGmail serviceを返す（token.jsonを再利用）"""
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)

def create_message(to_email: str, subject: str, body: str):
    """メール本文をGmail API送信用に変換"""
    message = EmailMessage()
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": encoded_message}

def send_email(service, to_email: str, subject: str, body: str):
    message = create_message(to_email, subject, body)
    result = service.users().messages().send(userId="me", body=message).execute()
    print("✅ 送信成功！ messageId:", result.get("id"))

def main():
    load_dotenv()

    to_email = os.getenv("TO_EMAIL")
    subject = os.getenv("SUBJECT", "No subject")
    body = os.getenv("BODY", "")

    print("DEBUG TO_EMAIL =", to_email)  # ←確認用（あとで消してOK）

    if not to_email:
        print("❌ TO_EMAIL が .env に設定されていません")
        return

    service = gmail_auth()
    send_email(service, to_email, subject, body)
if __name__ == "__main__":
    main()

