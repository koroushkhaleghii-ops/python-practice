# Exercise 21: Check if two strings are isomorphic
# Example: "egg" and "add" -> True, "foo" and "bar" -> False

def is_isomorphic_mapping(s, t):
    if len(s) != len(t):
        return False
    map_s_to_t = {}
    map_t_to_s = {}
    for ch_s, ch_t in zip(s, t):
        if ch_s in map_s_to_t:
            if map_s_to_t[ch_s] != ch_t:
                return False
        else:
            map_s_to_t[ch_s] = ch_t
        if ch_t in map_t_to_s:
            if map_t_to_s[ch_t] != ch_s:
                return False
        else:
            map_t_to_s[ch_t] = ch_s
    return True

def is_isomorphic_zip(s, t):
    if len(s) != len(t):
        return False
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

# Example
test1_s, test1_t = "egg", "add"
test2_s, test2_t = "foo", "bar"
test3_s, test3_t = "paper", "title"
print(f"'{test1_s}' and '{test1_t}': {is_isomorphic_mapping(test1_s, test1_t)}")
print(f"'{test2_s}' and '{test2_t}': {is_isomorphic_mapping(test2_s, test2_t)}")
print(f"'{test3_s}' and '{test3_t}': {is_isomorphic_zip(test3_s, test3_t)}")