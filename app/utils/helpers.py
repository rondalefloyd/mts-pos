def getManageTypeByIndex(index):
    match index:
        case 0:
            return 'Sales'
        case 1:
            return 'Transaction'
        case 2:
            return 'Item'
        case 3:
            return 'Stock'
        case 4:
            return 'Promo'
        case 5:
            return 'Reward'
        case 6:
            return 'Member'
        case 7:
            return 'User'