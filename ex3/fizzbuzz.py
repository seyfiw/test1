def fizz_buzz(numbers):
    output = []
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            output.append("FizzBuzz")
        elif num % 3 == 0:
            output.append("Fizz")
        elif num % 5 == 0:
            output.append("Buzz")
        else:
            output.append(num)
    return output