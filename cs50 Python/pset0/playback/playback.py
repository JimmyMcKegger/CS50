# replaces spaces with ellipses

text = input("Enter your message: ")

arr = text.split()

print('...'.join(arr))