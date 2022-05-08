import json
from difflib import get_close_matches
x=open('data.json')
data=x.read()
res=json.loads(data)
while True:
        try:
                q=input("Enter the word to search for meaning ")
                if (q.lower() in res.keys()):
                        mn=res.get(q.lower())
                        #print(mn)
                        
                elif (q.title() in res.keys()):
                        mn=res.get(q.title())
                        
                elif (q.upper() in res.keys()):
                        mn=res.get(q.upper)
                        
                elif (len(get_close_matches(q,res.keys()))>0):
                        mn=get_close_matches(q,res.keys())
                        print("Did't find any exact match \nSimilar words found are ")
                                
                else:
                        print('Word Not Found')

#--Displaying----------------------------------------------------------------
                        
                if type(mn)==list:
                        num=1
                        for i in mn:
                                print('%d.%s'%(num,i))
                                num+=1
                del mn #workes 
                #mn.clear() #Doesn't work if we use this 
        except:
                print('Invalid Input')

#--Next_Word-----------------------------------------------------------------
                print('-'*50)
        
        flag=0      
        while True:
                br=input('Wants to search for another Word ? (y/n)')
                if br=='n':
                        flag=1
                        break
                elif br=='y':
                        break
                else:
                        print("Enter 'y' or 'n' only....!!!")
                        #raise ValueError
        
        if flag==1:
                break

        
        


