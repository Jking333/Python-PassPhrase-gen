import pandas as pd
import numpy as np
import pydantic
from typing import Optional
import pprint


class PassPhrase(pydantic.BaseModel):
    passphrase_input : Optional[str]

    @pydantic.validator('passphrase_input',allow_reuse=True)
    def check_passphrase_valid(cls,passphrase_input:str):
        print('started validator')
        passphrase_input = passphrase_input.lower()
        print(f'aye we did the test\t\t {passphrase_input}')
        return passphrase_input
    @staticmethod
    def get_Passphrase_from_User():
        user_input = input('Please Enter pass:\t')
        return user_input


def main():
    pass_phrase_object = PassPhrase()
    pass_phrase_object.passphrase_input=PassPhrase.get_Passphrase_from_User()
    PassPhrase.check_passphrase_valid(pass_phrase_object.passphrase_input)
    print(pass_phrase_object.__dict__)

if '__name__' == main():
    main()