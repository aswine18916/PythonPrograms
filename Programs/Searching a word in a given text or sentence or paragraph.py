import re

"""Finding the occurence of words in a given paragraph and displaying the number of occurence"""
text='''
Jana gana mana adhinayaka Jaya he

Bharata bhagya vidhata

Punjab Sindh Gujarat Maratha 

Dravida Utkala Banga

Vindhya Himachala Yamuna Ganga 

Uchchala Jaladhi taranga

Tava shubha name jage 

Tava shubha asisa mage 

Gahe tava Jaya gatha 

Jana gana mangala dayaka Jaya he 

Bharata bhagya vidhata

Jaya he Jaya he Jaya he Jaya Jaya Jaya Jaya he!
'''



def findall(*yourstring):
    for word in yourstring:
        search = re.findall(word, text)
        print("The searched word {} is present {} times in the whole text".format(word,len(search)))


findall('Jaya', 'Tava')