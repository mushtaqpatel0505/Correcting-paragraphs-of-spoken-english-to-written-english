def input_paragraph():
    texts=input("Enter the paragraph: ")
    return texts


import spacy
from word2number import w2n
def abbr_tup_money_corre(texts):
    
    abbreviation = ["ML","CM", "PM", "DM", "AM", "MIT","BBC","BC","FM","AD"]      # list of abbreviation
    tuples={"single":1,"double":2,"triple":3}                                     # list of tuples
    
    # Load the large English NLP model
    nlp = spacy.load('en_core_web_sm')
    
    docs =nlp(texts)
    for entity in docs.ents:
        if entity.label_ =='MONEY':
            num=(w2n.word_to_num(entity.text))     # converting word to number
            num_list=(entity.text).split()         # creating a list of words of number
            
            
    sent = texts.split('.')                        # splitting the paragraph into sentences
    words=[]
    for word in sent:
        words.append(word.split())                 # splitting each sentence to words
    
    
    for lst in words:
        for ab in abbreviation:
            j=0
            while j+1<len(lst):   
                if str(lst[j]) + str(lst[j+1]) == ab:     # checking for abbreviation 
                    lst.remove(lst[j+1])                  # removing individial alphabet
                    lst.remove(lst[j])                    
                    lst.insert(j, ab)                     # inserting corrected abbreviation

                j+=1
                
        for tup in tuples:
            i=0
            while i<len(lst):
                if str(lst[i]) in tuples.keys():          # checking for tuples
                    s = str(lst[i])
                    st=str(lst[i+1])
                    lst.insert(i,(st*(tuples[s])))        # inserting corrected tuples
                    lst.remove(s)                         # removing tuple word
                    lst.remove(st)                        # removing next word
                    
                i+=1        
        
        i=0
        while i < len(lst):
        
            if num_list[0]== lst[i] and num_list[len(num_list)-1]== lst[i + len(num_list)-1]:      # checking for word number
                for val in num_list:
                    lst.remove(val)                                                                # removing word number
                lst.insert(i,("$"+str(num)))                                                       # inserted number with sign
            
            i+=1

    words=words[:-1]
    new=[]
    new1=''
    for lst in words:
        new.append(' '.join(lst))
    for sent in new:                                            # joining sentences to paragraph
        new1+= sent + '. '
    return new1



def main():

    texts=input_paragraph()
    print('---------------------------------------------------')
    corrected_para = abbr_tup_money_corre(texts)
    print('Corrected paragraph')
    print(corrected_para)

if __name__ =="__main__":
    main()