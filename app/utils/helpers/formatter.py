def billFormat(value, default_value=0.00):
    if value is None:
        return f"{default_value:.2f}"
    return f"{value:.2f}"