def wrapper(f):
    def fun(l):

        # complete the function
        print("Inside fun")
        prefix = "+91"
        l2 = []
        for number in l:
            sec_part = number[len(number) - 5 : len(number)]
            first_part = number[len(number) - 10 : len(number) - 5]
            new_s = prefix + " " + first_part + " " + sec_part
            l2.append(new_s)
        print(l2)
        return f

    return fun


@wrapper
def sort_phone(l):
    print("Inside Sort")
    print(*sorted(l), sep="\n")


if __name__ == "__main__":
    l = [input() for _ in range(int(input()))]
    print("inside Main")
    sort_phone(l)
