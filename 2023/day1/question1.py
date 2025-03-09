# https://adventofcode.com/2023/day/1
with open('input.txt', 'r') as file:
    file_content = file.read()
    list1 = []
    list2 = []
    list3 = []
    number_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
    # Add more number words as needed
}
    first_number = None
    last_number = None
    first_found = False
for line in file_content.splitlines():
    list1.append(line)
# for i in list1:
#    jemo = [let for let in i]
#    print(jemo)
for j in list1:
   for jemo in j:
      if jemo.lower() in number_words:
        list3.append(number_words[j.lower()])
      
for i in list1:
    digit_count = 0
    for char in i:
        if char.isdigit() :
         digit_count += 1
         list2.append(char)
      
print(list2)
print(list3)
           
  















