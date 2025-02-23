def all_elements_true(t):
    return all(t)

def parse_input(value):
    if value.lower() == "none":
        return None
    elif value.lower() == "false":
        return False
    elif value.isdigit():
        return int(value)
    return value 
values = tuple(parse_input(v) for v in input("Enter tuple elements separated by space: ").split())

print("All elements are true:", all_elements_true(values))
