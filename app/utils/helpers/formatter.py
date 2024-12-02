def billFormat(currency, value, default_value="N/A"):
    if value is None:
        print('look for currency:', currency)
        return f"{default_value}"
    return f"{currency}{value:.2f}"