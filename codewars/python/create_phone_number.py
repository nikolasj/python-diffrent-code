# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

def create_phone_number(n):
    # res = f"({n[0:3]}) {n[3:6]}-{n[6:]}"

    f_res = ""
    s_res = ""
    t_res = ""
    for i in range(len(n)):
        if i <= 2:
            f_res += str(n[i])
        elif i > 2 and i < 6:
            s_res += str(n[i])
        else:
            t_res += str(n[i])
    return f"({f_res}) {s_res}-{t_res}"




print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # "(123) 456-7890"

# def create_phone_number(n):
# 	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# def create_phone_number(n):
#     n = ''.join(map(str,n))
#     return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])