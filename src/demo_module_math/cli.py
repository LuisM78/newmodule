import argparse
from demo_module_math.operations import add, multiply

def main():
    parser = argparse.ArgumentParser(description="Math CLI tool")
    parser.add_argument("operation", choices=["add", "multiply"])
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    args = parser.parse_args()

    if args.operation == "add":
        print(add(args.a, args.b))
    else:
        print(multiply(args.a, args.b))

if __name__ == "__main__":
    main()
