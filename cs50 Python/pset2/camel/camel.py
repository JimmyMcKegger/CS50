# Converts camel case to snake case

def main():
  camel = input('camelCase: ')
  snake = []
  for char in camel:
    if char.isupper():
      snake.append('_')
      snake.append(char.lower())
    else:
      snake.append(char)

  print(''.join(snake))

if __name__ == "__main__":
  main()