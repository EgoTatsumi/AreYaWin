import random, os
flags = [i[:-4].capitalize()for i in os.listdir('Images/flags')]
print(flags)


def take_flag():
    return random.choice(flags)


def flag_game(corans):
    correct = corans
    flags.remove(correct)
    ans1, ans2, ans3 = random.choices(flags, k=3)
    answers = [correct, ans1, ans2, ans3]
    random.shuffle(answers)
    while len(set(answers)) != 4:
        ns1, ans2, ans3 = random.choices(flags, k=3)
        answers = [correct, ans1, ans2, ans3]
        random.shuffle(answers)
    vars = dict()
    for i in range(1, 5):
        vars[i] = answers[i-1]
    return vars

