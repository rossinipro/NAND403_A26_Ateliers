import sys
import json

def main():
    if len(sys.argv) < 2:
       print("Usage: python main.py <json_file>")
       return

    json_file = sys.argv[1]

    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    print(data)


if __name__ == "__main__":
    main()

this_is_a_string = "je suis un string"
print(this_is_a_string)

def my_good_function():
    print("This is a good function!")

my_good_function()
print("Hello World!")
