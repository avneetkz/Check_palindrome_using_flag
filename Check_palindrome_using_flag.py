# function to check whether the string is palindrome or not 
def palin(str):
    j= -1
    flag= 0
    
    for i in str:
        if(i != str[j]):
            flag= 1
        j -= 1

    if (flag== 1):
        print(f'{str} is not palindrome')
    else:
        print(f'{str} is palindrome')
            

# driver code       
if __name__=="__main__":
    string= input("Enter a string to check whether its palindrome or not: ")
    palin(string)
    
    
