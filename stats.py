def word_count(book):
    count = book.split()
    return len(count)

def char_count(book):
    result = {}
    for char in book:
        if char.lower() in result:
            result[char.lower()] += 1
        else:
            result[char.lower()] = 1
    return result

def sort_list(dictionary):
    def sort_on(item):
        return item["num"]
    result = []
    for char, num in dictionary.items():
        if char.isalpha():
            dict = {"char": char, "num": num}
            result.append({"char": char, "num": num})
    result.sort(reverse=True, key=sort_on)
    return result

