from ou_syllabus import SyllabusData
from bs4 import BeautifulSoup as bs4


with open('my_class.html', encoding='utf-8') as f: #履修登録画面のhtmlファイルを読み込む
    html = f.read()
# 曜日の略称のリスト
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
soup = bs4(html, 'html.parser')
course_number_list = []
for day in week:
    for i in range(1, 11):
        if soup.select_one("#ctl00_phContents_RegEdit_reTable_ttTable_lct" + day + str(i) + "_ctl00_lblLctCd > a") != None:
            course_number_list.append(soup.select_one("#ctl00_phContents_RegEdit_reTable_ttTable_lct" + day + str(i) + "_ctl00_lblLctCd > a").text)

course_number_list = list(dict.fromkeys(course_number_list))  # 順序を保持して重複を削除
# 各授業の教科書とその備考を取得
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
    
