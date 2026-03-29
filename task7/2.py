def main(x):
    # Словари для преобразования входных значений в индексы
    lang_to_idx = {'COBOL': 0, 'SQL': 1, 'NL': 2}
    year_to_idx = {2017: 0, 2007: 1, 1988: 2}

    # Результаты для x[2] == 1993: [lang][year]
    results_1993 = {
        0: {0: 0, 1: 1, 2: 2},   # COBOL
        1: {0: 3, 1: 3, 2: 3},   # SQL
        2: {0: 4, 1: 5, 2: 6},   # NL
    }

    # Результаты для x[2] == 2008: [year][lang]
    results_2008 = {
        0: {0: 7, 1: 8, 2: 9},     # 2017
        1: {0: 10, 1: 10, 2: 10},  # 2007
        2: {0: 11, 1: 11, 2: 11},  # 1988
    }

    # Выбор таблицы результатов по x[2]
    tables = {1993: results_1993, 2008: results_2008}
    keys = {1993: (lang_to_idx[x[0]], year_to_idx[x[1]]),
            2008: (year_to_idx[x[1]], lang_to_idx[x[0]])}

    table = tables[x[2]]
    key1, key2 = keys[x[2]]
    return table[key1][key2]


# Примеры
if __name__ == "__main__":
    print(main(['SQL', 2017, 1993, 1982]))   # 3
    print(main(['SQL', 1988, 2008, 1982]))   # 11
    print(main(['COBOL', 2007, 1993, 1982])) # 1
    print(main(['COBOL', 2007, 2008, 1970])) # 10
    print(main(['NL', 1988, 1993, 1970]))    # 6