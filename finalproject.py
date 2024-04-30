import random

def get_card_color_from_suit(suit):
    if suit == 'Spades' or suit == 'Clubs':
        return 'black'
    else:
        return 'red'


def get_card_face_from_value(value):
    if value <= 10:
        return str(value)
    elif value == 11:
        return 'J'
    elif value == 12:
        return 'Q'
    elif value == 13:
        return 'K'
    else:
        return 'A'


def build_deck():
    deck = []
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    values = range(2, 15)
    for suit in suits:
        for value in values:
            card = {}
            card['value'] = value
            card['suit'] = suit
            card['face'] = get_card_face_from_value(value)
            card['color'] = get_card_color_from_suit(suit)
            deck.append(card)

    return deck

def shuffle(deck):
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        temp = deck[j]
        deck[j] = deck[i]
        deck[i] = temp


def is_high_card(card1,card2,card3,card4,card5):
    if is_pair(card1,card2,card3,card4,card5)==False and is_2_pair(card1,card2,card3,card4,card5)==False and is_3_of_a_kind(card1,card2,card3,card4,card5)==False and is_4_of_a_kind(card1,card2,card3,card4,card5)==False and is_full_house(card1,card2,card3,card4,card5)==False and is_flush(card1,card2,card3,card4,card5)==False and is_straight(card1,card2,card3,card4,card5)==False and is_straight_flush(card1,card2,card3,card4,card5)==False:
        return True
    else:
        return False

def is_pair(card1,card2,card3,card4,card5):
    if is_2_pair(card1,card2,card3,card4,card5) or is_3_of_a_kind(card1,card2,card3,card4,card5) or is_4_of_a_kind(card1,card2,card3,card4,card5) or is_full_house(card1,card2,card3,card4,card5):
        return False
    if card1['value']==card2['value'] or card1['value']==card3['value'] or card1['value']==card4['value'] or card1['value']==card5['value'] or card2['value']==card3['value'] or card2['value']==card4['value'] or card2['value']==card5['value'] or card3['value']==card4['value'] or card3['value']==card5['value'] or card4['value']==card5['value']:
        return True
    else:
        return False

def is_2_pair(card1,card2,card3,card4,card5):
    if is_4_of_a_kind(card1,card2,card3,card4,card5) or is_full_house(card1,card2,card3,card4,card5):
        return False
    pair1counter=0
    pair2counter=0
    if card1['value'] == card2['value']:
        pair1counter+=1
        if card3['value'] == card4['value'] or card3['value'] == card5['value'] or card4['value'] == card5['value']:
            pair2counter+=1
            return True
        else:
            pair1counter=0
            pair2counter=0
    if card1['value'] == card3['value']:
        pair1counter+=1
        if card2['value'] == card4['value'] or card2['value'] == card5['value'] or card4['value'] == card5['value']:
            pair2counter+=1
            return True
        else:
            pair1counter=0
            pair2counter=0
    if card1['value'] == card4['value']:
        pair1counter+=1
        if card2['value'] == card3['value'] or card2['value'] == card5['value'] or card3['value'] == card5['value']:
            pair2counter+=1
            return True
        else:
            pair1counter=0
            pair2counter=0
    if card1['value'] == card5['value']:
        pair1counter+=1
        if card2['value'] == card3['value'] or card2['value'] == card4['value'] or card3['value'] == card4['value']:
            pair2counter+=1
            return True
        else:
            pair1counter=0
            pair2counter=0
    if card2['value'] == card3['value']:
        pair1counter+=1
        if card1['value'] == card4['value'] or card1['value'] == card5['value'] or card4['value'] == card5['value']:
            pair2counter+=1
            return True
        else:
            pair1counter=0
            pair2counter=0
    if card3['value'] == card4['value']:
        pair1counter+=1
        if card1['value'] == card2['value'] or card1['value'] == card5['value'] or card2['value'] == card5['value']:
            pair2counter+=1
            return True
        else:
            pair1counter=0
            pair2counter=0
    if card4['value'] == card5['value']:
        pair1counter+=1
        if card1['value'] == card2['value'] or card1['value'] == card3['value'] or card2['value'] == card3['value']:
            pair2counter+=1
            return True
        else:
            pair1counter=0
            pair2counter=0
    if card2['value'] == card4['value']:
        pair1counter+=1
        if card1['value'] == card3['value'] or card1['value'] == card5['value'] or card3['value'] == card5['value']:
            pair2counter+=1
            return True
        else:
            pair1counter=0
            pair2counter=0
    if card3['value'] == card5['value']:
        pair1counter+=1
        if card1['value'] == card2['value'] or card1['value'] == card4['value'] or card2['value'] == card4['value']:
            pair2counter+=1
            return True
        else:
            pair1counter=0
            pair2counter=0
    if card2['value'] == card5['value']:
        pair1counter+=1
        if card1['value'] == card3['value'] or card1['value'] == card4['value'] or card3['value'] == card4['value']:
            pair2counter+=1
            return True
        else:
            pair1counter=0
            pair2counter=0
    return False

