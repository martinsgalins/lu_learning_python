from package1 import mod2
def calc(number_1,number_2,operator):      
            if operator == "*" :
                result = number_1*number_2

            elif operator == "-" :
                result =  number_1-number_2

            elif operator == "+" :
                result =  number_1+number_2

            else:
                result =  number_1/number_2

            return mod2.print_result(number_1,number_2,operator,result)           