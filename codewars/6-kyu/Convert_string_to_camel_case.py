def to_camel_case(text: str) -> str:
    output = ""

    i = 0
    while i < len(text):
        if text[i] == "-" or text[i] == "_":
            output += text[i + 1].upper()
            i += 2
        else:
            output += text[i]
            i += 1

    return output
