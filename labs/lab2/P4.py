def main() -> None:
    vowels_list = []
    sentence = input('Enter string input:')
    for char in sentence:
        if char in "aeiouAEIOU":
            vowels_list.append(char)
    print(f'Vowels in {sentence} are {vowels_list}')


if __name__ == '__main__':
    main()
