
word = input()
for i in range(int(word[0])):
    if len(word) > 10:
        c_len = len(word[1:-1])
        print(f"{word[0]}{c_len}{word[-1]}")
    elif len(word)>1:
        print(word)


# num = int(input())
# for i in range(num):
#     st = input()
#     if len(st) > 10:
#         print(f"{st[0]}{len(st)-2}{st[-1]}")
#     else :
#         print(st)