import requests
from bs4 import BeautifulSoup as bs4
import time  # サーバーへの負荷を考慮して1秒待機するためにインポート
"""
# 教科書情報を格納するリストを定義
textbook_list = soup.select("#ctl00_phContents_ucSylContents_CateText_tdTextBooks > table  ")
# 参考書情報を格納するリストを定義
reference_list = soup.select("#ctl00_phContents_ucSylContents_cateReference_tdTextBooks>table span")
"""

# 結果を表示
"""print("講義名は「{}」です。".format(course_name.text))
print("教科書情報は以下の通りです。")
print(textbook_list)
print("参考書情報は以下の通りです。")
print((reference_list))
print(len(reference_list))"""


# シラバスデータに関するクラスを定義
class SyllabusData():
    def __init__(self):
        self.course_name = ""  # 講義名
        self.course_no = ""  # 講義番号
        self.class_ification = ""  # 科目区分
        self.term = ""  # 学期
        self.numbering_code = ""  # ナンバリングコード
        self.classroom = ""  # 教室
        self.required_or_elective = ""  # 必修・選択の別
        self.credit = ""  # 単位数
        self.day_and_period = ""  # 曜日と時限
        self.instructor = ""  # 担当教員
        self.sdgs = []  # 持続的な開発目標
        self.target_students = ""  # 対象学生
        self.other_faculty_students = ""  # 他学部学生の履修の可否
        self.contact = ""  # 連絡先
        self.office_hours = ""  # オフィスアワー
        self.department_specific = ""  # 学部・研究科独自の項目
        self.language = ""  # 使用言語
        self.course_description = ""  # 授業の概要
        self.learning_objectives = ""  # 学習目的
        self.learning_outcomes = ""  # 到達目標
        self.course_schedule = ""  # 授業計画
        self.out_of_class_learning = ""  # 授業時間外の学習(予習･復習)方法(成績評価への反映についても含む)
        self.teaching_format = {"lect_ratio": "", "group_work": "", "interactive_work": "", "thinking_work": "",
                                "understanding": "", "practical_type": "", "teaching_format_memo_for_student": ""}  # 授業形態
        self.equipment = {"media": "", "lms": "", "human_support": "", "memo_for_student": ""}  # 使用メディア・機器・人的支援の活用
        self.textbook_list = []  # 教科書情報を格納するリスト
        self.textbook_memo = ""  # 教科書の備考
        self.reference_list = []  # 参考書情報を格納するリスト
        self.reference_memo = ""  # 参考書の備考
        self.grading = ""  # 成績評価基準
        self.prerequisites = ""  # 受講要件
        self.teache_training = ""  # 教職課程該当科目
        self.jabee = ""  # JABEEとの関連
        self.sdgs_detail = ""  # 持続的な開発目標(SDGs)(詳細)
        self.professional_faculty = ""  # 実務経験のある教員による授業科目
        self.notes = ""  # 備考/履修上の注意
        self.lcos = ""  # 学習成果(LCOs)

    def scrape_syllabus(self, course_no):
        url = "https://kyomu.adm.okayama-u.ac.jp/Portal/Public/Syllabus/DetailMain.aspx?lct_year=2023&lct_cd={}&je_cd=1".format(course_no)
        time.sleep(1)  # 1秒待機
        response = requests.get(url)

        # 正しいレスポンスが得られなければ例外を発生させる
        response.raise_for_status()

        soup = bs4(response.text, "html.parser")
        self.course_name = soup.select_one("#ctl00_phContents_sylSummary_txtSbjName_lbl").text
        self.course_no = soup.select_one("#ctl00_phContents_sylSummary_txtLctCd_lbl").text
        self.class_ification = soup.select_one("#ctl00_phContents_sylSummary_txtSbjArea_lbl").text
        self.term = soup.select_one("#ctl00_phContents_sylSummary_txtDeCtrCd_lbl").text
        self.numbering_code = soup.select_one("#ctl00_phContents_sylSummary_txtNumbering_lbl").text
        self.classroom = soup.select_one("#ctl00_phContents_sylSummary_txtClassroom_lbl").text
        self.required_or_elective = soup.select_one("#ctl00_phContents_sylSummary_txtReqNm_lbl").text
        self.credit = soup.select_one("#ctl00_phContents_sylSummary_txtCredits_lbl").text
        self.day_and_period = soup.select_one("#ctl00_phContents_sylSummary_txtPeriod_lbl").text
        self.instructor = soup.select_one("#ctl00_phContents_sylSummary_txtStaffName_lbl").text
        for sdg in soup.select("#ctl00_phContents_sylSummary_trSDGsicons img"):
            self.sdgs.append(sdg.get("alt"))
        self.target_students = soup.select_one("#ctl00_phContents_ucSylContents_cateTargetStudents_lblNormal").text
        self.other_faculty_students = soup.select_one("#ctl00_phContents_ucSylContents_cateOtherFaculties_selectedText").text
        self.contact = soup.select_one("#ctl00_phContents_ucSylContents_cateContact_trJapanese").text.strip()
        self.office_hours = soup.select_one("#ctl00_phContents_ucSylContents_cateOfficeHours_trJapanese").text.strip()
        self.department_specific = soup.select_one("#ctl00_phContents_ucSylContents_CateSpecificItems_lblNormal").text
        self.language = soup.select_one("#ctl00_phContents_ucSylContents_CateLanguage_selectedText").text
        self.course_description = soup.select_one("#ctl00_phContents_ucSylContents_cateDescription_lblNormal").text
        self.learning_objectives = soup.select_one("#ctl00_phContents_ucSylContents_cateObectives_lblNormal").text
        self.learning_outcomes = soup.select_one("#ctl00_phContents_ucSylContents_CateOutcomes_lblNormal").text
        self.course_schedule = soup.select_one("#ctl00_phContents_ucSylContents_CateSchedule_lblNormal").text
        self.out_of_class_learning = soup.select_one("#ctl00_phContents_ucSylContents_CateOutside_lblNormal").text
        self.teaching_format["lect_ratio"] = soup.select_one("#ctl00_phContents_ucSylContents_CateFormatClass_selectedText").text.replace("：", ":")
        self.teaching_format["group_work"] = soup.select_one("#ctl00_phContents_ucSylContents_CateAlGroupWork_selectedText").text
        self.teaching_format["interactive_work"] = soup.select_one("#ctl00_phContents_ucSylContents_CateAlTeacher_selectedText").text
        self.teaching_format["thinking_work"] = soup.select_one("#ctl00_phContents_ucSylContents_CateAlThinking_selectedText").text
        self.teaching_format["understanding"] = soup.select_one("#ctl00_phContents_ucSylContents_CateAlReflections_selectedText").text
        self.teaching_format["practical_type"] = soup.select_one("#ctl00_phContents_ucSylContents_CateFormatPractical_selectedText").text
        self.teaching_format["teaching_format_memo_for_student"] = soup.select_one("#ctl00_phContents_ucSylContents_CateFormatMemo_lblNormal").text
        self.equipment["media"] = soup.select_one("#ctl00_phContents_ucSylContents_CateEquipmentMedia_selectedText").text
        self.equipment["lms"] = soup.select_one("#ctl00_phContents_ucSylContents_CateEquipmentLms_selectedText").text
        self.equipment["human_support"] = soup.select_one("#ctl00_phContents_ucSylContents_CateEquipmentHuman_selectedText").text
        self.equipment["memo_for_student"] = soup.select_one("#ctl00_phContents_ucSylContents_CateEquipmentMemo_lblNormal").text
        i = 1
        while soup.select_one("#ctl00_phContents_ucSylContents_CateText_ItemBookTextBook_{}_lblRowHeader_lbl".format(i)) != None:
            self.textbook_list.append({"isbn": soup.select_one("#ctl00_phContents_ucSylContents_CateText_ItemBookTextBook_{}_lblIsbn".format(i)).text,
                                       "book_title": soup.select_one("#ctl00_phContents_ucSylContents_CateText_ItemBookTextBook_{}_lblBookName > a".format(i)).text,
                                       "author": soup.select_one("#ctl00_phContents_ucSylContents_CateText_ItemBookTextBook_{}_lblAuthor".format(i)).text,
                                       "publisher": soup.select_one("#ctl00_phContents_ucSylContents_CateText_ItemBookTextBook_{}_lblPublisher".format(i)).text,
                                       "year": soup.select_one("#ctl00_phContents_ucSylContents_CateText_ItemBookTextBook_{}_lblYear".format(i)).text})
            i += 1
        self.textbook_memo = soup.select_one("#ctl00_phContents_ucSylContents_CateText_itemBookBook_Note_lblNormal").text
        i = 1
        while soup.select_one("#ctl00_phContents_ucSylContents_cateReference_ItemBookReferenceBook_{}_lblRowHeader_lbl".format(i)) != None:
            self.reference_list.append({"isbn": soup.select_one("#ctl00_phContents_ucSylContents_cateReference_ItemBookReferenceBook_{}_lblIsbn".format(i)).text,
                                        "book_title": soup.select_one("#ctl00_phContents_ucSylContents_cateReference_ItemBookReferenceBook_{}_lblBookName > a".format(i)).text,
                                        "author": soup.select_one("#ctl00_phContents_ucSylContents_cateReference_ItemBookReferenceBook_{}_lblAuthor".format(i)).text,
                                        "publisher": soup.select_one("#ctl00_phContents_ucSylContents_cateReference_ItemBookReferenceBook_{}_lblPublisher".format(i)).text,
                                        "year": soup.select_one("#ctl00_phContents_ucSylContents_cateReference_ItemBookReferenceBook_{}_lblYear".format(i)).text})
            i += 1
        self.reference_memo = soup.select_one("#ctl00_phContents_ucSylContents_cateReference_itemBookBook_Note_lblNormal").text
        self.grading = soup.select_one("#ctl00_phContents_ucSylContents_cateGrading_lblNormal").text
        self.prerequisites = soup.select_one("#ctl00_phContents_ucSylContents_catePrerequisites_lblNormal").text
        self.teache_training = soup.select_one("#ctl00_phContents_ucSylContents_cateTeacher_lblNormal").text
        self.jabee = soup.select_one("#ctl00_phContents_ucSylContents_CateJabee_lblNormal").text
        self.sdgs_detail = soup.select_one("#ctl00_phContents_ucSylContents_cateSdgs_RefGv").text
        self.professional_faculty = soup.select_one("#ctl00_phContents_ucSylContents_cateExperience_trMain").text
        self.notes = soup.select_one("#ctl00_phContents_ucSylContents_cateNote_lblNormal").text
        self.lcos = soup.select_one("#ctl00_phContents_ucSylContents_cateLcos_lvRefer_ctrl0_lblname_j").text


