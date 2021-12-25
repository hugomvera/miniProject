# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f' {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Password generator functions')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/





def my_function():
    import string
    string.ascii_letters
    import random
    lower_upper_alphabet = string.ascii_letters
    list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
    random_letter1 = random.choice(string.ascii_letters)
    random_letter2 = random.choice(string.ascii_letters)
    random_letter3 = random.choice(string.ascii_letters)
    random_letter4 = random.choice(string.ascii_letters)
    random_letter5 = random.choice(string.ascii_letters)
    random_letter6 = random.choice(string.ascii_letters)
    n = random.randint(0, 9)
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    sp1 = random.choice(list)
    sp2 = random.choice(list)
    sp3 = random.choice(list)
    str1 =  random_letter1+sp1 +str(n2)+sp2+random_letter2+str(n1)+sp3+ random_letter3  +random_letter4+ random_letter5+random_letter6 + str(n)
    random_letter = random.choice(lower_upper_alphabet)
    set1 = set("!@#$%^&*()_+=?/>.<,:;}]{{|")
    return str1


my_function()



class loginCredentials:
  def __init__(self, userName, website):
    self.name = userName
    self.website = website
    self.password = my_function()



