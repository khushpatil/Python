def remove_none_values(dict):
    for key in dict.copy():
        if dict[key] == None:
            del dict[key]
    return dict

def sort_pages(dict):
    arr = []
    for element in dict:
        arr.append((element, dict[element]))
    arr.sort()
    return arr

def print_report(pages):
    pages = remove_none_values(pages)
    pages_list = sort_pages(pages)
    for page in pages_list:
        url = page[0]
        count = page[1]
        print(f"Found {count} internal links to {url}")