for i in range (1,101):
    if i%3==0:
        if i%5 ==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    if i%5 == 0 and i%3 !=0:
        print("Buzz")
    if i%5 !=0 and i%3 !=0:
        print(i)
