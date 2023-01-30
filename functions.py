def getaverage(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)
    
#getaverage([5.0, 3.5, 7.8, 9.9, 10.0])


def print_letter_count( text, letter):
    counter = 0
    for char in text:
        if char  == letter:
            counter +=1
    print('Number of', letter, 'is', counter)
#print_letter_count('Welcome', 'e')
print_letter_count(text='Welcome', letter='e')
print_letter_count(letter='e', text='Welcome')


def show_truth():
    mysterious_var.append('New-Salam')
    print(mysterious_var)

mysterious_var = ['Salam']
print(mysterious_var)
show_truth()
print(mysterious_var)


def show_truth():
    global mysterious_var
    mysterious_var = 'New-Salam'
    print(mysterious_var)

mysterious_var = 'Salam'
print(mysterious_var)
show_truth()
print(mysterious_var)
print(mysterious_var)

def show_truth():
    mysterious_var = 'New-Salam'
    print(mysterious_var)

mysterious_var = 'Salam'
print(mysterious_var)
show_truth()
print(mysterious_var)
print(mysterious_var)


