#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##Specify Correct Character Encoding
import sys 

class SExpressionCalculator:


    def evaluate_expression(self,expr_input)->int:
        expr_end_tag = ')'
        #loop until all expressions have been evaluated
        while(expr_end_tag in expr_input):
            end_sub_expr = expr_input.find(')')
            start_sub_expr = expr_input[0:end_sub_expr].rindex('(')
            parsed_expr = expr_input[start_sub_expr+1:end_sub_expr] ##creating an expression from the FUNC EXPR EXPR wit
            output_val = SExpressionCalculator().evaluate_singular_expression(parsed_expr)

            ## only 1 expression, no nested expression so we can return this singular calculated value
            if(start_sub_expr == 0):
                return output_val
            
            else:
            ## replace an instance of an expression in the input with the calculated value 
            ## repeat until entire input string is calculated and then repeat until entire string is calculated
                expr_input = expr_input[0:start_sub_expr] + str(output_val) + expr_input[end_sub_expr+1:]
        return int(expr_input)

    ## evaluates a single expression ex. add 4 6
    def evaluate_singular_expression(self,expr:str)->int:
        if(isinstance(expr, str)==False):
            raise ValueError("input must be a string")
        expr = expr.split()
        func = expr[0]
        if(len(expr)!= 3 or (func != "add" and func != "multiply")):
            raise ValueError("Invalid Functions Present") 
        elif(func == 'add'):
            return int(expr[1]) + int(expr[2])
        elif(func == 'multiply'):
            return int(expr[1]) * int(expr[2])

        
def main():
    ##command line param"
    print(SExpressionCalculator().evaluate_expression(sys.argv[1]))


if __name__ == '__main__':
    main()