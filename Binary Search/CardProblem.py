
def located_cards(cards, query):
    lo, hi = 0, len(cards)-1
    
    while lo <= hi:
        mid = (lo + hi ) // 2
        mid_val = cards[mid]
        
        if mid_val == query:
            return mid
        
        if query < mid_val:
            lo = mid + 1
        else:
            hi = mid -1
            
    return -1
            
    


if __name__ == "__main__":
    cards = [9,7,5,4,3,2,1]
    query = 5
    output = 1
    result = located_cards(cards, query) == output
    print(result)
    