# confirms the answer

def main():
  answer = input("What is the Answer to the Great Questions of Life, the Universe, and Everything? ").strip()
  if answer == '42':
    print("Yes")
  elif answer.lower() == 'forty-two':
    print("Yes")
  elif answer.lower() == 'forty two':
    print("Yes")
  else:
    print("No")

if __name__ == "__main__":
  main()