import requests
import os

# 取得したいURL
url = "https://diamondgotcat.github.io/MathConsole/main/main.py"

# GETリクエストを送信し、レスポンスを取得
response = requests.get(url)

# レスポンスのステータスコードを確認
if response.status_code == 200:
    # レスポンスのテキストデータをファイルに書き込む
    try:
      os.mkdir("/usr/local/share/mathconsole/bin/")
    except:
      pass
  
    with open("/usr/local/share/mathconsole/bin/main.py", "w", encoding="utf-8") as file:
        file.write(response.text)
    with open("/usr/local/share/mathconsole/bin/mathconsole", "w", encoding="utf-8") as file:
        file.write("""

#!/bin/bash

bash -c "$SHELL -c 'python3 /usr/local/share/mathconsole/bin/main.py'"

        """)
    os.system("chmod +x /usr/local/share/mathconsole/bin/mathconsole")
    print("Installed to 'mathconsole' in '/usr/local/share/mathconsole/bin/'")
else:
    print(f"Error Downloading: {response.status_code}")
