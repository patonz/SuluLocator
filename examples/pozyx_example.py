import sys
sys.path.append("..")  # Adds the parent directory to Python's search path.

from modules.pozyx_wrapper import PozyxWrapper

ANCHORS = [0x1174, 0x117D, 0x1222, 0x1136]

def print_distance(anchor, distance):
    print(f"Distance to anchor {anchor:0x} is {distance} mm.")

def main():
    wrapper = PozyxWrapper(anchors=ANCHORS, callback=print_distance)
    wrapper.start()

if __name__ == "__main__":
    main()
