text="ABBABBC"

def get_count(ch):
    
    return text.count(ch)

most_frequent_char=max(text,key=get_count)

print(most_frequent_char)

min_frequent_char=min(text,key=get_count)

print(min_frequent_char)