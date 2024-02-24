import sys
import argparse


def main():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="YouTube Downloder"
    )

    parser.add_argument('-u', '--url', help="YouTube Video DOwnloader")
    parser.add_argument('-q', '--quality', help="YouTube Video Quality", default="highest")
    parser.add_argument('-d', '--delay', help='Delay Between Downloads', type=int, default=0)
    

    arg = parser.parse_args()
    print(arg)