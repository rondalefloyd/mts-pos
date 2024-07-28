import re

def function_route_not_exist(function_route, class_name):
    message =  f"<b>{function_route}</b> does not exist. Please check <b>{class_name}</b>."
    
    return message

def exception_error_message(error):
    return f'Something went wrong: {error}'

def integrity_error_message(error):
    match = re.search(r'DETAIL:  Key \(([^)]+)\)=\(([^)]+)\) already exists.', f"{error}")
    
    if match:
        field_name = match.group(1).replace('"', '')
        return f"<b>{field_name}</b> already exists."
    
def value_error_message(error):
    return 'test'
    pass