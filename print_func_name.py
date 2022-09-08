def print_name(func, *args):
    print("Function name and attributes:")
    print(func.__name__, *args, sep='\n')
    print()


def open_browser(browser_name):
    print_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_name(find_registration_button_on_login_page, page_url, button_text)


open_browser('Microsoft Edge')
go_to_companyname_homepage('https://ya.ru/')
find_registration_button_on_login_page('https://ya.ru/', 'Голосовой поиск')
