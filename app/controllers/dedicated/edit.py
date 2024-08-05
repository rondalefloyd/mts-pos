import os, sys, logging, math, json
from peewee import *
from datetime import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append(os.path.abspath(''))  # required to change the default path
from app.models.entities import (
    Users,
    Members,
    Rewards,
    Promos,
    ItemTypes,
    Brands,
    Suppliers,
    SalesGroups,
    Items,
    ItemPrices,
    Stocks,
)
from app.utils.databases import postgres_db


class EditThread(QThread):
    finished = pyqtSignal(object)
    
    def __init__(self, function_route, entry=None):
        super().__init__()
        self.function_route = function_route
        self.entry = entry
    
    def run(self):
        result = {
            'success': False,
            'message': 'N/A',
            'dictData': {},
            'listData': [],
        }
        
        try:
            with postgres_db:
                if self.function_route == 'edit_items_related_data_by_ids':
                    result = edit_items_related_data_by_ids(self.entry, result)
                elif self.function_route == 'edit_members_data_by_id':
                    result = edit_members_data_by_id(self.entry, result)
                elif self.function_route == 'edit_promos_data_by_id':
                    result = edit_promos_data_by_id(self.entry, result)
                elif self.function_route == 'edit_rewards_data_by_id':
                    result = edit_rewards_data_by_id(self.entry, result)
                elif self.function_route == 'edit_stocks_data_by_id':
                    result = edit_stocks_data_by_id(self.entry, result)
                else:
                    result['message'] = f"'{self.function_route}' is an invalid function..."
                        
            logging.info('database operation done...')
            
        except Exception as exception:
            result['message'] = exception
            postgres_db.rollback()
            logging.error('exception: ', exception)
            logging.info('database operation rolled back...')
            
        finally:
            postgres_db.close()
            logging.info('database closed...')
            
        self.finished.emit(result)
        print(f'{self.function_route} -> result:', json.dumps(result, indent=4, default=str))
        
# add function here
def edit_items_related_data_by_ids(entry=None, result=None):
    # TODO: finish this
    return result
    pass
def edit_members_data_by_id(entry=None, result=None):
    try:
        member = Members.select().where(Members.MemberName == entry['memberName'])
        
        if member.exists():
            result['message'] = 'Member already exists'
            return result
            
        member = Members.get_or_none(Members.Id == entry['id'])
        member.MemberName = entry['memberName']
        member.BirthDate = entry['birthDate']
        member.Address = entry['address']
        member.MobileNumber = entry['mobileNumber']
        member.Points = entry['points']
        member.save()
        
        result['success'] = True
        result['message'] = 'Member updated'
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def edit_promos_data_by_id(entry=None, result=None):
    try:
        promo = Promos.select().where(Promos.PromoName == entry['promoName'])
        
        if promo.exists():
            result['message'] = 'Promo already exists'
            return result
            
        promo = Promos.get_or_none(Promos.Id == entry['id'])
        promo.PromoName = entry['promoName']
        promo.DiscountRate = entry['discountRate']
        promo.Description = entry['description']
        promo.save()
        
        result['success'] = True
        result['message'] = 'Promo updated'
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result
    
def edit_rewards_data_by_id(entry=None, result=None):
    try:
        reward = Rewards.select().where(Rewards.RewardName == entry['rewardName'])
        
        if reward.exists():
            result['message'] = 'Reward already exists'
            return result
            
        reward = Rewards.get_or_none(Rewards.Id == entry['id'])
        reward.RewardName = entry['rewardName']
        reward.Points = entry['points']
        reward.Target = entry['target']
        reward.Description = entry['description']
        reward.save()
        
        result['success'] = True
        result['message'] = 'Reward updated'
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result

def edit_stocks_data_by_id(entry=None, result=None):
    try:
        stock = Stocks.get_or_none(Stocks.Id == entry['id'])
        stock.OnHand = entry['onHand']
        stock.Available = entry['available']
        stock.save()
        
        result['success'] = True
        result['message'] = 'Stock updated'
        return result
        
    except Exception as exception:
        result['message'] = f"An error occured: {exception}"
        return result