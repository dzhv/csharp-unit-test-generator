from typing import List, Any

def assert_equal(actual, expected):
    assert actual == expected, f"objects were not equal.\nActual: {actual},\nExpected: {expected}"

def deep_compare(left, right, excluded_keys = []):
    print(f"Comparing actual: {left}\nexpected: {right}")

    # convert left and right to dicts if possible, skip if they can't be converted
    try: 
        left = left.__dict__
        right = right.__dict__
    except:
        pass

    # both sides must be of the same type 
    if type(left) != type(right):
        return False

    # compare the two objects or dicts key by key
    if type(left) == dict:
        return compare_dicts(left, right, excluded_keys)

    # check for each item in lists
    if type(left) == list:
        return compare_lists(left, right, excluded_keys)

    print(f"Standard comparison: {left} vs {right}")
    print(f"result: {left == right}")
    return left == right

def compare_dicts(left, right, excluded_keys) -> bool:
    for key in left:
        # make sure that we did not exclude this key
        if key in excluded_keys:
            continue

        # check if the key is present in the right dict, if not, we are not equals
        if key not in right:
            return False
        else:
            # compare the values if the key is present in both sides
            if not deep_compare(left[key], right[key], excluded_keys):
                return False

    # check if any keys are present in right, but not in left
    for key in right:
        if key not in left and key not in excluded_keys:
            return False
    
    return True

def compare_lists(left: List[Any], right: List[Any], excluded_keys) -> bool:
    # right and left must have the same length
    if len(left) != len(right):
        return False

    # compare each item in the list
    for index in range(len(left)):
        if not deep_compare(left[index], right[index], excluded_keys):
            return False

    return True