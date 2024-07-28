def function_route_error_message(function_route, error):
    message = (
        f"An error occured in <b>{function_route}</b>.<br>"
        f"Error: <i>{error}</i><br>"
        f"Please contact customer support."
    )
    
    return message

def class_error_message(class_name):
    message = f"Something went wrong in {class_name}"
    
    return message

def function_route_not_exist(function_route, class_name):
    message =  f"<b>{function_route}</b> does not exist. Please check <b>{class_name}</b>."
    
    return message