import os
import argparse
import cv2

def parse_args(): 
    parser = argparse.ArgumentParser(description="Load image; save it")

    parser.add_argument('-i','--input', type=str,
        default='./input/',
        help='Directory path to the input(s). (default: %(default)s)')

    parser.add_argument('-o','--output', type=str,
        default='./output/',
        help='Directory path to the output name or folder. (default: %(default)s)')

    parser.add_argument('-f','--file_extension', type=str,
        default='png',
        help='png or jpg (default: %(default)s)')

    parser.add_argument('-p','--process', type=str,
        default='resize',
        help='resize, crop, or pad (default: %(default)s)')

    parser.add_argument('--scale', type=float,
        default=1.0,
        help='multiplier for resize (default: %(default)s)')

    args = parser.parse_args()
    return args

def process(img, filename, args):
    if args.process=='resize':
        resize(img, filename, args)

def resize(img, filename, args):
    (h, w) = img.shape[:2]
    resized = cv2.resize(img, (int(w*args.scale),int(h*args.scale)), interpolation = cv2.INTER_CUBIC)
    save_image(resized, args.output, filename, args.file_extension)

def save_image(img,path,filename,ext):
    if(ext == "png"):
        new_file = os.path.splitext(filename)[0] + ".png"
        cv2.imwrite(os.path.join(path, new_file), img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    elif(ext == "jpg"):
        new_file = os.path.splitext(filename)[0] + ".jpg"
        cv2.imwrite(os.path.join(path, new_file), img, [cv2.IMWRITE_JPEG_QUALITY, 95])


def main():
    # load arguments from command line
    args = parse_args()

    # make sure output folder exists, otherwise saving won’t work
    if not os.path.exists(args.output):
        os.makedirs(args.output)



    # check if input path is a folder or a single image
    if os.path.isdir(args.input):
        #process folder
        for root, subdirs, files in os.walk(args.input):
        
            #loop thru all files in folder
            for file in files:
                #load file
                img = cv2.imread(os.path.join(args.input,file))  

                #save file
                if hasattr(img, 'copy'):
                    process(img, os.path.splitext(file)[0], args)

    else:
        #process image
        img = cv2.imread(args.input)

        if hasattr(img, 'copy'):
            process(img, os.path.splitext(args.input)[0], args)



if __name__ == "__main__":
    main()