# Evaluates a mathematecal expression and outputs a float
import operator

ops = {
  "+": operator.add,
  "-": operator.sub,
  "/": operator.truediv,
  "*": operator.mul
  }

def main():
  exp = input("Expression: ")
  x, y, z = exp.split()

  x = float(x)
  z = float(z)

  answer = ops[y](x, z)
  print(answer)

if __name__ == "__main__":
  main()