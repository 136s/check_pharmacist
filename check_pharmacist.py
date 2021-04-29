import time
import pandas as pd
from selenium import webdriver

SEARCH_URL = "https://licenseif.mhlw.go.jp/search_iyaku/top.jsp"
SLEEP_SEC = 3
IN_CSV_NAME = "./list.csv"
OUT_CSV_NAME = "./output.csv"

# 名前を投げると「登録年」の list が返ってくる
def get_years(name) :
    driver.get(SEARCH_URL)
    time.sleep(SLEEP_SEC)
    search_box = driver.find_element_by_name("name")
    search_box.send_keys(name)
    search_box.submit()
    
    regi = driver.find_elements_by_class_name('REGISTRATION_TD')
    years = []
    for r in regi:
        years.append(r.text)
    return years

# csv は name, years カラムの 2 行からなる（ヘッダー付き） 
df = pd.read_csv(IN_CSV_NAME, encoding="shift-jis")
df["years"] = df["years"].astype(str)

driver = webdriver.Chrome()
for i, _ in df.iterrows():
    result = get_years(df.at[i, "name"])
    df.at[i, "years"] = " ".join(result) # スペース区切りで格納
driver.quit()

df.to_csv(OUT_CSV_NAME, encoding="shift_jis", index=False)