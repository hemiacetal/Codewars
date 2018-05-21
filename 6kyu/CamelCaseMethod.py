def camel_case(string):

    
    return "".join(map(lambda x: "" if len(x) is 0 else x[0].upper()+x[1:],string.split(" ")))
    