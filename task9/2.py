def extract_assignments_from_block(block):
    if 'auto' not in block:
        return None

    auto_part = block.split('auto', 1)[1]
    if ';' not in auto_part:
        return None

    assignment = auto_part.split(';', 1)[0]
    if '=' not in assignment:
        return None

    parts = assignment.split('=', 1)
    var_name = parts[0].strip()
    value = parts[1].strip()

    return var_name, value


def main(text):
    result = {}
    blocks = text.split('(')

    for block in blocks:
        assignment = extract_assignments_from_block(block)
        if assignment:
            var_name, value = assignment
            result[var_name] = value

    return result
