def main() -> None:
    fread = input('Enter filename to append:')
    with open(fread, 'r+') as fr:
        data = fr.read()
    append_text = input('Enter text to append:')
    file_wr = input('Enter file name to write:')
    with open(file_wr, 'w') as fw:
        fw.write(data + '\n' + append_text)
    # read content in new file
    with open(file_wr, 'r') as fnew_r:
        print(fnew_r.read())


if __name__ == '__main__':
    main()
