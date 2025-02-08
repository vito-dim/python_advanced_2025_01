# def list_roman_emperors(*args, **kwargs):
#     result = []
#     success_emperors = {}
#     failed_emperors = {}
#
#     for name, rule in kwargs.items():
#         for arg in args:
#             if name in arg[0] and arg[1] == True:
#                 success_emperors[name] = rule
#             elif name == arg[0] and arg[1] == False:
#                 failed_emperors[name] = rule
#
#     total_emperors = len(success_emperors) + len(failed_emperors)
#     result.append(f'Total number of emperors: {total_emperors}')
#     if success_emperors:
#         success_emperors = sorted(success_emperors.items(), key=lambda kvp: (-kvp[1], kvp[0]))
#         result.append('Successful emperors:')
#         for name, rule in success_emperors:
#             result.append(f'****{name}: {rule}')
#     if failed_emperors:
#         failed_emperors = sorted(failed_emperors.items(), key=lambda kvp: (kvp[1], kvp[0]))
#         result.append('Unsuccessful emperors:')
#         for name, rule in failed_emperors:
#             result.append(f'****{name}: {rule}')
#
#     return '\n'.join(result)


def list_roman_emperors(*args, **kwargs):
    success_emperors = {}
    failed_emperors = {}

    for emperor, status in args:
        if status:
            success_emperors[emperor] = kwargs[emperor]
        else:
            failed_emperors[emperor] = kwargs[emperor]

    total_emperors = len(args)
    result = [f'Total number of emperors: {total_emperors}']
    if success_emperors:
        success_emperors = sorted(success_emperors.items(), key=lambda kvp: (-kvp[1], kvp[0]))
        result.append('Successful emperors:')
        for name, rule in success_emperors:
            result.append(f'****{name}: {rule}')
    if failed_emperors:
        failed_emperors = sorted(failed_emperors.items(), key=lambda kvp: (kvp[1], kvp[0]))
        result.append('Unsuccessful emperors:')
        for name, rule in failed_emperors:
            result.append(f'****{name}: {rule}')

    return '\n'.join(result)

# print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14, ))
print(
    list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False),
                        ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19, ))
# print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19,
#                           Claudius=13, ))
