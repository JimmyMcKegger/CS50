

def convert(str):
  # replace for ':)' or ':('
  a = str.replace(':)', '🙂')
  b = a.replace(':(', '🙁')
  # return converted text
  return b

def main():
  text = input()
  newText = convert(text)
  print(newText)



if __name__ == "__main__":
    main()