import argparse

def predict(x):
    return x * 2

parser = argparse.ArgumentParser()
parser.add_argument("value", type=int)

args = parser.parse_args()

print("Prediction:", predict(args.value))