import const
from bd import get_connection, execute_query


def prepare_categoris(data):
    data_print = []
    categories = []
    for id_cat, name in data:
        categories.append(int(id_cat))
        data_print.append(f'{id_cat:3}  -{name:^15}')
    data_print = '\n'.join(data_print)
    return data_print, categories


def input_category(categories):
    while True:
        category = input('Выдерите категорию: ')
        if not category.isdigit() or int(category) not in categories:
            print('Ошибка, повторите ввод')
        else:
            break
    return category


def print_data(category, connection):
    query = const.QUERY_FILMS.format(category)
    data = execute_query(connection, query)
    film_ids = []
    if data is not None:
        print('-' * 150)
        print('   Название фильма   |  Год | Описание')
        print('-' * 150)
        index = 1
        for row in data:
            film_id = row[0]
            name = row[1]
            year = row[2]
            description = row[3]
            print(f'{index}. {name[:20]:>20} |{year:^6}| {description[:100]}')
            film_ids.append(film_id)
            index += 1
        return len(data), film_ids
    return 0, film_ids


def show_film_details(film_id, connection):
    query = const.QUERY_FILM_DETAILS.format(film_id)
    data = execute_query(connection, query)
    if data:
        print('-' * 100)
        print('Информация о фильме:')
        print(f'ID: {data[0][0]}')
        print(f'Название: {data[0][1]}')
        print(f'Описание: {data[0][2]}')
        print(f'Год выпуска: {data[0][3]}')

        actor_names = set()
        for actor_details in data:
            actor_names.add(f'{actor_details[-2]} {actor_details[-1]}')

        print('Актеры:', ', '.join(actor_names))
    else:
        print('Информация о фильме не найдена.')


def input_movie(max_index):
    while True:
        movie_choice = input('Выберите фильм (1-{}): '.format(max_index))
        if not movie_choice.isdigit() or not (1 <= int(movie_choice) <= max_index):
            print('Ошибка, повторите ввод')
        else:
            return int(movie_choice)


def main():
    connection = get_connection()
    if connection is None:
        return None

    data = execute_query(connection, const.QUERY_CATEGOTIES)
    data_print, categories = prepare_categoris(data)
    while True:
        print(data_print)
        category = input_category(categories)
        film_count, film_ids = print_data(category, connection)

        if film_count > 0:
            movie_choice_index = input_movie(film_count)
            movie_id = film_ids[movie_choice_index - 1]
            show_film_details(movie_id, connection)

        print('-' * 100)
        if input('Хотите выйти? (Д/Y): ').lower() in ('д', 'y'):
            print('До свидания\nРабота программы завершена')
            break

    connection.close()


main()
