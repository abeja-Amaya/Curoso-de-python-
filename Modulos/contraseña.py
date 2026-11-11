

def new_password(num1, words, num2):
    num = (num1 * 2) + 137
    words = words
    key = "xxx"
    num_2 = num2 * 10 - 1
    print("--------------------------------------------->")
    print(f"YOUR PASSWORD IS : {key}{num}{words}{num_2}")
    return