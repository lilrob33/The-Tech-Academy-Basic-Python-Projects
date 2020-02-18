

mySentence = 'loves the color'

color_list = ['Blue','Red','Pink','White', 'Black']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name, mySentence, i)
        lst.append(msg)
    return lst

lst = color_function('Pedro')   
for i in lst:
    print(i)
