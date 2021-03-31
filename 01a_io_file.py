import argparse
import cv2

def parse_args(): 
    parser = argparse.ArgumentParser(description="Load image; save it")

    parser.add_argument('-i','--input', type=str,
        default='./input/',
        help='Directory path to the inputs folder. (default: %(default)s)')

    parser.add_argument('-o','--output', type=str,
        default='./output/',
        help='Directory path to the outputs folder. (default: %(default)s)')

    args = parser.parse_args()
    return args

def main():
	#load arguments from command line
	args = parse_args()

    #load image
	img = cv2.imread(args.input)

    #save image
	cv2.imwrite(args.output, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])



if __name__ == "__main__":
    main()