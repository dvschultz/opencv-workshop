import os
import cv2
import argparse

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

def save_image(img, path, filename, ext):
    if(ext == "png"):
        new_file = os.path.splitext(filename)[0] + ".png"
        cv2.imwrite(os.path.join(path, new_file), img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    elif(ext == "jpg"):
        new_file = os.path.splitext(filename)[0] + ".jpg"
        cv2.imwrite(os.path.join(path, new_file), img, [cv2.IMWRITE_JPEG_QUALITY, 95])

def main():
	args = parse_args()

	if os.path.isdir(args.input):
		files = os.listdir(args.input)

		for file in files:
			# print(os.path.join(args.input, file))
			img_data = cv2.imread(os.path.join(args.input, file))

			save_image(img_data, args.output, file, 'png')
	else:
		img_data = cv2.imread(args.input)
		name = args.input.split('/')[-1]
		save_image(img_data, args.output, name, 'jpg')

if __name__ == "__main__":
	main()











