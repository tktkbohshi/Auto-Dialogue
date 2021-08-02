import numpy as np

def loadCanditates(path=""):
    user = []
    system = []
    data = np.load(path, allow_pickle=True)

    for dialogue in data:
        for n, sentence in enumerate(dialogue):
            if n % 2 == 0:
                user.append(sentence)
            else:
                system.append(sentence)

    return user, system
