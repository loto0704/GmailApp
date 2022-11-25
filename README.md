# Gmailメール送信色々
## アプリパスワードを使用したメール送信
※コードは「SendGmail-AppPassKey」を参照

### ライブラリのインストール
```
pip install -r requirements.txt
```
※下記を使用しないのであれば、標準ライブラリのみでOK

使用ライブラリ
- chardet：文字コード自動判別のために使用
- python-dotenv：.envファイルの読み込みに使用

### 使用方法
引数にて送信者のメールアドレスリストのCSVを指定
```
python send_mail.py ./sample-email-list.py
```
