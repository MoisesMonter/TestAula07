import re


def validor(var):
    # Se der pra fazer em regex é pra usar
    if len(var) == 1:
        info = r"^[a-zA-Z]$"  
    else: 
        info = r"^[a-zA-Z][a-zA-Z0-9]*[1-6][a-zA-Z0-9]*$"
    
    return bool(re.match(info, var))

