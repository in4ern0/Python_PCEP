Can you catch SyntaxErrors?
In the video with the introduction to exceptions, I've mentioned that you can use the default except block to catch any sort of exception:

try:
  # your code
except:
  # any exception
However, there is one special exception type: SyntaxError. You should pay attention to how it works.

If you raise a SyntaxError manually, then you can catch it in the except block just fine:

try:
  raise SyntaxError
except:
  print('Got it!') # SyntaxError is caught here
However, if you make a syntax error in the try block and Python automatically raises a SyntaxError for you, then you cannot catch it:

try:
  5:4 # this line generates a SyntaxError
except:
  print('Got it!') # SyntaxError is NOT caught here
  
  
  
  
try:
    value = int(input('Enter integer'))
    print('The inverse of', value, 'is', 1/value)
except ZeroDivisionError:
    print('You put 0 there is nothing calculate for zero')
except ValueError:
    print('You did not provide integer number, so I will not calculate')
except:
    print('Something strange happened here sorry')