def main():
    course_number = input("講義番号を入力してください (例: 2023098452)\n")
    syllabus_data = SyllabusData()
    syllabus_data.scrape_syllabus(course_number)
    print("講義名は「{}」です。".format(syllabus_data.course_name))
    print("講義番号は「{}」です。".format(syllabus_data.course_no))
    print("科目区分は「{}」です。".format(syllabus_data.class_ification))
    print("学期は「{}」です。".format(syllabus_data.term))
    print("ナンバリングコードは「{}」です。".format(syllabus_data.numbering_code))
    print("教室は「{}」です。".format(syllabus_data.classroom))
    print("必修・選択の別は「{}」です。".format(syllabus_data.required_or_elective))
    print("単位数は「{}」です。".format(syllabus_data.credit))
    print("曜日と時限は「{}」です。".format(syllabus_data.day_and_period))
    print("担当教員は「{}」です。".format(syllabus_data.instructor))
    print("持続的な開発目標は「{}」です。".format(syllabus_data.sdgs))
    print("対象学生は「{}」です。".format(syllabus_data.target_students))
    print("他学部学生の履修の可否は「{}」です。".format(syllabus_data.other_faculty_students))
    print("連絡先は「{}」です。".format(syllabus_data.contact))
    print("オフィスアワーは「{}」です。".format(syllabus_data.office_hours))
    print("学部・研究科独自の項目は「{}」です。".format(syllabus_data.department_specific))
    print("使用言語は「{}」です。".format(syllabus_data.language))
    print("授業の概要は「{}」です。".format(syllabus_data.course_description))
    print("学習目的は「{}」です。".format(syllabus_data.learning_objectives))
    print("到達目標は「{}」です。".format(syllabus_data.learning_outcomes))
    print("授業計画は「{}」です。".format(syllabus_data.course_schedule))
    print("授業時間外の学習(予習･復習)方法(成績評価への反映についても含む)は「{}」です。".format(syllabus_data.out_of_class_learning))
    print("全授業時間に対する[講義形式]:[講義形式以外]の実施割合は「{}」です。".format(syllabus_data.teaching_format["lect_ratio"]))
    print("協働的活動(ペア･グループワーク､ディスカッション､プレゼンテーションなど)「{}」です。".format(syllabus_data.teaching_format["group_work"]))
    print("対話的活動(教員からの問いかけ､質疑応答など)は「{}」です。".format(syllabus_data.teaching_format["interactive_work"]))
    print("思考活動(クリティカル･シンキングの実行､問いを立てるなど)は「{}」です。".format(syllabus_data.teaching_format["thinking_work"]))
    print("理解の確認･促進(問題演習､小テスト､小レポート､授業の振り返りなど)は「{}」です。".format(syllabus_data.teaching_format["understanding"]))
    print("実践型科目タイプは「{}」です。".format(syllabus_data.teaching_format["practical_type"]))
    print("授業形態-履修者への連絡事項は「{}」です。".format(syllabus_data.teaching_format["teaching_format_memo_for_student"]))
    print("視聴覚メディア(PowerPointのスライド､CD､DVDなど)は「{}」です。".format(syllabus_data.equipment["media"]))
    print("学習管理システム(Moodleなど)は「{}」です。".format(syllabus_data.equipment["lms"]))
    print("人的支援(ゲストスピーカー､TA､ボランティアなど)は「{}」です。".format(syllabus_data.equipment["human_support"]))
    print("履修者への連絡事項は「{}」です。".format(syllabus_data.equipment["memo_for_student"]))
    print("教科書情報は以下の通りです。")
    for textbook in syllabus_data.textbook_list:
        print("ISBN:{}, 書名:{}, 著者名:{}, 出版社:{}, 出版年:{}".format(
            textbook["isbn"], textbook["book_title"], textbook["author"], textbook["publisher"], textbook["year"]))
    print("教科書の備考は「{}」です。".format(syllabus_data.textbook_memo))
    print("参考書情報は以下の通りです。")
    for reference in syllabus_data.reference_list:
        print("ISBN:{}, 書名:{}, 著者名:{}, 出版社:{}, 出版年:{}".format(
            reference["isbn"], reference["book_title"], reference["author"], reference["publisher"], reference["year"]))
    print("参考書の備考は「{}」です。".format(syllabus_data.reference_memo))
    print("成績評価基準は「{}」です。".format(syllabus_data.grading))
    print("受講要件は「{}」です。".format(syllabus_data.prerequisites))
    print("教職課程該当科目は「{}」です。".format(syllabus_data.teache_training))
    print("JABEEとの関連は「{}」です。".format(syllabus_data.jabee))
    print("持続的な開発目標(SDGs)(詳細)は「{}」です。".format(syllabus_data.sdgs_detail))
    print("実務経験のある教員による授業科目は「{}」です。".format(syllabus_data.professional_faculty))
    print("備考/履修上の注意は「{}」です。".format(syllabus_data.notes))
    print("学習成果(LCOs)は「{}」です。".format(syllabus_data.lcos))


if __name__ == "__main__":
    main()
