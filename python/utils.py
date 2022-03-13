def convert_str_ascii_to_string(characters:str):
    chars = ""
    single_ascii = ""

    for char in characters:
        if char == ' ':
            chars += chr(int(single_ascii))
            single_ascii = ''
        else:
            single_ascii += char
    return chars