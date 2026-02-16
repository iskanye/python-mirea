# 8.3
import sys


def convert_quotes(text):
    result = []
    i = 0
    in_code_block = False
    in_inline_code = False
    quote_open = False

    while i < len(text):
        # Проверка на блоки кода
        if i + 2 < len(text) and text[i : i + 3] == "```":
            in_code_block = not in_code_block
            result.append("```")
            i += 3
            continue

        # Проверка на инлайн код
        if text[i] == "`" and not in_code_block:
            in_inline_code = not in_inline_code
            result.append("`")
            i += 1
            continue

        # Обработка кавычек только вне блоков кода
        if text[i] == '"' and not in_code_block and not in_inline_code:
            if quote_open:
                result.append("»")
            else:
                result.append("«")
            quote_open = not quote_open
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
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Читаем из стандартного ввода
        text = sys.stdin.read()

    # Преобразуем и выводим результат
    converted = convert_quotes(text)
    print(converted, end="")


if __name__ == "__main__":
    main()
