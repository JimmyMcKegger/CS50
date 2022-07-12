# takes a time and outputs what meal

meal = ('breakfast', 'lunch', 'dinner')

def main():
  ans = ""
  time = input("What time is it? ")
  tod = convert(time)

  if 6.99 < tod < 7.99:
    ans = meal[0]
  elif 11.99 < tod < 13.01:
    ans = meal[1]
  elif 17.99 < tod < 18.99:
    ans = meal[2]

  if ans:
    print(ans + " time")

def convert(time):
    sep = time.index(':')
    hour = int(time[:sep])
    minute = float(time[sep + 1:]) / 60
    return hour + minute

if __name__ == "__main__":
  main()