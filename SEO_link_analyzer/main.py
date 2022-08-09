import sys
from crawl import crawl_page
from report import print_report
def main():
    sys.setrecursionlimit(1500)
    if len(sys.argv) == 2:
        print(sys.argv[1])
        base_url = sys.argv[1]
        dict = {}
        dict = crawl_page(base_url, base_url, dict)
        print(dict)
        print_report(dict)
    else:
        exit(1)

if __name__ == "__main__":
    main()