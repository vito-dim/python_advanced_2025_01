def concatenate(*args, **kwargs):
    text = ''.join(args)
    for match, replacement in kwargs.items():
        text = text.replace(match, replacement)
    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
