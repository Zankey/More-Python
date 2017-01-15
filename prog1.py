#Step 1: Input

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
string3 = input("Enter the third string: ")
string4 = input("Enter the fourth string: ")


#Step 2: Process

#if-elif-else chain for the largest string

if string1 > string2 and string1 > string3 and string1 > string4:
    LARGEST_STRING = string1

elif string2 > string1 and string2 > string3 and string2 > string4:
    LARGEST_STRING = string2

elif string3 > string1 and string3 > string2 and string3 > string4:
    LARGEST_STRING = string3

else:
    LARGEST_STRING = string4
    

#if-elif-else chain for the second largest string
    
     # string1 cases

if string1 < string2 and string1 > string3 and string1 > string4:
    SECOND_LARGEST_STRING = string1

elif string1 < string3 and string1 > string2 and string1 > string4:
    SECOND_LARGEST_STRING = string1

elif string1 < string4 and string1 > string2 and string1 > string3:
    SECOND_LARGEST_STRING = string1

    #string2 cases

elif string2 < string1 and string2 > string3 and string2 > string4:
    SECOND_LARGEST_STRING = string2

elif string2 < string3 and string2 > string1 and string2 > string4:
    SECOND_LARGEST_STRING = string2

elif string2 < string4 and string2 > string1 and string2 > string3:
    SECOND_LARGEST_STRING = string2

     #string 3 cases

elif string3 < string1 and string3 > string2 and string3 > string4:
    SECOND_LARGEST_STRING = string3

elif string3 < string2 and string3 > string1 and string3 > string4:
    SECOND_LARGEST_STRING = string3

elif string3 < string4 and string3 > string1 and string3 > string2:
    SECOND_LARGEST_STRING = string3

    #string4 case
    
else:   
    SECOND_LARGEST_STRING = string4


#if-elif-else chain for the second smallest string

   # string1 cases

if string1 > string2 and string1 < string3 and string1 < string4:
    SECOND_SMALLEST_STRING = string1

elif string1 > string3 and string1 < string2 and string1 < string4:
    SECOND_SMALLEST_STRING = string1

elif string1 > string4 and string1 < string2 and string1 < string3:
    SECOND_SMALLEST_STRING = string1

    #string2 cases

elif string2 > string1 and string2 < string3 and string2 < string4:
    SECOND_SMALLEST_STRING = string2

elif string2 > string3 and string2 < string1 and string2 < string4:
    SECOND_SMALLEST_STRING = string2

elif string2 > string4 and string2 < string1 and string2 < string3:
    SECOND_SMALLEST_STRING = string2

     #string 3 cases

elif string3 > string1 and string3 < string2 and string3 < string4:
    SECOND_SMALLEST_STRING = string3

elif string3 > string2 and string3 < string1 and string3 < string4:
    SECOND_SMALLEST_STRING = string3

elif string3 > string4 and string3 < string1 and string3 < string2:
    SECOND_SMALLEST_STRING = string3

    #string4 case

else:  
    SECOND_SMALLEST_STRING = string4



#if-elif-else chain for the smallest string

if string1 < string2 and string1 < string3 and string1 < string4:
    SMALLEST_STRING = string1

elif string2 < string1 and string2 < string3 and string2 < string4:
    SMALLEST_STRING = string2

elif string3 < string1 and string3 < string2 and string3 < string4:
    SMALLEST_STRING = string3

else:
    SMALLEST_STRING = string4


#Step 3: Output

print("\nThe largest string is:", LARGEST_STRING)
print("The second largest string is:", SECOND_LARGEST_STRING)
print("The second smallest string is:", SECOND_SMALLEST_STRING)
print("The smallest string is:", SMALLEST_STRING)











