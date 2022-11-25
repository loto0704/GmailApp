import os
import sys
from dotenv import load_dotenv
from chardet import detect
import csv
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail(gmail, password, mail, mailText, subject):
    charset = 'iso-2022-jp'
    msg = MIMEText(mailText, 'plain', charset)
    msg['Subject'] = Header(subject.encode(charset), charset)
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(gmail, password)
    smtp_obj.sendmail(gmail, mail, msg.as_string())
    smtp_obj.quit()


def txt_read():
    with open(sys.argv[1], 'rb') as bf:  # バイナリーで読み込み
        binary_data = bf.read()
        encode_data = detect(binary_data)

    email_list = []
    with open(sys.argv[1], mode='r', encoding=encode_data['encoding']) as csv_file:
        f = csv.reader(csv_file, delimiter=',')
        next(f)  # headerスキップ
        for i in f:
            email_list.append(i[1])

        return email_list


def main():
    # .envファイルの内容を読み込む
    load_dotenv()
    email_list = txt_read()

    email_from = os.environ['EMAIL']
    password = os.environ['APP-PASSKEY']
    mail_text = 'メール本文'
    subject = '件名'
    for i in email_list:
        email_to = i
        send_mail(email_from, password, email_to, mail_text, subject)


if __name__ == '__main__':
    main()
