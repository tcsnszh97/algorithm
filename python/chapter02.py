def comparestring1(longstring,shortstring):
    for i in shortstring:
        if i in longstring:
            continue
        else:
            print("string2 no in string1")
            return False
    print("string2 in string1")

if __name__ == "__main__":
    string1 = "ABCDEFG"
    string2 = "DEFG"
    comparestring1(string1,string2)