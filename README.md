# General description
Each paragraph of the text is examined separately and if there is a verse in it, it is observed.
The location of the verse along with the address of the verse in the Quran is presented in a list in the output.
Also, the input text can be converted into an HTML text in which the verses of the Qur'an are placed in their own tag and have a title, as well as a link to the Qur'an page on the relevant site.
Input can be text or a list of texts.

------------

## github
The source code is available at the following address:
https://github.com/Rezajafar1361/verse_searcher.git

------------
## def  ayeh_find
### INPUT VALUE
1. text:
>متن ورودی 
2. quran_url:
> شماره سوره و شماره آیه به این لینک اضافه شده و لینک روی آیه را ایجاد میکنند
این لینک باید به صورت زیر کار کند:
url/شماره سوره/شماره آیه
3. ayeh_class: 
> کلاسی که به تگ آیه سوار میشود
4. paragraph_mark:
> از آنجا که ورودی به صورت لیستی از متنهاست این تگ چیزی است که مابین متنها در پاراگرافهای مختلف قرار میگیرد مانند
/br , p , hr 
5. tag:
> تگی که متن آیه در آن قرار میگیرد باید به صورت تکست بدون علامت بزرگتر و کوچکتر باشد مانند
p  ,  a  ,  span  ,  ayeh  ,  quran
6. min_word:
> حداقل تعداد کلمه ای که در جستجوی قرآنی شرکت میکند-اگر از 2 کمتر بود 2 در نظر گرفته میشود
7. min_len_pure_text:
> حداقل تعداد حرف قسمت متن برای آیه یابی که اگر از 10 کمتر بود 10 در نظر گرفته میشود
8. flag_identifying:
> در این کد اگر برای یک تکه متن چند آیه قرآن ناپیوسته پیشنهاد شود یعنی آن تکه در قسمتهای مختلف قرآن موجود است  فلذا ابتدا با کل آدرس آیاتی که در کل متن ورودی هستند تطبیق داده میشود اگر یکی از آدرس های اختصاص یافته به آن تکه متن یا +1 یا -1 آن در آدرسهای آن پاراگراف بود آن آدرس برگزیده میشود در غیر این صورت اگر این فلگ صفر بود هیچ آدرسی برای آن تکه متن برگزیده نمیشود و صرفا تگ آیه به آن میخورد و اگر این تگ یک بود اولین آدرس از بین آدرسهای اختصاص داده شده برگزیده میشود



### OUTPUT VALUE
return: خروجی به صورت یک دیکشنری است با سه کلید و مقدار
- html_output:
> کلید اول متن به صورت اچ تی ام ال است که همان متن ورودی است و لیکن آیات آن با مقادیر مناسب تگ گذاری شده است بر روی هر آیه عنوان قرار داده شده به علاوه یک تگ مخصوص و همچنین لینک و همچنین یک ویژگی برای تعیین  شماره آیات  شماره آیات یک رشته از اعداد(شماره آیه) است. ممکن است یک عدد یا چند عدد که با , جدا شده اند در آن باشد
- list_output:
> کلید دوم اطلاعات آیات پیدا شده در پاراگرافهاست که به صورت یک لیست از لیستهاست که درون هر کدام یک یا چند دیکشنری است هر لیست داخلی متناظر با یک پاراگراف است مقادیر دیکشنری عبارتند از
1. ayehid:
> به صورت یک رشته که یک عدد و یا چند عدد که با ، جدا شده اند داشته باشد البته اگر شماره آیه پیدا نشد این لیست تهی خواهد بود
2. ayeh_text:
> متن تکه ای از متن که به عنوان آیه تشخیص داده شده است
3. index_start_end:
> ایندکس ابتدایی و انتهایی تکه متنی که به عنوان آیه تشخیص داده شده است
به صورت یک تاپل با دو عدد شروع و پایان
4. ayeh_adress_text:
> (این متن بر روی تول تیپ میتواند سوار شود)آدرس متنی تکه متنی که به عنوان آیه شناسایی شده است
5. link_ayeh:
> لینکی که میتواند بر آن تکه متن سوار شود
- list_ayat:
> در این کلید کل آیات به کار رفته در متن ورودی به صورت لیستی از اعداد ارائه میشود

------------


## def  clear_additions
این تابع بدین منظور تهیه شده تا تمامی تگهایی که تابع آیه یاب به یک متن زده را حذف کند
- html_text:
> متن ورودی که به صورت یک رشته باید باشد(لزومی بر پاراگراف کردن نیست و یک متن بلند نیز در اینجا قابل بارگذاری است)
- tag:
> تگی که باید حذف شود(به صورت پیش فرض تگ پیش فرض تابع آیه یاب را ملاک قرار میدهد)
- class_name:
> فقط آن تگهایی پاک میشوند که این کلاس را دارا باشند(به صورت پیش فرض همان کلاس تابع آیه یاب ملاک قرار گرفته است)
- return:
> خروجی یک رشته خالی شده از کلیه ی تگها و اضافات تابع آیه یاب است

------------

## example for ayehyab
##### sample example
```python
from quran_search_in_text.ayeh_yab import AyehYab

#open txt file or another text
file = open('1.txt', 'r', encoding='utf-8')
rows = file.readlines()

output = AyehYab().ayeh_find(rows)
```

##### full example
```python
from quran_search_in_text.ayeh_yab import AyehYab
file = open('1.txt', 'r', encoding='utf-8')
rows = file.readlines()

# remove all previous tags of this module
text = AyehYab().clear_additions(html_text=rows, tag="span", class_name="s")

# verse search with all settings
output = AyehYab().ayeh_find(
					text=text,
					quran_url = 'https://data.belquran.com/fa-IR/Quran/s/',
					ayeh_class = 'ayeh',
					paragraph_mark = '</br>',
					tag = 'a',
					min_word = 3,
					min_len_pure_text = 10,
					flag_identifying = 1
				   )

```

------------

## pip installation
		pip install quran_search_in_text


------------


## authors
name: Reza jafarzadeh
email: rezajafar90@gmail.com
from: Iran


------------

[![quran](https://islam4u.pro/blog/wp-content/uploads/2023/12/DALL%C2%B7E-2023-12-03-12.53.52-A-wide-artistic-interpretation-of-the-last-chapter-of-the-Holy-Quran.-The-image-should-depict-an-open-book-with-Arabic-script-symbolizing-the-Quran.png "quran")](http://belquran.com "quran")

