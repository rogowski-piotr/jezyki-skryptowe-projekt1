def function(characters='', exclude_characters=None):
    exclude_characters = [ ord(char) for char in exclude_characters ] if exclude_characters else [ ord(char) for char in ' \t\n\r\x0b\x0c' ]
    cut_head = 0
    cut_tail = 0

    for index in range(len(characters)):
        if ord(characters[index]) in exclude_characters:
            cut_head += 1
        else: break

    for index in range(len(characters) - 1, -1, -1):
        if ord(characters[index]) in exclude_characters:
            cut_tail += 1
        else: break

    return characters[cut_head : len(characters) - cut_tail]