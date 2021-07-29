taekwondo_olympics2020_w49k = {
    'Gold': {'Thailand'},
    'Silver': {'Spain'},
    'Bronze': {'Israel', 'Serbia'}
}


def print_medal() -> None:
    global taekwondo_olympics2020_w49k
    print('The list of medals in Taekwondo Olympics 2020 women 49 kilograms:')
    for medal_type in taekwondo_olympics2020_w49k:
        for country in taekwondo_olympics2020_w49k[medal_type]:
            print(f'{country} received {medal_type} medal')
    print('The dictionary of medals is', taekwondo_olympics2020_w49k)


if __name__ == '__main__':
    print_medal()
