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

'''
AyehYab().ayeh_find(text=rows, quran_url = 'https://data.belquran.com/fa-IR/Quran/s/', ayeh_class = 'ayeh', paragraph_mark = '</br>', tag = 'a', min_word = 3, min_len_pure_text = 10, flag_identifying = 1)
'''