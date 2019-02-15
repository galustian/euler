card_scores = {str(i):i for i in range(2, 10)}
card_scores['T'], card_scores['J'], card_scores['Q'], card_scores['K'], card_scores['A'] = 10, 11, 12, 13, 14
def card_scores_list(hand): return [card_scores[hand[i][0]] for i in range(5)]

def num_pairs(hand):
    highest, card_score = 0, 0
    for i in range(4):
        card_count = 0
        for j in range(i+1, 5):
            if hand[i][0] == hand[j][0]: card_count += 1
        if card_count == highest and highest > 0 and card_scores[hand[i][0]] > card_score:
            card_score = card_scores[hand[i][0]]
        if card_count > highest:
            highest = card_count
            card_score = card_scores[hand[i][0]] if card_scores[hand[i][0]] > card_score else card_score
    return highest, card_score
            
def pair(hand): return num_pairs(hand)[0] == 1, num_pairs(hand)[1]
def two_pairs(hand): return len(set(card_scores_list(hand))) == 3 and pair(hand)[0], num_pairs(hand)[1]
def three_of_a_kind(hand): return num_pairs(hand)[0] == 2, num_pairs(hand)[1]
def four_of_a_kind(hand): return num_pairs(hand)[0] == 3, num_pairs(hand)[1]
def full_house(hand): return len(set(card_scores_list(hand))) == 2 and three_of_a_kind(hand)[0], three_of_a_kind(hand)[1]

def straight(hand):
    sort = sorted(card_scores_list(hand))
    return sort == list(i for i in range(sort[0], sort[0]+5)), max(card_scores_list(hand))
def flush(hand):
    symbols = [hand[i][1] for i in range(4)]
    return len(set(symbols)) == 1, max(card_scores_list(hand))
def straight_flush(hand): return straight(hand)[0] and flush(hand)[0], max(card_scores_list(hand))
def royal_flush(hand): return straight_flush(hand)[0] and max(card_scores_list(hand)) == 14, 14

def hand_score(hand):
    if royal_flush(hand)[0]: return 9, royal_flush(hand)[1]
    if straight_flush(hand)[0]: return 8, straight_flush(hand)[1]
    if four_of_a_kind(hand)[0]: return 7, four_of_a_kind(hand)[1]
    if full_house(hand)[0]: return 6, full_house(hand)[1]
    if flush(hand)[0]: return 5, flush(hand)[1]
    if straight(hand)[0]: return 4, straight(hand)[1]
    if three_of_a_kind(hand)[0]: return 3, three_of_a_kind(hand)[1]
    if two_pairs(hand)[0]: return 2, two_pairs(hand)[1]
    if pair(hand)[0]: return 1, pair(hand)[1]
    return 0, max(card_scores_list(hand))

def largest_card_score(hand, ith_largest_card=0):
    return sorted(card_scores_list(hand), reverse=True)[ith_largest_card]

def winner(hand1, hand2):
    hand_score1, card_score1 = hand_score(hand1)
    hand_score2, card_score2 = hand_score(hand2)

    if hand_score1 > hand_score2: return True
    if hand_score1 < hand_score2: return False
    
    i = 0
    while card_score1 == card_score2:
        card_score1 += largest_card_score(hand1, ith_largest_card=i)
        card_score2 += largest_card_score(hand2, ith_largest_card=i)
        i += 1
    return card_score1 > card_score2  

def compute(player1_hands, player2_hands):
    player1_points = 0
    for i in range(len(player1_hands)):
        if winner(player1_hands[i], player2_hands[i]):
            player1_points += 1
    return player1_points

if __name__ == '__main__':
    with open('p054.txt') as f:
        player1_hands, player2_hands = [], []
        for line in f:
            cards = line.strip().split(' ')
            player1_hands.append(cards[:5])
            player2_hands.append(cards[5:])
    
    print(compute(player1_hands, player2_hands))
