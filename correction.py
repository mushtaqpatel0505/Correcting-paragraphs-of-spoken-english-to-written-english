import spacy
from word2number import w2n
# Load the large English NLP model
nlp = spacy.load('en_core_web_sm')
    
texts=input()
docs =nlp(texts)
for entity in docs.ents:
    if entity.label_ =='MONEY':
        num=(w2n.word_to_num(entity.text))
        num_list=(entity.text).split()
        
sent = texts.split('.')
words=[]
for word in sent:
    words.append(word.split())      



abre= ["CM", "PM", "DM", "AM", "MIT","BBC","BC","FM","AD"]
for lst in words:
    for ab in abre:
        j=0
        while j+1<len(lst):   
            if str(lst[j]) + str(lst[j+1]) == ab:
                lst.remove(lst[j+1])
                lst.remove(lst[j])
                lst.append(ab)

            j+=1
print('abbrevation')
print('-----------Done-------------------------------------')


            
tuples={"single":1,"double":2,"triple":3}
for lst in words:
    for tup in tuples:
        i=0
        while i<len(lst):
            if str(lst[i]) in tuples.keys():
                lst.append((str(lst[i+1])*(tuples[str(lst[i])])))
                lst.remove(lst[i])
            i+=1
print('tuple correction')
print('-------------Done----------------------------------')

            
for lst in words:
    i=0
    while i < len(lst):
        
        if num_list[0]== lst[i] and num_list[len(num_list)-1]== lst[i + len(num_list)-1]:
            for val in num_list:
                lst.remove(val)
            lst.insert(i,("$"+str(num)))
            
        i+=1
print('text to number')
print('------------Done-----------------------------------')
print(words)      

new=[]
new1=''
for lst in words:
    new.append(' '.join(lst))
for sent in new:
    new1+= sent + '. '
print(new1)
