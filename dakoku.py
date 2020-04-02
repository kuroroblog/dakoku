# -*- coding: utf-8 -*-

import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 入力内容
# --------------------

email = ''
passward = ''
# chrome driverのファイルパス (例 : /usr/local/bin/chromedriver)
executable_path = ''

# --------------------

options = Options()

# ヘッドレスモードで実行する場合
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, executable_path=executable_path)

try:
    driver.get("https://id.jobcan.jp/users/sign_in?app_key=atd")

    # メールアドレスとパスワードを入力
    driver.find_element_by_id('user_email').send_keys(email)
    driver.find_element_by_id('user_password').send_keys(passward)

    # ログインボタンをクリック
    driver.find_element_by_name('commit').click()

    # 簡易的にJSが評価されるまで秒数で待つ
    time.sleep(5)

    # 打刻
    driver.find_element_by_id('adit-button-push').click()

    # 簡易的にJSが評価されるまで秒数で待つ
    time.sleep(5)

except:
    traceback.print_exc()

finally:

    # エラーが起きても起きなくてもブラウザを閉じる
    driver.quit()
