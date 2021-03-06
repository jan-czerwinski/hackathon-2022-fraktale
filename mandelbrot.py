import argparse
from utils import (read_image)

def main():
    print('Script started')
    parser = argparse.ArgumentParser(description='CLI argument processing')
    parser.add_argument('--image_path', required=True, help='Path to image that is meant to be processed')
    parser.add_argument('--save_path', required=True, help='Path to save filtered image')
    args = parser.parse_args()

    print('Reading image')
    img = read_image(args.image_path)
    print(f'Read image with shape{img.shape}')

if __name__ == '__main__':
    main()