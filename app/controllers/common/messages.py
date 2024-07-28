import re

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


def exception_error_message(error):
    return f'Something went wrong: {error}'

def integrity_error_message(error):
    match = re.search(r'DETAIL:  Key \(([^)]+)\)=\(([^)]+)\) already exists.', f"{error}")
    
    if match:
        field_name = match.group(1).replace('"', '')
        return f"{field_name} already exists."