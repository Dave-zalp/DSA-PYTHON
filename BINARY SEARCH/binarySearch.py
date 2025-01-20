def locate_cards(cards, query):

    position = 0

    while position < len(cards):

        if cards[position] == query:
            return position

        # Increment the position
        position += 1

    return -1



def remove_repeat_nums(cards):
    seen = set()
    new_list = []
    for i in cards:
        if i not in seen:
            new_list.append(i)
            seen.add(i)
    return new_list


new_cards = remove_repeat_nums([-10, -5, 0, 3, 7, 9, 12, 18])

print(locate_cards(new_cards, 7))
