command_data = input()
final_price = 0
price_after_tax = 0
while True:
    if command_data == 'special' or command_data == 'regular':
        break
    price = float(command_data)
    if price < 0:
        print(f"Invalid price!")
        command_data = input()
        continue
    final_price += price
    command_data = input()
if final_price == 0:
    print('Invalid order!')
else:
    taxes = 0.20 * final_price
    price_after_tax += taxes + final_price
    if command_data == 'special':
        price_after_tax -= price_after_tax * 0.10
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {final_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print(f'-----------')
    print(f"Total price: {price_after_tax:.2f}$")
