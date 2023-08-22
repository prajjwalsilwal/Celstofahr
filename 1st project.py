user_input = float(input("Enter your value: "))
while True:
    def conv_cels(x):
        return (x-32) * (5/9)

    def conv_fahr(x):
        return (x* (9/5))+32
    selection = int(input("Do you want to convert it to 1.Celsius or 2. Fahrenheit: "))

    if selection == 1:
        choice = "Celsius"
        result = round(conv_cels(user_input),2)
        break

    elif selection == 2:
        choice = "Fahrenheit"
        result = round(conv_fahr(user_input),2)
        break

    else:
        print("Invalid input")
        continue

print("Your value was: ",user_input,". You wanted to convert it to: ",choice,". The result is:",result,sep="")