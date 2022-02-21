# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


# Function to check corresponding opening and closing brackets
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

  
# Function to find mismatch brackets
def find_mismatch(text):
    opening_brackets_stack = []
    
    # Iterate over string text
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next,i))

        if next in ")]}":
            # Process closing bracket
            if not opening_brackets_stack:
                return Bracket(next, i)
            # Check for corresponding opening and closing brackets
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return Bracket(next, i)
    # Return None if all brackets are corresponding
    if not opening_brackets_stack:
        return None
    else:
        return opening_brackets_stack[0]


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == None:
        print("Success")
    else:
        print(mismatch.position+1)


if __name__ == "__main__":
    main()
