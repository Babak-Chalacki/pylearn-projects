
def read_from_file():
    global words_bank
    words_bank = []
    f = open('translate.txt','r')
    temp = f.read().split('\n') 
    for i in range(0,len(temp),2):
        my_words = {'en':temp[i],'fa':temp[i+1]}
        words_bank.append(my_words)

    f.close()


def translate_english_to_persian(): 
    user_text = input("text : ")
    user_splits = user_text.split(' ')
    output = ''
    for user_split in user_splits:
        for word in words_bank:
            if user_split == word['en']:
                output = output + word['fa'] + ' '
                print(word['fa'])
                break
        
        else:
            output = output + user_split + ' '
                
    print(output)
    
def show_menu():
    print('1- en to pa')
    print('2- pa to en')
    print('3- add new word')
    print('4- exit')

read_from_file()
show_menu()
choice = int(input('enter your choice'))

while True:
    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        ...    
    elif choice == 3:
        ...    
    elif choice == 4:  
        exit(0)
    else:
        print('invalid input')    