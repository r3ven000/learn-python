VOCAB = {"п":1, "р":2, "и":3, "в":4, "е":5, "т":6, " ":7}

DATA = [
    ("привет", "привет"),   # вход → желаемый выход
    ("пока",   "пока"),
    ("впит",   "впит"),     # повторы букв — чтобы сеть не запомнила одно слово
    ("пвт",    "пвт"),
]

def word_to_codes(word):
    codes = []
    for i in word:
        codes.append(word[i])
    return codes

def codes_to_onehot(codes):
    for code in codes:
        vector = [0]
        vector[0]*7
        print(vector)

word_to_codes(VOCAB)
codes_to_onehot(codes)

