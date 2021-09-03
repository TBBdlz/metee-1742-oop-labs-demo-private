def main() -> None:
    num_tuple = (2, 123.4567, 10000, 12345.67)
    print('file_00{:d}: {}, {:.2e}, {:.2e}'.format(
        num_tuple[0], num_tuple[1], num_tuple[2], num_tuple[3]))


if __name__ == '__main__':
    main()
