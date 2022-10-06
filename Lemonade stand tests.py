import unittest

class InvalidSaleItemError(Exception):
    pass
class MenuItem:
    """Represents Items on the lemonade stand menu"""
    def __init__(self, name, wholesale_cost, selling_price ):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        return self._name

    def get_wholesale_cost(self):
        """Whole sale cost for each Item"""
        return self._wholesale_cost

    def get_selling_price(self):
        """Selling price for each item"""
        return self._selling_price

class SalesForDay:
    """What sold today and how much"""
    def __init__(self, day, sales_dict ):
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        return self._day

    def get_sales_dict(self):
        return self._sales_dict



class LemonadeStand:
    """The name of the lemonade stand, how many days has it been open, the menu and what was sold"""
    def __init__(self, name):
        self._name = name
        self._current_day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        return self._name

    def add_menu_item(self, menu_item):
        """Add Item to the menu"""
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self,sales_dict):
     ''' The sales that happened on a specific day '''
        try:
            for key in sales_dict:
                if key not in self._menu:
                    raise InvalidSaleItemError
            self._sales_for_today = SalesForDay(self._current_day)
            self._sales_record.append(self.sales_for_today)
            self._current_day +=1
        except InvalidSaleItemError:
            finally
            print("this item is not avalible")

    def get_sales_dict_for_day(self, day):
        ''' What sold for the day'''
        for sales_day in self._sales_record:
            if sales_day.get_day() == day:
                return sales_day.get_sales_dict

    def total_sales_for_menu_item(self, menu_item_name):
        total_sales = 0
        for record in self._sales_record:
            for key, value in record.get_sales_dict().items():
                if key.lower() == menu_item_name.lower():
                     total_sales += value
                     return total_sales

    def total_profit_for_menu_item(self, menu_item_name):
        return self._menu[menu_item_name].get_selling_price() * self._total_sales_for_menu_item(menu_item_name)

    def total_profit_for_stand(self):
        total_profit = 0
        for name, menu_item in self._menu.items():
            total_sales_of_item = self.total_sales_for_menu_item(name)
            profit = total_sales_of_item * menu_item.get_selling_price() - total_sales_of_item * menu_item.get_wholesale_cost()
            total_profit += profit
            return total_profit

        if __name__ =="__main__":
            """Menu Items Scone.Cookie and salad wrap are added"""
            scone = MenuItem("Scone", 2.5, 6.5)
            cookie = MenuItem("Cookie", 3.5, 7.5)
            salad_wrap = MenuItem("SaladWrap",10.5,14)
            sales_dict1 = {"Scone": 19, "Cookie":42, "SaladWrap":15}
            sales_dict2 = {"Scone": 29, "Cookie": 52, "SaladWrap":20}

            lemonade_stand = LemonadeStand("Lemon Drop")
            """The lemonade stand is named Lemon Drop """
            lemonade_stand.add_menu_item(scone)
            lemonade_stand.add_menu_item(cookie)
            lemonade_stand.add_menu_item(salad_wrap)

            lemonade_stand.enter_sales_for_today(sales_dict1)
            lemonade_stand.enter_sales_for_today(sales_dict2)