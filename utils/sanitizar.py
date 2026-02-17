
def sanitizar(user_input):
    user_input = user_input.lower()
    user_input = user_input.replace("á", "a")
    user_input = user_input.replace("é", "e")
    user_input = user_input.replace("í", "i")
    user_input = user_input.replace("ó", "o")
    user_input = user_input.replace("ú", "u")
    user_input = user_input.replace("ñ", "n")
    user_input = user_input.replace("ü", "u")
    return user_input  
