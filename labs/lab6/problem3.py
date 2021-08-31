def main() -> None:
    fread = input('Enter filename to append:')
    with open(fread, 'r+') as fr:
        data = fr.read()
        fr.write('\ncatto')
    print(data)


if __name__ == '__main__':
    main()
