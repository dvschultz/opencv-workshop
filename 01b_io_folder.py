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

    args = parser.parse_args()
    return args

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
        files = os.listdir(args.input)

        #loop thru all files in folder
        for file in files:
            #load file
            img = cv2.imread(os.path.join(args.input,file))  

            #save file
            if hasattr(img, 'copy'):
                out_path = os.path.join(args.output,file)
                save_image(img, out_path, file, args.file_extension)
    else:
        #process image
        img = cv2.imread(args.input)
        save_image(img, out_path, file, args.file_extension)



if __name__ == "__main__":
    main()