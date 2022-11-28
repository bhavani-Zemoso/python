import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    parser.add_argument("-x", "--execute", action="store", required=True, help="Value for execute")
    parser.add_argument("-y", help="Value for y", default=False)
    parser.add_argument("-z", help="Value for z", type=int)

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", help="Value for a", default="Hello")
    group.add_argument("-b", help="Value for b")
    return parser.parse_args()

if __name__ == '__main__':
    print(get_args())