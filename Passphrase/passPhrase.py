import pydantic
from typing import Optional
import pprint
global char_repl_list
char_repl_list = {'l':'1','L':'1','i':'1','!':'1','I':'1'}


class PassPhrase(pydantic.BaseModel):

    
    passphrase_input : Optional[str]

    @pydantic.validator('passphrase_input',allow_reuse=True,pre=True,)
    def check_passphrase_valid(cls,passphrase_input:str):
        print('started validator\n')

        passphrase_input_char_list = list(passphrase_input)
        for index, character in enumerate(passphrase_input_char_list):
            if character in char_repl_list.keys() and passphrase_input_char_list.count(character) == passphrase_input.count(character):
                new_character = char_repl_list[character]
                passphrase_input_char_list[index] = new_character
                print('Character swapping')

        new_passphrase = "".join(passphrase_input_char_list)
        print(f'aye we did the test\t\tCHANGED-> {passphrase_input}\tTO-> {new_passphrase}')
        return new_passphrase
    @staticmethod
    def get_Passphrase_from_User():
        user_input = input('Please Enter pass:\t')
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