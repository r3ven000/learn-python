<<<<<<< HEAD
import numpy
#step 1

VOCAB = {"п":1, "р":2, "и":3, "в":4, "е":5, "т":6, " ":7} #dict

DATA = [
    ("привет", "привет"),   # вход → input
=======
VOCAB = {"п":1, "р":2, "и":3, "в":4, "е":5, "т":6, " ":7}

DATA = [
    ("привет", "привет"),   # вход → желаемый выход
>>>>>>> e4a6425 (delete old practice)
    ("пока",   "пока"),
    ("впит",   "впит"),     # повторы букв — чтобы сеть не запомнила одно слово
    ("пвт",    "пвт"),
]

<<<<<<< HEAD
def word_to_codes(word): #translate word to numbers(codes)
=======
def word_to_codes(word):
>>>>>>> e4a6425 (delete old practice)
    codes = []
    for i in word:
        codes.append(VOCAB[i])
    return codes

<<<<<<< HEAD
def codes_to_onehot(codes): #matrix
=======
def codes_to_onehot(codes):
>>>>>>> e4a6425 (delete old practice)
    result = []
    for code in codes:
        vector = [0] * 7
        vector[code - 1] = 1
        result.append(vector)
    return result

<<<<<<< HEAD
#step 2

N = 10
W1 = np.random.uniform(-0.5, 0.5, (7, N))
b1 = np.random.uniform(-0.5, 0.5, (1, N))
W2 = np.random.uniform(-0.5, 0.5, (N, 7))
b2 = np.random.uniform(-0.5, 0.5, (1, 7))
=======
>>>>>>> e4a6425 (delete old practice)

