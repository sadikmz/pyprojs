def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n,max_n,unique_words)

nexted_tuple = ((0,"a"),(1,"b"),(2,"c"),(3,"d"),(4,"d"))

print(get_data(nexted_tuple))
