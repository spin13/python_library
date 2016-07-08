

# sort list "l" by key_index "k"
# 
def sort_by_key(l, k):
    return sorted(l, key=lambda x: x[k])

# sort string list order by descending
def sort_desc_str(l):
    return sorted(l, reverse=True)

# sort string list order by ascending
def sort_asc_str(l):
    return sorted(l)

# sort integer list order by descending
def sort_desc_int(l):
    return sorted(l, reverse=True, key=int)

# sort integer list order by ascending
def sort_asc_int(l):
    return sorted(l, key=int)


