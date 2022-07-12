# Removes vowels from a message
def main():
  text = input("Input: ").strip()
  twttr = shorten(text)
  print("Output: " + twttr)

def shorten(word):
  # vars
  vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
  tweet = []
  # make a new string
  for char in word:
    if char in vowels:
      continue
    else:
      tweet.append(char)
  return "".join(tweet)

if __name__ == "__main__":
  main()