def words_to_number(words: str) -> int:
    word_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }
    multipliers = {"hundred": 100, "thousand": 1000, "million": 1000000}

    words = words.lower().replace("-", " ")
    tokens = words.split()
    current = 0
    total = 0

    for token in tokens:
        if token == "and":
            continue
        if token in word_map:
            current += word_map[token]
        elif token in multipliers:
            current *= multipliers[token]
            if token != "hundred":
                total += current
                current = 0

    return total + current
