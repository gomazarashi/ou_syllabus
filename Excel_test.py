import pandas as pd
from pandas import DataFrame
import numpy as np

# 二学期のシートを読み込み
column=list(range(0, 17))
# 3,5列目を削除
column.remove(3)
column.remove(5)
print(column)
df_2nd_term = pd.read_excel('0000_2023_Liberal_Education_Class_Time_ALL.xlsx', sheet_name=1, skiprows=range(0, 5), usecols=column)
df_2nd_term = df_2nd_term.set_axis(["講義番号", "開講学期", "曜日", "時", "科目区分", "授業科目", "単位数", "担当教員", "履修対象_2023入",
                                "履修対象_2022入", "履修対象_2021入", "抽選対象科目", "教室", "備考", "シラバス"], axis=1)

