def transform_table(input_table):
    """Transform table by removing empty columns, splitting cells,
    transforming data, and transposing."""
    cleaned_data = remove_empty_columns(input_table)
    transformed_rows = transform_rows(cleaned_data)

    # Remove rows that contain only None values
    filtered_rows = [
        row for row in transformed_rows
        if any(cell is not None for cell in row)
    ]

    result_table = list(zip(*filtered_rows))
    return [list(row) for row in result_table]


def remove_empty_columns(data):
    """Remove columns that contain only None values."""
    transposed_data = list(zip(*data))
    non_empty_columns = [
        col for col in transposed_data
        if any(cell is not None for cell in col)
    ]
    return list(zip(*non_empty_columns))


def transform_rows(cleaned_data):
    transformed_rows = []
    for row in cleaned_data:
        new_row = []
        for cell in row:
            transformed_cell = transform_cell(cell)
            if isinstance(transformed_cell, list):
                new_row.extend(transformed_cell)
            else:
                new_row.append(transformed_cell)
        transformed_rows.append(new_row)
    return transformed_rows


def transform_cell(cell):
    """Transform a single cell based on its content."""
    if cell is None:
        return None
    if ';' in cell:
        return split_and_convert(cell)
    if '(' in cell and ')' in cell:
        return format_phone_number(cell)
    if '-' in cell and len(cell) == 10:
        return extract_year(cell)
    return cell


def split_and_convert(cell):
    """Split cell by ';' and convert values."""
    parts = cell.split(';')
    yes_no = 'да' if int(parts[0]) == 1 else 'нет'
    rounded_value = str(round(float(parts[1]), 1))
    return [yes_no, rounded_value]


def format_phone_number(cell):
    """Format phone number to standard format."""
    area_code = cell[1:4]
    first_part = cell[6:9]
    second_part = cell[10:12]
    third_part = cell[12:14]
    formatted = (
        f"({area_code}) {first_part}-"
        f"{second_part}-{third_part}"
    )
    return formatted


def extract_year(cell):
    """Extract year from date string."""
    return cell[:4]


# Пример 1
input_table_1 = [
    ['(647) 461-5192', '2000-07-21', None, '0;0.427'],
    ['(698) 897-5905', '2004-12-28', None, '1;0.127'],
    ['(855) 931-2356', '1999-08-11', None, '1;0.931']
]

print("Пример 1:")
result_1 = transform_table(input_table_1)
for row in result_1:
    print(row)

print("\nПример 2:")
input_table_2 = [
    ['(257) 341-2528', '2000-09-28', None, '1;0.506'],
    ['(207) 668-1394', '2004-12-26', None, '0;0.579'],
    ['(755) 081-0255', '2004-01-08', None, '1;0.019'],
    ['(714) 752-8440', '2004-09-18', None, '1;0.820']
]

result_2 = transform_table(input_table_2)
for row in result_2:
    print(row)

print("\nПример 3 (без заголовка):")
input_table_3 = [
    ['(647) 461-5192', '2000-07-21', None, '0;0.427'],
    ['(698) 897-5905', '2004-12-28', None, '1;0.127'],
    ['(855) 931-2356', '1999-08-11', None, '1;0.931']
]

result_3 = transform_table(input_table_3)
for row in result_3:
    print(row)
