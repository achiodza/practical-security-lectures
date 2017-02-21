"""
QUESTION 7
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.  
Sample String : 'The lyrics is not that poor!' 
Expected Result : 'The lyrics is good!'

"""

def not_poor(str1):
  
  isnot = str1.find('is not')
  sbad = str1.find('poor')

  if sbad > isnot:
    #we use the replace keyword to replace that part of the string that we do not want, on the condition that the word poor is followed by the word not 
    str1 = str1.replace(str1[isnot:sbad+4], 'are good')
    #the value 4 is that of the size of the word to be replaced if it is less than that to be replaced then
  return str1
print(not_poor('The lyrics is not that poor!'))
