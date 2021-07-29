olympic2020_str = "Badminton: Thailand vs. Great Britain," \
                  "Table Tennis: Thailand vs. Japan"


def main() -> None:
    global olympic2020_str
    sport_list = olympic2020_str.split(',')
    print('For some Olympics 2020 games of Thai athletes:')
    for sport_data in sport_list:
        text_pair = sport_data.split(':')
        print(f'For {text_pair[0]}, the game is between {text_pair[1]}')


if __name__ == '__main__':
    main()
