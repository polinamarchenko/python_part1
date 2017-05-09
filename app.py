def difference(a,b):
    print(a-b)
    return a-b

difference(2,3)

def product(a,b):
    print(a*b)
    return a*b

product(2,3)

def print_day(num):
    if num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    elif num == 7:
        return "Sunday"
    elif num not in range(1,8):
        return None

print_day(3)

def last_element(my_list):
    if not my_list:
        return None
    else:
        print(my_list[-1])
        return my_list[-1]

last_element([1,2,3,4])

def number_compare(a,b):
    if a > b:
        print("First is greater!")
    elif a < b:
        print("Second is greater!")
    else:
        print("Numbers are equal")

number_compare(2,3)

def single_letter_count(word,char):
    word.lower()
    char.lower()
    if char not in word:
        return 0
    return word.count(char)

single_letter_count("banana", "a")

def multiple_letter_count(string):
    return {val: string.count(val) for val in string}

multiple_letter_count("banana")

def list_manipulation(l, command, location, val=None):
    if(command == "remove" and location == "end"):
            return l.pop()
    elif(command == "remove" and location == "beginning"):
            return l.pop(0)
    elif(command == "add" and location == "beginning"):
            l.insert(0, val)
            return l
    elif(command == "add" and location == "end"):
            l.append(val)
            return l

list_manipulation([1,2,3,4], "remove", "beginning")

def is_Palindrome(collection):
    True if collection[::-1] == collection else False

is_Palindrome("asddsa")

def frequency(l, term):
    return l.count(term)

frequency([1,2,3,4,1,1,1], 1)

def flip_case(string, char):
    new_str = ''
    for el in string:
        if (el == char.lower()):
            new_str += el.upper()
        elif (el == char.upper()):
            new_str += el.lower()
        else:
            new_str += el
    return new_str

flip_case("Hardy har har", "h")

def multiply_even_numbers(l):
    prod = 1
    for val in l:
        if val % 2 == 0:
            prod *= val
    return prod

multiply_even_numbers([1,2,3,4,5])

def capitalize(string):
    return string.capitalize()

capitalize("polina")

def compact(l):
    print([val for val in l if val])

compact([1,2,"", [], False, {}, "All done"])

def partition(coll, fn):
    list1 = []
    list2 = []
    list3 = []
    for val in coll:
        if fn(val):
            list1.append(val)
        else:
            list2.append(val)
    list3.append(list1)
    list3.append(list2)
    return(list3)

def is_even(num):
    return num % 2 == 0

partition([1,2,3,4,5,6], is_even)

def intersection(list1, list2):
    return [val for val in list2 if val in list1]

intersection([1,2,3],[2,3,4])

def mode(l):
    count = {val:l.count(val) for val in l}
    key_max = ''
    for key, value in count.items():
        if (key_max == '' or count[key] > count[key_max]):
            key_max = key
    return key_max

mode([1,2,3,4,5,6,6,6,6])

def once(fn):
    def inner(*args):
        inner.counter += 1
        if (inner.counter == 1):
            return fn(*args)
        else:
            return None
    inner.counter = 0
    return inner

def add(a,b):
    return a+b

def run_once(fn):
    def inner(*args):
        inner.counter += 1
        if (inner.counter == 1):
            return fn(*args)
        else:
            return None
    inner.counter = 0
    return inner

@run_once
def add(a,b):
    return a+b
