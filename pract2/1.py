# 8.3
import sys


def convert_quotes(text):
    result = []
    i = 0
    code_block = False
    inline_code = False
    quote = False

    while i < len(text):
        # Проверка на блоки кода
        if i + 2 < len(text) and text[i : i + 3] == "```":
            code_block = not code_block
            result.append("```")
            i += 3
            continue

        # Проверка на инлайн код
        if text[i] == "`" and not code_block:
            inline_code = not inline_code
            result.append("`")
            i += 1
            continue

        # Обработка кавычек только вне блоков кода
        if text[i] == '"' and not code_block and not inline_code:
            if quote:
                result.append("»")
            else:
                result.append("«")
            quote = not quote
            i += 1
            continue

        result.append(text[i])
        i += 1

    return "".join(result)


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Ошибка: файл '{filename}' не найден", file=sys.stderr)
            sys.exit(1)
    else:
        # Читаем из стандартного ввода
        text = sys.stdin.read()

    # Преобразуем и выводим результат
    converted = convert_quotes(text)
    print(converted, end="")


if __name__ == "__main__":
    main()
