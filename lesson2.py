page = 'xyz <a href= "link_1"> abc <a href= "link_2"> def <a href= "link_3"> ghi'



# Procedures & Control

# ====== Crawler

# start_link = page.find('<a href=')
# start_quote = page.find('"', start_link)
# end_quote = page.find('"', start_quote +1)
# url = page[start_quote+1:end_quote]
# print(url)
# # find next link
# page = page[end_quote]
# start_link = page.find('<a href=')
# ... repeat above portion.


# def get_next_target(page):
#     # proceduralize the repeat portion above
#     start_link = page.find('<a href=')
#     start_quote = page.find('"', start_link)
#     end_quote = page.find('"', start_quote + 1)
#     url = page[start_quote + 1:end_quote]
#     return url, end_quote

# ======= End Crawler


def rest_of_string(e):
    return e[1:]
print(rest_of_string('example'))  # prints string from location 1


def inc(n):
    return n + 1  # takes a number as input and outputs that number plus one
print(inc(3))  # prints 3 + 1 | 4


def square(a):
    return a*a  # takes a number as input and outputs that number squared
print(square(3))  # prints 3*3 | 9


def square2(a):
    return a**2 # takes a number as input and outputs that number squared
print(square2(3))  # prints 3**2 | 9


def sum3(a,b,c):
    # def procedure that outputs the sum of three input numbers
    return a+b+c
print(sum3(1,5,6))  # prints total |12


def abbaize(a,b):
    # def pro that takes two inputs and returns a string of the first one
    # followed by 2 repetitions of the second input
    # followed by the first input
    return a + b + b + a
print(abbaize('m','n'))  # if numbers, it would add them


def find_second(a,b):
    # def pro that takes 2 strings: search and target
    # output a number that is the location of the second occurrence
    # of the target string
    first_b = a.find(b)
    return a.find(b, first_b+1)
print(find_second('biggest old baddest old dog', 'old'))  # prints second occurrence of old


# Decisions: boolean
print(2>3)  # returns True
print(21>3)  # returns False
print(7*3<21)  # returns True
print(7 == 7)  # returns True
print( 7 == 9)  # returns False


def absolute(x):
    # return absolute value of number
    if x < 0:
        x = -x
    return x
print(absolute(-9))
print(absolute(9))
print(abs(-9))  # built in function **


def bigger(a,b):
    # takes two numbers, outputs greater
    if a > b:
        return a
    return b
print(bigger(7,20))


def is_friend(name):
    # takes string and outputs boolean indicating if
    # the string is the nam eof a friend.
    # friends with names that start with D
    return name[0]=='D'
print(is_friend('David'))  # prints True
print(is_friend('Michael'))  # prints False


def is_friend2(name):
    # friends with names that start with D and N
    if name[0] == 'D':
        return True
    if name[0] == 'N':
        return True
    return False
print(is_friend2('Daisy'))  # prints True
print(is_friend2('Megan'))  # prints False
print(is_friend2('Nancy'))  # prints True


# BEST **
def is_friend3(name):
    return name[0] == 'D' or name[0] == 'N'
print(is_friend3('Daisy'))  # prints True
print(is_friend3('Megan'))  # prints False
print(is_friend3('Nancy'))  # prints True


def biggest(a,b,c):
    return max(a,b,c)
print(biggest(4,2,7))


def median(a,b,c):
    big = max(a,b,c)
    if big == a:
        return bigger(b,c)  # bigger line 92
    if big == b:
        return bigger(a,c)
    return bigger(a,b)
print(median(5,8,2))


# Loops
# while is continuous


i = 19
while i < 22:
    print(i)
    i += 1

# != NOT EQUAL

i = 0
while i != 10:
    i += 1
    print(i)  # prints numbers 1-10
    # CAREFUL. if it had not equaled 10 at some point, would continue to run forever; see below

# i = 1
# while i != 10:
#     i += 2
#     print(i)
# runs forever (prints 3, 5, 7, 9, 11, 13... skips 10)


def print_numbers(x):
    i = 0
    while i != x:
        i += 1
        print(i)
print(print_numbers(5))


def factorial(n):
    result = 1
    while n >= 1:
        result *= n
        n = n -1
    return result
print(factorial(5))


# == Break


# not the best way to do this, but illustrates the concept
# above example is BETTER
def print_numbers2(n):
    i = 1
    while True:
        if i > n:
            break
        print(i)
        i += 1
print(print_numbers2(5))


# ===================================================== CRAWLER

start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote+1:end_quote]
print(url)
# find next link
page = page[end_quote:]


def get_next_target(page):
    start_link = page.find('<a href=')
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

print(print_all_links(page))


# ===================================================== END CRAWLER


def udacify(x):
    return "U" + x
print(udacify('acify'))


def countdown(x):
    i = x
    while i > 0:
        print(i)
        i -= 1
    print("Blastoff")
print(countdown(5))


# relook at this*
def find_last(string, target):
    last_pos = -1
    while True:
        pos = string.find(target, last_pos +1)
        if pos == -1:
            return last_pos
        last_pos = pos
print(find_last('big old little old dog', 'old'))


print("End of Lesson")
# == End of Lesson
