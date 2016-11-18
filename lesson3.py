# Manage Data
# string sequence of characters
# list sequence of anything
# different rules


s = 'yabba'
# string
print(s[0])  # prints y
print(s[2:4])  # prints bb

l = ['yabba', 'dabba', 'do', 'hi', 'bye']
# list
print(l[0])  # prints yabba
print(l[2:4])  # prints ['do', 'hi']

stooges = ['Moe', 'Larry', 'Curly']
# def variable list of 3 stooges
print(stooges)  # prints list of stooges

days_in_month = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']


def how_many_days(month):
    # def takes as an input a number representing a month and returns the number of days in that month
    return days_in_month[month-1]
print(how_many_days(1))


beatles = [['John', 1940],
           ['Paul', 1942],
           ['George', 1943],
           ['Ringo', 1940]]
# nested lists; lists in lists
print(beatles[3])  # prints entire index at location 3; Ringo, 1940
print(beatles[3][0])  # index within index; prints Ringo
print(beatles[3][1])  # prints 1940


countries = [['China', 'Beijing', 1350],
             ['India', 'Delhi', 1210],
             ['Romania','Bucharest', 21],
             ['United States', 'Washington', 307]]
print(countries[1][1])  # print capitol of India
# what multiple of Romanias population is the population of China
print(countries[0][2] / countries[2][2])  # China population = 0,2 | Romania population = 2,2


stooges[2] = 'Shemp'  # changes value of list from Curly to Shemp
print(stooges)


spy = [0, 0, 7]
agent = spy
# aliasing
spy[2] = agent[2]+1
print(spy)
print(agent)

print('place')


def replace_spy(p):
    p[2] += 1
    return p

print(replace_spy(spy))


stooges.append('Curly')
# mutate list by appending a fourth stooge to the list
print(stooges)


add_operator = [0,1] + [2,3]
# takes two lists and makes one
print(add_operator)


print(len(add_operator))
# prints length of list (*no zero placeholder, actually counts from 1)
nested = ['a', ['b', ['c']]]
# ZAC ; does not count lists within lists
print(len(nested))


p = [1,2]
p.append(3)
p = p + [4,5]
# example
print(p)

p = [1,2]
q = [3,4]
p.append(q)  # appends q as list, does not count elements, counts as one
print(len(p))


def print_all_elements(p):
    i = 0
    while i < len(p):
        print(p[i])
        i += 1

def find_element(x,y):
    #  use index; return the index of the first element in the input list that matches the value
    # return -1 if no matching element
    if y not in x:
        return -1
    return x.index(y)
print(find_element([1,2,3],3))


def product_list(list_of_numbers):
    # return number that is result of multiplying all numbers together
    quot = 1
    for i in list_of_numbers:
        quot *= i
    return quot
print(product_list([9]))
# 9
print(product_list([1,2,3,4]))
# 24
print(product_list([]))
# 1


def greatest(list_of_numbers):
    # take a list of POSITIVE integers and return the biggest
    big = 0
    for num in list_of_numbers:
        if num > big:
            big = num
    return big
print(greatest([4,23,1]))
# 23
print(greatest([]))
# 0



