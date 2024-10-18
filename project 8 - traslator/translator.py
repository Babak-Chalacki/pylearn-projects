import gtts

def read_from_file():
    global words_bank
    words_bank = []
    f = open('translate.txt', 'r', encoding='utf-8')
    temp = f.read().split('\n') 
    for i in range(0, len(temp) - 1, 2):
        my_words = {'en': temp[i], 'fa': temp[i + 1]}
        words_bank.append(my_words)
    f.close()
def translate_english_to_persian():
    user_text = input("text : ")
    sentences = user_text.split('.')
    output = ''
    
    for sentence in sentences:
        user_splits = sentence.strip().split(' ')
        for user_split in user_splits:
            found = False
            for word in words_bank:
                if user_split.lower() == word['en']: 
                    output += word['fa'] + ' '
                    found = True
                    break
            
            if not found:
                output += user_split + ' '  
        
        output += '. ' 
    
    print(output.strip()) 
    
    x = gtts.gTTS(output.strip(), lang="fa", slow=False) 
    x.save('voice.mp3')

def translate_persian_to_english():
    user_text = input("sentence : ")
    sentences = user_text.split('.')
    output = ''
    
    for sentence in sentences:
        user_splits = sentence.strip().split(' ')
        for user_split in user_splits:
            found = False
            for word in words_bank:
                if user_split.lower() == word['fa']: 
                    output += word['en'] + ' '
                    found = True
                    break
            
            if not found:
                output += user_split + ' '  
        
        output += '. ' 
    
    print(output.strip()) 
    
    x = gtts.gTTS(output.strip(), lang="en", slow=False) 
    x.save('voice_en.mp3')

def add_new_word():
    english_word = input("Enter the English word: ")
    persian_word = input("Enter the Persian translation: ")
    
    new_entry = {'en': english_word, 'fa': persian_word}
    words_bank.append(new_entry)
    
    f = open('translate.txt', 'a', encoding='utf-8')
    f.write(f"{english_word}\n{persian_word}\n")
    f.close()
    print("New word added successfully.")
 
def show_menu():
    print('1- English to Persian')
    print('2- Persian to English')
    print('3- Add new word')
    print('4- Exit')

read_from_file()
show_menu()
choice = int(input('Enter your choice: '))

while True:
    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        translate_persian_to_english()    
    elif choice == 3:
        add_new_word()    
    elif choice == 4:  
        exit(0)
    else:
        print('Invalid input')    