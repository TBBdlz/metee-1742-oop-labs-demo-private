def main() -> None:
    my_name: str = 'Metee'
    my_id: str = '633040174-2'
    my_province: str = 'Loei'

    print(f'Welcome to the program prob2.py by {my_name}'
          f', {my_id} who has hometown as {my_province}')

    trip_dict: dict = dict()
    while True:
        try:
            trip_year = int(input('Enter a trip year (e.g.2021):'))
            place_visited = input('Enter the places you visit:')
            places_list = place_visited.split(', ')
            if trip_year < 2000 or trip_year > 2021:
                raise ValueError
            if trip_year in trip_dict:
                trip_dict.update({trip_year: places_list})
            else:  # trip year is not in dictionary
                places_list.append(my_province)
                trip_dict[trip_year] = places_list
        except ValueError:
            print('A valid trip year is an integer in the range [2000, 2021]')
            break
    print(trip_dict)
    search_text = input('Enter place for which you want to search:')
    found = False
    for year in trip_dict:
        for place in trip_dict[year]:
            if place == search_text:
                found = True
                break


if __name__ == '__main__':
    main()
