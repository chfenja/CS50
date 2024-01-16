# Could be optimized

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if start_two_letters(plate):
        if num_c(plate):
            if num_at_end(plate):
                if no_punc_space(plate):
                    return True
    else:
        return False

def num_at_end(plate):
    found_number = False
    for c in plate:
        if c.isdigit():
            if c == "0" and not found_number:
                return False
            found_number = True
        if c.isalpha() and found_number:
            return False
    return True

def start_two_letters(plate):
    two_c = plate[0:2]
    if two_c.isalpha():
        return True
    else:
        return False

def num_c(plate):
    if 2 <= len(plate) <= 6:
        return True
    else:
        return False

def no_punc_space(plate):
    if plate.isalnum():
        return True
    else:
        return False

main()
