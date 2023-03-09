from odoo import models, fields, api


class SocialStock(models.Model):
    _name = "stock.management"
    _description = "Social stocks management in red crescent"
    Date = fields.Date()
    Pate = fields.Char()
    Couscous = fields.Char()
    Soupe_SELECTION = [
        ('250g', '250g'),
        ('500g', '500g'),
        ('1kg', '1kg'),
    ]
    Soup_unity = fields.Selection(Soupe_SELECTION, string="Soupe Unity")
    Soup_quantity = fields.Char(string="Soupe Quantity")
    Tomate_SELECTION = [
        ('500g', '500g'),
        ('1kg', '1kg'),
    ]

    Tomato_unity = fields.Selection(Tomate_SELECTION)
    Tomato_quantity = fields.Char(string="Tomato Quantity")
    huile_SELECTION = [
        ('1L', '1L'),
        ('1.8L', '1.8L'),
        ('3L', '3L'),
        ('5L', '5L'),
    ]
    Oil_unity = fields.Selection(huile_SELECTION)
    Oil_quantity = fields.Char(string="Oil Quantity")
    Milk = fields.Char()
    Harissa_SELECTION = [
        ('70g', '70g'),
        ('150g', '150g'),
        ('500g', '500g'),
    ]
    Harissa_unity = fields.Selection(Harissa_SELECTION)
    Harissa_quantity = fields.Char(string="Harissa Quantity")
    Malsouka = fields.Char()
    Sugar = fields.Char()
    Rice = fields.Char()
    Jam = fields.Char()
    Coffee_SELECTION = [
        ('100g', '100g'),
        ('150g', '150g'),
        ('200g', '200g'),
        ('250g', '250g'),
        ('500g', '500g'),
        ('1kg', '1kg'),
    ]
    Coffee_unity = fields.Selection(Coffee_SELECTION)
    Coffee_quantity = fields.Char(string="Coffee Quantity")
    Tea_SELECTION = [
        ('100g', '100g'),
        ('150g', '150g'),
        ('200g', '200g'),
        ('250g', '250g'),
        ('500g', '500g'),
        ('1kg', '1kg'),
    ]
    Tea_unity = fields.Selection(Tea_SELECTION)
    Tea_quantity = fields.Char(string="Tea Quantity")
    Tuna_SELECTION = [

        ('65g', '650g'),
        ('160g', '160g'),
        ('260g', '260g'),
        ('400g', '400g'),
    ]
    Tuna_unity = fields.Selection(Tuna_SELECTION)
    Tuna_quantity = fields.Char(string="Tuna Quantity")
    EggTray = fields.Char()
    Cheese_SELECTION = [

        ('8g', '8g'),
        ('16g', '16g'),
        ('24g', '24g'),
    ]
    Cheese_unity = fields.Selection(Cheese_SELECTION)
    Cheese_quantity = fields.Char(string="Cheese Quantity")
    Salt = fields.Char()
    Chameya_SELECTION = [
        ('200g', '200g'),
        ('350g', '350g'),
    ]
    Chameya_unity = fields.Selection(Chameya_SELECTION)
    Chameya_quantity = fields.Char(string="Chameya Quantity")
    Chocoline = fields.Char()
    Cream = fields.Char()
    Soda_SELECTION = [
        ('1L', '1L'),
        ('1.5L', '1.5L'),
        ('2L', '2L'),
    ]
    Soda_unity = fields.Selection(Soda_SELECTION)
    Soda_quantity = fields.Char(string="Soda Quantity")
    def add_stock(self, stock_data):
        stock = self.create(stock_data)
        return stock

    def update_stock(self, stock_data):
        self.write(stock_data)
        return True

    def delete_stock(self):
        self.unlink()
        return True

    def save_stock(self):
        self.ensure_one()

        if self.id:
            self.update_stock({
                'Date': self.Date,
                'Pate': self.Pate,
                'Couscous': self.Couscous,
                'Soup_unity': self.Soup_unity,
                'Soup_quantity': self.Soup_quantity,
                'Tomato_quantity': self.Tomato_quantity,
                'Tomato_unity': self.Tomato_unity,
                'Oil_quantity': self.Oil_quantity,
                'Oil_unity': self.Oil_unity,
                'Milk': self.Milk,
                'Harissa_quantity': self.Harissa_quantity,
                'Harissa_unity': self.Harissa_unity,
                'Malsouka': self.Malsouka,
                'Sugar': self.Sugar,
                'Rice': self.Rice,
                'Jam': self.Jam,
                'Coffee_unity': self.Coffee_unity,
                'Coffee_quantity': self.Coffee_quantity,
                'Tea_quantity': self.Tea_quantity,
                'Tea_unity': self.Tea_unity,
                'Tuna_quantity': self.Tuna_quantity,
                'Tuna_unity': self.Tuna_unity,
                'EggTray': self.EggTray,
                'Cheese_quantity': self.Cheese_quantity,
                'Cheese_unity': self.Cheese_unity,
                'Salt': self.Salt,
                'Chameya_quantity': self.Chameya_quantity,
                'Chameya_unity': self.Chameya_unity,
                'Chocoline': self.Chocoline,
                'Cream': self.Cream,
                'Soda_quantity': self.Soda_quantity,
                'Soda_unity': self.Soda_unity,
            })
        else:
            self.add_stock({
                'Date': self.Date,
                'Pate': self.Pate,
                'Couscous': self.Couscous,
                'Soup_unity': self.Soup_unity,
                'Soup_quantity': self.Soup_quantity,
                'Tomato_quantity': self.Tomato_quantity,
                'Tomato_unity': self.Tomato_unity,
                'Oil_quantity': self.Oil_quantity,
                'Oil_unity': self.Oil_unity,
                'Milk': self.Milk,
                'Harissa_quantity': self.Harissa_quantity,
                'Harissa_unity': self.Harissa_unity,
                'Malsouka': self.Malsouka,
                'Sugar': self.Sugar,
                'Rice': self.Rice,
                'Jam': self.Jam,
                'Coffee_unity': self.Coffee_unity,
                'Coffee_quantity': self.Coffee_quantity,
                'Tea_quantity': self.Tea_quantity,
                'Tea_unity': self.Tea_unity,
                'Tuna_quantity': self.Tuna_quantity,
                'Tuna_unity': self.Tuna_unity,
                'EggTray': self.EggTray,
                'Cheese_quantity': self.Cheese_quantity,
                'Cheese_unity': self.Cheese_unity,
                'Salt': self.Salt,
                'Chameya_quantity': self.Chameya_quantity,
                'Chameya_unity': self.Chameya_unity,
                'Chocoline': self.Chocoline,
                'Cream': self.Cream,
                'Soda_quantity': self.Soda_quantity,
                'Soda_unity': self.Soda_unity,
            })
