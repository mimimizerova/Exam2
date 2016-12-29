import urllib.request
import html
import re
import os
def download_page(pageUrl): 
    try:
        page = urllib.request.Request(pageUrl)
        with urllib.request.urlopen(page) as response:
            html = response.read().decode('utf-8')
    except:
        print('Error at', pageUrl)
    return html

def find_words (text):
    A = []
    reg1 = re.compile('С[А-Яа-я]*', flags=re.U | re.DOTALL)
    reg2 = re.compile ('\sс[а-я]*', flags=re.U | re.DOTALL)
    A1 = reg1.findall(text)
    A2 = reg2.findall(text)
    for word in A1:
        A.append(word)
    for word in A2:
        A.append(word[1:])
    return A

def find_verbs(text):
    V = []
    reg = re.compile('\n.*=V')
    words = reg.findall(text)
    for word in words:
        word = word[word.find('\n')+1:word.find('{')]
        V.append(word)
        
    return V

def find_wordform_for_table(text):
    W = []
    reg = re.compile('\n.*=[A-Z]+')
    words = reg.findall(text)
    for word in words:
        wordform = word[word.find('\n')+1:word.find('{')]
        W.append(wordform)
        
    return W
def find_lemma_for_table(text):
    L = []
    reg = re.compile('\n.*=[A-Z]+')
    words = reg.findall(text)
    for word in words:
        lemma = word[word.find('{')+1:word.find('=')]
        L.append(lemma)
        
    return L
def find_part_of_speech(text):
    P = []
    reg1 = re.compile('\n.*=[A-Z]+')
    reg2 = re.compile('[A-Z]+')
    words = reg1.findall(text)
    for word in words:
        Part = reg2.findall(word)
        P.append(Part[0])


    return P
    
    
txt = "C:\\Users\\Lenovo\\Desktop\\mystem.exe -cnid "
fl = r"C:\Users\Lenovo\Desktop\\Exam\\words.txt"
mystem_plain = txt + fl + " C:\\Users\\Lenovo\\Desktop\\Exam\\glossed-words.txt"
os.system(mystem_plain)

file = open('glossed-words.txt', 'r', encoding = 'utf-8')
s = file.read()
file.close()

    
    
    

print ('Сейчас на экран выведутся все слова с буквы "с":')
Arr1 = find_words(download_page(r'http://web-corpora.net/Test2_2016/short_story.html'))
for word in Arr1:
    print(word)

print('Сейчас на экран выведутся все глаголы с буквы "с":')
Arr2 = find_verbs(s)
for word in Arr2:
    print (word)
Wordforms = find_wordform_for_table(s)
Lemmas = find_lemma_for_table(s)
Parts = find_part_of_speech(s)

doc = open ('SQL.txt', 'a', encoding = 'utf-8')
for j in range (len(Wordforms)):
    string = 'INSERT INTO "table" (id, lemma, wordform, part_of_speech) VALUES (%d, "%s", "%s", "%s"); \n'%(j+1, Lemmas[j], Wordforms[j], Parts[j])
    doc.write(string)
doc.close()


