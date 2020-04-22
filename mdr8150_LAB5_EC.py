# Michael Rao
# 4/22/2020
# 1001558150
# Windows 10 / Python 3.7.6

import sys # used to exit the program if no valid file name is provided
import os

# Takes in lines of a file formatted in infix 
# Converts infix expression to postfix
# calculates expression
# Expressions have to formatted with spaces, seperating operands and operators
# Only supports +, -, *, /, ^
    
#Dictionary of supported operators 
OPERATORS = {
    '+' : (0),
    '-' : (0),
    '*' : (5),
    '/' : (5),
    '%' : (5),
    '^' : (10)
}

def main(): 
    filepath = "input_RPN_EC.txt"

    # Checks file to make sure it exist
    if not os.path.isfile(filepath):
        print("File or file path does not exist...".format(filepath))
        sys.exit()
    
    with open(filepath) as fp:
        for line in fp:
            input = line.split()
            output = infixToPostfix(input)
            if output == -1 :
                print("Please provide proper input.... ")
                print()
            else :
                print("Formatted in RPN: ", end = " ")
                for i in range(len(output)):
                    print(output[i], end = " ")
                print()
                RPNCalculation(output)

# Check if operator is in the dictionary of operators
# Returns True if the token is a operator 
# Returns False if the toke is not a operator 
def isOperator(token):
    return token in OPERATORS.keys()

#Compare the precedence of two tokens
def cmpPrecedence(token1, token2):
    return OPERATORS[token1] - OPERATORS[token2]

#Converts an infix expression to Postfix 
#Returns a list of operators and operands in Postfix 
def  infixToPostfix(tokens):
    out = []
    stack = []
    #Read all tokens given 
    for token in tokens: 
        if isOperator(token):
            #If token is an operator
            while len(stack) != 0 and isOperator(stack[-1]):
                
                if ( cmpPrecedence(token, stack[-1]) < 0):
                    
                    out.append(stack.pop())
                    continue 
                break
            stack.append(token)
        elif token == '(': 
            stack.append(token) 
        elif token == ')':
            while len(stack) != 0 and stack[-1] != '(':
                out.append(stack.pop())
            stack.pop() 
        elif token.isdigit():
            out.append(token)
        else :
            #print('This character is not supposrted: %s' % token)
            print(ValueError('This character is not supported: %s' % token))
            return -1 
    while len(stack) != 0:
        out.append(stack.pop())
    return out

def RPNCalculation(RPNList):
    stack = []
    for token in RPNList:
        if isOperator(token):
            val_1 = int(stack.pop())
            val_2 = int(stack.pop())
            if token == '+':
                val = val_1 + val_2
            elif token == '-':
                val = val_1 - val_2
            elif token == '*':
                val = val_1 * val_2
            elif token == '/':
                val = val_2 / val_1
            elif token == '%':
                val = val_2 % val_1
            elif token == '^':
                val = pow(val_2,val_1)
            stack.append(val)
        else :
            stack.append(token)
    print("Evaluates to: ",stack.pop())
    print()        


if __name__ == '__main__':
    main()
