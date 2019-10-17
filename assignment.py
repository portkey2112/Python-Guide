# https://stackoverflow.com/questions/4869770/why-does-python-assignment-not-return-a-value
# Python (before 3.8) DOES NOT return anything from an assignment
# ex - in C/C++/Java
#       if (x = y) { .. }
#       means that value of y is assigned to x and the assigned value is returned.
# however, this does not happen in Python before v3.8
#
# WHY IS THIS IMPORTANT ?
# This is a kind of short cut used by many programmers, who prefer using C/C++/Java
# There are many who feel that having assignments be expressions,
# especially in languages like Python where any value is allowable in a condition (not just values of some boolean type).
# This is error-prone. Presumably Guido is/was among those who feel that way.
#
# This was till Python v3.8 got released.
# https://docs.python.org/3/whatsnew/3.8.html
# Assignment expression -
# There is new syntax := that assigns values to variables as part of a larger expression.
# It is affectionately known as “the walrus operator” due to its resemblance to the eyes and tusks of a walrus.
# for ex -
#       if (n := len(a)) > 10:
#           print(f"List is too long ({n} elements, expected <= 10)")
#


if __name__ == '__main__':
    x = int(input("Enter value of x -"))
    y = int(input("Enter value of y -"))
    if x == y:
        print("X and Y are same")
        # works fine

    if x = y:
        print("Value of Y is assigned to X")
        #     if x = y:
        #          ^
        # SyntaxError: invalid syntax

    if (x = y) > 10:
        print("Value of Y is assigned to X and returned")
        #     if (x = y) > 10:
        #          ^
        # SyntaxError: invalid syntax
