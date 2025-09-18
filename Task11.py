drink = input("WHAT DRINK DO YOU WANT TO ORDER? ")
if drink.islower():
    print("I DIDN'T HEAR YOUR ORDER!")
elif drink.isupper():
    many = int(input("HOW MANY? "))
    coffee_scoops = many * 4
    print(f'{many} {drink}S COMING RIGHT UP!')
    print(f'The barista needs {coffee_scoops} scoops of coffee in the coffee making machine')
else:
    print("Please enter the drink in all uppercase or all lowercase.")
