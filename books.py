#!/usr/bin/env python3
import requests
import sys
import os
import json
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mkdir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def name_to_pdf(name, dir):
    return '{}/{}.pdf'.format(dir, name.replace('/', '-'))

def downloader(url, name):
    response = requests.get(url)
    with open(name, 'wb') as file:
        file.write(response.content)

def print_choices(items):
    for i in range(len(items)):
        print('{}. {}'.format(i + 1, items[i]))

def validate_choice(total, choice):
    return 0 <= choice < total

def choose(prompt, items):
    choices = []
    while True:
        clear()
        print(prompt)
        print_choices(items)
        selected = ', '.join([items[i] for i in choices])
        print('Selected: {}'.format(selected if len(choices) > 0 else None))
        choice = input('Enter a number, "all" for all categories or q to return [q]: ')
        if choice == 'q' or choice == '':
            break
        elif choice == 'all':
            return list(range(len(items)))
        choice = int(choice) - 1
        if validate_choice(len(items), choice):
            if choice not in choices:
                choices.append(choice)
            else:
                choices.remove(choice)
    clear()
    return choices

def main(filename, path):
    mkdir(path)
    with open(filename) as file:
        _json = json.loads(''.join(file.readlines()).replace('\n',''))
    
    categories = list(_json.keys())
    categories_prompt = ['{} ({} books)'.format(item, len(_json[item])) for item in categories]
    choices = choose('Select a category: ', categories_prompt)
    choices = [categories[i] for i in choices]

    total_books_chosen = 0
    for category in choices:
        total_books_chosen += len(_json[category])

    current_book_n = 1
    for category in choices:
        print('{} Getting books from {} {}'.format('*'*10, category, '*'*10))
        subPath = '{}/{}'.format(path, category)
        mkdir(subPath)
        books = next(os.walk(subPath))[2]

        for book in _json[category]:
            perc_progress = current_book_n / total_books_chosen

            if book['title'].replace('/', '-') + '.pdf' not in books:
                print('[{:.0%}]-> Getting book: {}'.format(perc_progress, book['title']))
                filename = name_to_pdf(book['title'], subPath)
                downloader(book['url'], filename)
            else:
                print('[{:.0%}]-> Already here: {}'.format(perc_progress, book['title']))
            
            current_book_n += 1

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage:')
        print('{} <json with books data> <output folder>'.format(sys.argv[0]))
    else:
        main(sys.argv[1], sys.argv[2])

