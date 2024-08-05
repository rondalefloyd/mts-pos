import re

def entry_has_value(alpha_entry: list = [], numeric_entry: list = [], entry: object = None):
    """
    Validates that specified fields in the entry dictionary have non-empty values for 
    string fields and valid numeric values (including scientific notation) for numeric fields.

    Args:
        alpha_entry (list): List of keys corresponding to string fields to be validated.
        numeric_entry (list): List of keys corresponding to numeric fields to be validated.
        entry (object): Dictionary containing the data to be validated.

    Returns:
        bool: True if all specified fields have valid values, False otherwise.

    Example:
        entry = {
            'name': 'John Doe',
            'age': '30',
            'height': '5.9',
            'weight': '70.5e1'
        }
        alpha_entry = ['name']
        numeric_entry = ['age', 'height', 'weight']

        # This will return True
        result = entry_has_value(alpha_entry, numeric_entry, entry)
    """
    # Check string fields
    for field in alpha_entry:
        value = entry.get_or_none(field, "").strip()
        if not value:
            return False

    # Check numeric fields
    for field in numeric_entry:
        value = entry.get_or_none(field, "").strip()
        float_regex = re.compile(r'^-?\d+(\.\d+)?([eE][-+]?\d+)?$')
        
        if not value or not float_regex.match(value):
            return False
    
    return True
