import requests
import sys

def main():
  # Check for command line arg
  if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
  # Chek if it's a number
  try:
    num = float(sys.argv[1])
  except ValueError:
    sys.exit("Command-line argument is not a number")
  # request for the price
  try:
      quote = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
      # print(json.dumps(quote.json(), indent=2))
  except requests.RequestException:
      raise

  price = float(quote.json()['bpi']['USD']['rate'].replace(",",""))
  amount = num * price

  # output price
  print(f"${amount:,.4f}")

if __name__ == "__main__":
  main()