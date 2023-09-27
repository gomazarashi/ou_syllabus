from getpass import getpass
from ou_syllabus import SyllabusData
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


WEEK_DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]



def get_course_number(driver, okadai_id, password):
    course_number_list = []
    driver.get("https://kyomu.adm.okayama-u.ac.jp/Portal/RichTimeOut.aspx")

    sleep(2)
    driver.find_element(By.ID, "error_lnkLogin_lnk").click()
    element = driver.find_element(By.ID, "username_input")
    element.send_keys(okadai_id)
    element.send_keys(Keys.ENTER)
    sleep(1)
    element = driver.find_element(By.ID, "password_input")
    element.send_keys(password)
    element.send_keys(Keys.ENTER)
    sleep(1)
    driver.find_element(By.ID, "ctl00_bhHeader_ctl18_lnk").click()
    driver.find_element(By.ID, "ctl00_bhHeader_ctl30_lnk").click()


    for day in WEEK_DAYS:
        for i in range(1, 11):
            try:
                element = driver.find_element(By.CSS_SELECTOR, "#ctl00_phContents_rrMain_ttTable_lct{}{}_ctl00_lblLctCd > a".format(day, i))
                course_number_list.append(element.text)
            except:
                pass
    driver.quit()
    return list(dict.fromkeys(course_number_list))

def get_textbook_info(course_number_list):
    for i in course_number_list:
        syllabus_data = SyllabusData()
        syllabus_data.scrape_syllabus(i)
        print("教科書情報は以下の通りです。")
        for textbook in syllabus_data.textbook_list:
            print("ISBN:{}, 書名:{}, 著者名:{}, 出版社:{}, 出版年:{}".format(
                textbook["isbn"], textbook["book_title"], textbook["author"], textbook["publisher"], textbook["year"]))
        print("------------")
        print("教科書の備考は「{}」です。".format(syllabus_data.textbook_memo))
        print("------------")





if __name__ == "__main__":
    print("入力された情報は履修時間割表の取得にのみ使用され、外部に送信されることはありません。\n")

    okadai_id = input("岡大IDを入力してください。\n")
    password = getpass("パスワードを入力してください。\n")

    driver = webdriver.Chrome(ChromeDriverManager().install())

    course_number_list= get_course_number(driver, okadai_id, password)
    get_textbook_info(course_number_list)