def is_3_of_a_kind(card1,card2,card3,card4,card5):
    if is_full_house(card1,card2,card3,card4,card5) or is_4_of_a_kind(card1,card2,card3,card4,card5):
        return False
    counter=1
    if card1['value']==card2['value']:
        counter+=1
        if card1['value']==card3['value'] or card1['value']==card4['value'] or card1['value']==card5['value']:
            counter+=1
            return True
        else:
            counter=1
    if card1['value']==card3['value']:
        counter+=1
        if card1['value']==card2['value'] or card1['value']==card4['value'] or card1['value']==card5['value']:
            counter+=1
            return True
        else:
            counter=1
    if card1['value']==card4['value']:
        counter+=1
        if card1['value']==card2['value'] or card1['value']==card3['value'] or card1['value']==card5['value']:
            counter+=1
            return True
        else:
            counter=1
    if card1['value']==card5['value']:
        counter+=1
        if card1['value']==card2['value'] or card1['value']==card3['value'] or card1['value']==card4['value']:
            counter+=1
            return True
        else:
            counter=1
    if card2['value']==card3['value']:
        counter+=1
        if card2['value']==card1['value'] or card2['value']==card4['value'] or card2['value']==card5['value']:
            counter+=1
            return True
        else:
            counter=1
    if card2['value']==card4['value']:
        counter+=1
        if card2['value']==card1['value'] or card2['value']==card3['value'] or card2['value']==card5['value']:
            counter+=1
            return True
        else:
            counter=1
    if card2['value']==card5['value']:
        counter+=1
        if card2['value']==card1['value'] or card2['value']==card3['value'] or card2['value']==card4['value']:
            counter+=1
            return True
        else:
            counter=1
    if card3['value']==card4['value']:
        counter+=1
        if card3['value']==card1['value'] or card3['value']==card2['value'] or card3['value']==card5['value']:
            counter+=1
            return True
        else:
            counter=1
    if card3['value']==card5['value']:
        counter+=1
        if card3['value']==card1['value'] or card3['value']==card2['value'] or card3['value']==card4['value']:
            counter+=1
            return True
        else:
            counter=1
    if card4['value']==card5['value']:
        counter+=1
        if card4['value']==card1['value'] or card4['value']==card2['value'] or card4['value']==card3['value']:
            counter+=1
            return True
        else:
            counter=1
    if counter !=3:
        return False

def is_4_of_a_kind(card1,card2,card3,card4,card5):
    if card1['value']==card2['value'] and card1['value']==card3['value'] and card1['value']==card4['value']:
        return True
    elif card1['value']==card2['value'] and card1['value']==card3['value'] and card1['value']==card5['value']:
        return True
    elif card1['value']==card2['value'] and card1['value']==card4['value'] and card1['value']==card5['value']:
        return True
    elif card1['value']==card3['value'] and card1['value']==card4['value'] and card1['value']==card5['value']:
        return True
    elif card2['value']==card3['value'] and card2['value']==card4['value'] and card2['value']==card5['value']:
        return True
    else:
        return False

