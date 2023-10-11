# TODO Найдите количество книг, которое можно разместить на дискете

memory_mb = 1.44
memory_for_sym = 4
book = {
    "pages": 100,
    "lines": 50,
    "symbols": 25
}

memory_b = memory_mb * 1024 * 1024
book_total_sym = book["pages"] * book["lines"] * book["symbols"]
memory_book = book_total_sym * 4
number_of_book = memory_b // memory_book

print("Количество книг, помещающихся на дискету:", int(number_of_book))
