def is_entry_valid(entry_keys:list, entry:object):
    for field in entry_keys:
        if not entry.get(field) or entry[field].strip() == '':
            return False
        
    return True