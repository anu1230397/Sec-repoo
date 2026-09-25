import argparse

parser = argparse.ArgumentParser(description="Simple calculator")

parser.add_argument("a", type=int)
parser.add_argument("b", type=int)

args = parser.parse_args()

print("Sum =", args.a + args.b)