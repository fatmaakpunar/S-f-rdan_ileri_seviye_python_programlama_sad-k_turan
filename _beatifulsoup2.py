# -*- coding: utf-8 -*-
"""_beatifulsoup2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bfM-G03dkJno6BMZuY2yTIUbd-6PkiP1
"""

html_doc ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk web sayfam değil :| </title>
</head>
<body>
<h1 id = "header">
        FATMA AKPUNAR
    </h1>
    <div class="grup1">
        <h2>
        Programlama
        </h2>

        <ul>
            <li>MENÜ 1</li>
            <li>MENÜ 2</li>
            <li>MENÜ 3</li>
        </ul>

   </div>
   <div class="grup2">
    <h2>
       Modüller
    </h2>
    <ul>
        <li>MENÜ 1</li>
        <li>MENÜ 2</li>
        <li>MENÜ 3</li>
    </ul>
   </div>
  <div class="grup3">
    <h2>
       Django
    </h2>
    <ul>
        <li>MENÜ 1</li>
        <li>MENÜ 2</li>
        <li>MENÜ 3</li>
    </ul>
    </div>
    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
"""
from bs4 import BeautifulSoup

soup =BeautifulSoup(html_doc, 'html.parser')
result = soup.prettify() #belgeyi daha okunabilir bir şekilde düzenleyerek dize olarak döndürür
result = soup.title #title içeriği gelir
result = soup.head
result = soup.body

result = soup.title.name #title ismi gelir
result = soup.titleistring #içindeki string bilgisi gelir

result = soup.h2 #ilk h2'yi getirir

result = soup.find_all('h2') #bütün h2'leri getiri
result = soup.find_all('h2')[0] #ilk h2'yi getirir

#result = soup.find_all('div')[1].ul.find_all('li') #bu şekilde de kullanılabilir

result = soup.findChildren('div') #div'in altındaki tüm etiketleri getirir

result = soup.div.findNextSibling().findNextSibling() # findNextSibling() bir sonraki div e geçer
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling() #findPreviousSibling bir önceki div e geçer

result = soup.find_all('a')
for link in result:
  print(link.get('href')) #get özelliği ile a etiketinden sadece linleri alabiliriz.