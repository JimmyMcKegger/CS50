
def main():
  myList = {}
  while True:
    try:
      item = input().upper()
    except EOFError:
      print()
      sorted_list = dict(sorted(myList.items()))
      for k, v in sorted_list.items():
        print(f"{v} {k}")
      exit()
    if item in myList:
      myList[item] += 1
    else:
      myList[item] = 1

if __name__ == "__main__":
  main()