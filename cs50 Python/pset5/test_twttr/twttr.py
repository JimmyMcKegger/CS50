# Removes vowels from a message
def main():
  text = input('Input: ')
  twttr = shorten(text)
  print('Output: ' + twttr)

def shorten(word):
  # vars
  vowels = ('a', 'e', 'i', 'o', 'u')
  tweet = ''
  # make a new string
  for char in word:
    if char.lower() in vowels:
      continue
    else:
      tweet += char
  return tweet

if __name__ == '__main__':
  main()