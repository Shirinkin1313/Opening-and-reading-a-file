

cook_book = []
def open_data(file_name):
    with open(file_name, encoding='utf8') as file:
        for line in file:
            cook_book.append(file.readline().strip())
            print(cook_book)

open_data('recipe')