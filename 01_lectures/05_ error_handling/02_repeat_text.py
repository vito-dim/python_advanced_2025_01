text = input()

try:
    times = int(input())
    repeated_text = text * times
    print(repeated_text)
except ValueError:
    print("Variable times must be an integer")
# else:
#     print("from else")
# finally:
#     print("from finally")


# IMPORTANT finally in FUNCTION, overrides the RETURN!!!! Regarding except and else, depends how function is built