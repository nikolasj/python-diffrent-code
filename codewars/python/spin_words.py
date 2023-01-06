# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python


def spin_words(sentence):
    res = []
    for i in sentence.split():
        if len(i) >= 5:
            res.append(i[::-1])
        else:
            res.append(i)
    return " ".join(i for i in res)


print(spin_words("Hey fellow warriors"))

# def spin_words(sentence):
#     # Your code goes here
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])