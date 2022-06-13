from package1 import mod2
def calc(a,b,c):      
            if c == "*" :
                result = a*b
                mod2.ttt(result)
            elif c == "-" :
                result =  a-b
                mod2.ttt(result)
            elif c == "+" :
                result =  a+b
                mod2.ttt(result)
            else:
                result =  a/b
                mod2.ttt(result)       