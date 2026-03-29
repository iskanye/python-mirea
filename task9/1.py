def main(text):
    import re
    pattern = r'\(\s*auto\s+(\w+)\s*=\s*(\w+)\s*;\s*\)'
    matches = re.findall(pattern, text)

    result = {}
    for var_name, value in matches:
        result[var_name] = value
    return result
