# from src.quran_search_in_text.ayeh_yab import AyehYab
from quran_search_in_text.ayeh_yab import AyehYab
file1 = open('1.txt', 'r', encoding='utf-8')
rows = file1.readlines()

text = AyehYab().clear_additions(html_text=rows, tag="span", class_name="s")
print(text)
print('***********************************************')
text = AyehYab().ayeh_find(rows)
print(text)
print('***********************************************')
text = AyehYab().clear_additions(html_text=rows, tag="span", class_name="s")
print(text)
print('***********************************************')

# print(a['html_output'])
# print(a['list_output'])
# print(a['list_ayat'])


# a = AyehYab().standard_text(text=text.join(rows))
# print(a)

