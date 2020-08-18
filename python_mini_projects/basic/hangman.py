import random
import re

class Word:

    # list of words to choose from
    words=['post','model','gate','manager','clouds','pottery','calender','helmet','dignity']

    def __init__(self):
        self.my_list=[]
        self.guess_word=random.sample(Word.words,len(Word.words))[0]        # get a random word from the list

    def get_word(self):
        for i in range(len(self.guess_word)):
            self.my_list.append('_')
        return self.my_list

    def guess_letter(self,letter):
        if letter:
            if letter in self.guess_word:
                if letter in self.my_list:
                    count=self.my_list.count(letter)        # checking for repeting letters

                    # get the index repeting letter 
                    index=[m.start() for m in re.finditer(letter,self.guess_word)][count]

                else:
                    index=self.guess_word.index(letter)
                
                self.my_list[index]=letter

            else:
                print(f'{letter} is not present in the word')

            return self.my_list
            
        else:
            print("Please enter a letter")

        

    def display(self):
        return ' '.join(self.my_list)




# driver code
man=Word()
man.get_word()
for i in range(len(man.guess_word)+2):
    result=man.display()
    print(result)
    if ''.join(result.split())==man.guess_word:
        print('Yay! You Won')
        break

    else:
        lt=input('Enter your guess: ')
        man.guess_letter(lt)
    
else:
    result=man.display()

    # checking if last letter completes the word
    if ''.join(result.split())==man.guess_word:
        print(man.guess_word)
        print('Yay! You Won')

    else:
        print('You Lose!')
        print(f'The Word was {man.guess_word}')






