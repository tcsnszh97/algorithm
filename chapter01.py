def LeftHanded1(string,n):
    alist = list(string)
    alist = alist[n:]+alist[:n]
    return ''.join(alist)

def LeftHanded2(string,n):
    return string[n:]+string[:n]

if __name__ == "__main__":
    s="ABCDEFG"
    n=3
    print(LeftHanded2(s,n))