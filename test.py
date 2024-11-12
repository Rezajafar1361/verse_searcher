from src.quran_search_in_text.ayeh_yab import AyehYab

file1 = open('1.txt', 'r', encoding='utf-8')
rows = file1.readlines()
a = AyehYab().ayeh_find(rows)

print(a['html_output'])
print(a['list_output'])
print(a['list_ayat'])
