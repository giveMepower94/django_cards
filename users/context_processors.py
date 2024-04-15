info = {
    'users_info': 100500,
    'cards_count': 200600,
    'menu': [
        {'title': 'Главная',
         'url_name': 'index'},
        {'title': 'О проекте',
         'url_name': 'about'},
        {'title': 'Каталог',
         'url_name': 'catalog'}
    ],
}


def get_menu(request):
    return info