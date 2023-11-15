import time

user = 'Гвидо'
def say_hello(name):
    print('Привет')
    for letter in name:
        print(letter)
        time.sleep(0.5)

if __name__=="__main__":
    say_hello(user)


