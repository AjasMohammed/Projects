from tabulate import tabulate

print("Enter The Prices: ")

total_sum = 0
data = []
while True:
    try:
        product = input("Product: ")
        if product == "":
            raise ValueError

        price = int(input('Price: '))

    except ValueError:
        data.append(["---------", "-------"])
        data.append(['TOTAL', total_sum])  # shows total in the end of table
        print("\nDo You want to view the Receipt? Y/N")
        user_inp = input(">>> ").lower()

        if user_inp == "y":
            headers = ['Product', 'Price']  # title of table
            print()
            print(tabulate(data, headers=headers))  # creates table
        break
    data.append([product.title(), price])
    total_sum += price

    print(f'\nTotal : {total_sum}\n')

print(f"\nYour Total Bill Payment is - {total_sum}.Rs \n....Thanks for shopping with us....\n")
