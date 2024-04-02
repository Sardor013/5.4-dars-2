
a = int(input())
c = 'H'

for i in range(a):
    print((c*i).rjust(a-1)+c+(c*i).ljust(a-1))

for i in range(a+1):
    print((c*a).center(a*2)+(c*a).center(a*6))

for i in range((a+1)//2):
    print((c*a*5).center(a*6))

for i in range(a+1):
    print((c*a).center(a*2)+(c*a).center(a*6))

for i in range(a):
    print(((c*(a-i-1)).rjust(a)+c+(c*(a-i-1)).ljust(a)).rjust(a*6))




import textwrap


def wrap(string, max_width):
    result = ""
    for i in range(0, len(string), max_width):
        result += string[i:i + max_width] + "\n"

    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)



