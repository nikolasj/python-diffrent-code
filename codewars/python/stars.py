# https://www.codewars.com/kata/5888cba35194f7f5a800008b/train/python

def asterisc_it(n):
    if isinstance(n, list):
        n = "".join([str(i) for i in n])
    else:
        n = str(n)

    result = ""
    for i in range(len(n)):
        if i < len(n) - 1:
            if int(n[i]) % 2 == 0 and int(n[i+1]) % 2 == 0:
                result += "{}*".format(n[i])
            else:
                result += n[i]
        else:
            result += n[i]

    return result


# print(asterisc_it(708))
# print(asterisc_it([1, 4, 64, 68, 67, 23, 1]))
#
# import re
#
# def asterisc_it(s):
#     if   isinstance(s,int):  s=str(s)
#     elif isinstance(s,list): s=''.join(map(str,s))
#     return re.sub(r'(?<=[02468])(?=[02468])', '*', s)

# def asterisc_it(n):
#     if type(n) == list: n = "".join(str(i) for i in n)
#     if type(n) == int : n = str(n)
#     return "".join([a+"*" if int(a)%2==0 and int(b)%2 == 0 else a for a,b in zip(n,n[1:])]) + n[-1]