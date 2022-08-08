import calendar
import datetime

class Flower():
    def __init__(self, name, once_every, how_much):
        self.name = name
        self.once_every = once_every
        self.how_much = how_much


#All inputs of the flower, prolly later im gonna do it in list of lists so we can get acess to every flower insted of just one
flowers = []
flower = Flower(name=input('What is the name of the flower: '), once_every=int(input('How many days till another watering: ')), how_much=float(input('How much water in ml: ')))

flowers.append(flower.name)
flowers.append(flower.once_every)
flowers.append(flower.how_much)
print(flowers)

'''#Once every 'days' list
once_every_list = []
once_every_list.append(flower.once_every)
'''

#Here we get next day to watering our flower
now = datetime.datetime.now()
base = datetime.datetime.today()
print('Today is: ',now.strftime("%A"), ' next watering should be done in: ', base+datetime.timedelta(days=flowers[1]), f' and you should add {flower.how_much} ml of water')