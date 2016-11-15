# how to get started; Python

print('udacity'[0])
# prints zero place holder
print('udacity'[1+1])
# prints 2 place holder
print('udacity'[-1])
# prints last place holder

s = 'Hello there'
print(s[3])
print(s[1+1+1])
# both print statements refer to the same place
print(s[-1])
print((s+s)[-1])
# both print statements refer to the same place


word = 'assume'
# print sub sequences
print(word[3])  # prints fourth letter
print(word[3:3])  # prints nothing! no characters between
print(word[:])  # prints full string
print(word[4:6])  # prints fifth and sixth letters (starts at start #, ends one before end #)
print('A' + word[1:])  # prints A + ssume
print(word[:-1])  # prints until last letter (**not full word)
print(word[:3]+word[3:])  # prints full word

print("place marker")

rex = 'Rex is the biggest old "baddest" old biggest old dog'
# finding strings in strings, CAPS matter
print(rex.find('biggest'))  # prints location of first occurrence of 'biggest'
print(rex[11:])  # prints string from location 11
print(rex.find('biggest', 12))  # finds the NEXT location of biggest (add one to first location)
print(rex.find('bog'))  # evals to -1; no occurrence


# ====== Crawler


# page = content of some website as a string
# loaded in Udacity; not available here-----
page = 'xyz <a href= "link_1"> abc <a href= "link_2"> def <a href= "link_3"> ghi'

start_link = page.find('<a href=')
# finds position of first <a href>
# pull out link:
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote +1)
url = page[start_quote+1:end_quote]

# ===== End Crawler

print('End of Lesson')
# EOL
