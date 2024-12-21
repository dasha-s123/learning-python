from Restaurant import IceCreamStand as ICS, Restaurant as RS

ice_cream_cafe_1 = ICS('Пингвин', 'мороженное',
                                 'ваниль', 'клубника', 'шоколад',
                                 open=False)

cafe_1 = RS('Тратория', 'пиццерия')

ice_cream_cafe_1.describe_restaurant()
ice_cream_cafe_1.set_number_served(4)
ice_cream_cafe_1.show_number_served()
ice_cream_cafe_1.show_flavors()
ice_cream_cafe_1.open_restaurant()
print()
cafe_1.describe_restaurant()
cafe_1.set_number_served(4)
cafe_1.show_number_served()
cafe_1.open_restaurant()
cafe_1.increasement_number_served(2)
cafe_1.show_number_served()