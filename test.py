# from src.quran_search_in_text.ayeh_yab import AyehYab
from quran_search_in_text.ayeh_yab import AyehYab
file1 = open('1.txt', 'r', encoding='utf-8')
rows = file1.readlines()
a = AyehYab().ayeh_find(rows)

print(a['html_output'])
# print(a['list_output'])
# print(a['list_ayat'])
print('***********************************************')
a = AyehYab().clear_additions(html_text=' '.join(rows), tag="span", class_name="s")
print(a)

