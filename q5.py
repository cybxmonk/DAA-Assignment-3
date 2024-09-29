def find_content_children(g, s):
    g.sort()
    s.sort()

    child_index = 0
    cookie_index = 0

    while child_index < len(g) and cookie_index < len(s):
        if s[cookie_index] >= g[child_index]:
            child_index += 1
        cookie_index += 1

    return child_index

# Example usage
if __name__ == "__main__":
    g = [1, 2, 3]  # greed factors of children
    s = [1, 1]     # sizes of cookies

    result = find_content_children(g, s)
    print("Number of content children:", result)
