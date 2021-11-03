import pydantic
from typing import Optional
import pprint
import regex as re
import pyperclip
global char_repl_list
char_repl_list = {'l':'1','L':'1',
    'i':'1','!':'1','I':'1', 
    'S' : '$', 's': '$', 
    'a': '@', 'A' : '@',
     }
global new_list
new_list = []


class PassPhraseLengthError(Exception):
    """Check PassPhrase Length"""
    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)

class PassPhrase(pydantic.BaseModel):

    
    passphrase_input : Optional[str]

    @pydantic.validator('passphrase_input',allow_reuse=True,pre=True,)
    def check_passphrase_valid(cls,passphrase_input:str):
        print('started validator\n')
        try:
            passphrase_input_split = passphrase_input.split(' ')
            if len(passphrase_input_split) <= 2:
                raise PassPhraseLengthError(passphrase_input,f'Passphrase too short -> {passphrase_input, len(passphrase_input_split)} <-Please try again')
        except PassPhraseLengthError as lenError:
            """Logic can be here for passphrase to manipulate the value OR just dump the error for later review"""
            print('\nPassPhraseLength Error\n')
            return lenError
        passphrase_input_char_list = passphrase_input.split(" ")
        for index, word in enumerate(passphrase_input_char_list):
            if index == 2:
                try:
                        
                    new_word = list(word)
                    new_word[4] = new_word[4].upper()
                    edited_word = "".join(new_word) 

                    new_list.append(edited_word)
                except IndexError:
                    new_list.append(word.upper())
            else:
                new_list.append(word[0])
           
        for index, character in enumerate(new_list):
            if character in char_repl_list.keys():
                new_character = char_repl_list[character]
                new_list[index] = new_character
                print('character swapping')
        new_passphrase = "".join(new_list)
        print(f'aye we did the test\t\tCHANGED-> {passphrase_input}\tTO-> {new_passphrase}')
        pyperclip.copy(new_passphrase)
        return new_passphrase
    @staticmethod
    def get_Passphrase_from_User():
        user_input = input('Please Enter pass:\t')
        user_input = re.sub("\s+"," ",user_input)
        return user_input
class Config(PassPhrase):
    allow_mutation=True

def main():
    pass_phrase_object = PassPhrase()
    pass_phrase_object.passphrase_input=PassPhrase.get_Passphrase_from_User()
    pass_phrase_object.passphrase_input=PassPhrase.check_passphrase_valid(pass_phrase_object.passphrase_input)
    print(pass_phrase_object.__dict__)

if '__name__' == main():
    main()