def is_full_house(card1,card2,card3,card4,card5):
    if card1['value']==card2['value'] and card3['value']==card4['value'] and card3['value']==card5['value']:
        return True
    elif card1['value']==card3['value'] and card2['value']==card4['value'] and card2['value']==card5['value']:
        return True
    elif card1['value']==card4['value'] and card2['value']==card3['value'] and card2['value']==card5['value']:
        return True
    elif card1['value']==card5['value'] and card2['value']==card3['value'] and card2['value']==card4['value']:
        return True
    elif card2['value']==card3['value'] and card1['value']==card4['value'] and card1['value']==card5['value']:
        return True
    elif card2['value']==card4['value'] and card1['value']==card3['value'] and card1['value']==card5['value']:
        return True
    elif card2['value']==card5['value'] and card1['value']==card3['value'] and card1['value']==card4['value']:
        return True
    elif card3['value']==card4['value'] and card1['value']==card2['value'] and card1['value']==card5['value']:
        return True
    elif card3['value']==card5['value'] and card1['value']==card2['value'] and card1['value']==card4['value']:
        return True
    elif card4['value']==card5['value'] and card1['value']==card2['value'] and card1['value']==card3['value']:
        return True
    return False

def is_flush(card1,card2,card3,card4,card5):
    if is_straight_flush(card1,card2,card3,card4,card5):
        return False
    if card1['suit']==card2['suit'] and card1['suit']==card3['suit'] and card1['suit']==card4['suit'] and card1['suit']==card5['suit']:
        return True
    else:
        return False

def is_straight(card1,card2,card3,card4,card5):
    if is_straight_flush(card1,card2,card3,card4,card5):
        return False
    my_tuple=(card1['value'], card2['value'], card3['value'], card4['value'], card5['value'])
    sorted_tuple=sorted(my_tuple)
    if sorted_tuple[0]+1 == sorted_tuple[1] and sorted_tuple[1]+1 == sorted_tuple[2] and sorted_tuple[2]+1==sorted_tuple[3] and sorted_tuple[3]+1==sorted_tuple[4]:
        return True
    else:
        return False

def is_straight_flush(card1,card2,card3,card4,card5):
    if card1['suit']==card2['suit'] and card1['suit']==card3['suit'] and card1['suit']==card4['suit'] and card1['suit']==card5['suit']:
        my_tuple=(card1['value'], card2['value'], card3['value'], card4['value'], card5['value'])
        sorted_tuple=sorted(my_tuple)
        if sorted_tuple[0]+1 == sorted_tuple[1] and sorted_tuple[1]+1 == sorted_tuple[2] and sorted_tuple[2]+1==sorted_tuple[3] and sorted_tuple[3]+1==sorted_tuple[4]:
            return True
        else:
            return False
    else:
        return False

def main():
    deck = build_deck()
    shuffle(deck)
    
    print(deck[0]['face']+' of ' +deck[0]['suit'])
    print(deck[1]['face']+' of ' +deck[1]['suit']) 
    print(deck[2]['face']+' of ' +deck[2]['suit'])
    print(deck[3]['face']+' of ' +deck[3]['suit'])
    print(deck[4]['face']+' of ' +deck[4]['suit'])

    card1=deck[0]
    card2=deck[1]
    card3=deck[2]
    card4=deck[3]
    card5=deck[4]

    if is_high_card(card1,card2,card3,card4,card5):
        print('Result: High card')
    if is_pair(card1,card2,card3,card4,card5):
        print('Result: A pair')
    if is_2_pair(card1,card2,card3,card4,card5):
        print('Result: 2 pair')
    if is_3_of_a_kind(card1,card2,card3,card4,card5):
        print('Result: 3 of a kind')
    if is_4_of_a_kind(card1,card2,card3,card4,card5):
        print('Result: 4 of a kind')
    if is_full_house(card1,card2,card3,card4,card5):
        print('Result: Full house')
    if is_flush(card1,card2,card3,card4,card5):
        print('Result: Flush')
    if is_straight(card1,card2,card3,card4,card5):
        print('Result: Straight')
    if is_straight_flush(card1,card2,card3,card4,card5):
        print('Result: Straight flush')


if __name__ == '__main__':
    main()

