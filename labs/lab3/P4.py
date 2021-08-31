"""
Convert string into list and vowels list
then convert all element in vowels to uppercase
author: Metee Yingyongwatthanakit
date: 5 August 2021
"""


def to_upper(s) -> str:
    return str(s).upper()


def main() -> None:
    input_str = input('Enter a string:')
    char_list = [char for char in input_str]
    print('Characters in the string are', char_list)
    vowels_list = [vowel for vowel in char_list if vowel in 'aeiouAEIOU']
    vowels_list = list(map(to_upper, vowels_list))
    print(f'The entered string is {input_str} and the result of convert a vowel to upper case is\n{vowels_list}')


if __name__ == '__main__':
    main()
