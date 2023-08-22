#Ask the user for the input value
user_input = float(input("Enter your value: "))
#The first loop so that if an error happens it will be useful
while True:
    #Defines a function to convert to Celsius
    def conv_cels(x):
        return (x-32) * (5/9)

    #Defines a function to convert to Fahrenheit
    def conv_fahr(x):
        return (x* (9/5))+32

    #Asks the user for their desired conversion. Users have to enter 1 or 2
    selection = int(input("Do you want to convert it to 1.Celsius or 2. Fahrenheit: "))

    #This calls the above conv_cels function and they exit out of the loop
    if selection == 1:
        choice = "Celsius"
        result = round(conv_cels(user_input),2)
        break

    #This calls the above conv_fahr function and they exit out of the loop
    elif selection == 2:
        choice = "Fahrenheit"
        result = round(conv_fahr(user_input),2)
        break

    #If user input is not 1 or 2 this prints the message and runs the loop again
    else:
        print("Invalid input")
        continue
#Final output message
print("Your value was: ",user_input,". You wanted to convert it to: ",choice,". The result is:",result,sep="")
