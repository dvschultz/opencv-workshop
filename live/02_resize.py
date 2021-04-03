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


    args = parser.parse_args()
    return args

def save_image(img,path,filename,ext):
    if(ext == "png"):
        new_file = os.path.splitext(filename)[0] + ".png"
        cv2.imwrite(os.path.join(path, new_file), img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    elif(ext == "jpg"):
        new_file = os.path.splitext(filename)[0] + ".jpg"
        cv2.imwrite(os.path.join(path, new_file), img, [cv2.IMWRITE_JPEG_QUALITY, 95])

def resize(img, filename, args):
    scale = .5
    # do the resize function
    (h,w) = img.shape[:2]

    img = cv2.resize(img, (int(w*scale), int(h*scale)), interpolation = cv2.INTER_CUBIC)

    save_image(img, args.output, filename, args.file_extension)

def crop(img, filename, args):
    patch = 1200
    (h,w) = img.shape[:2]
    center_x = int(w/2)
    center_y = int(h/2)
    start_x = int(center_x - (patch/2))
    end_x = int(start_x + patch)
    start_y = int(center_y - (patch/2))
    end_y = int(start_y + patch)

    #crop
    crop = img[start_y:end_y, start_x:end_x]

    save_image(crop, args.output, filename, args.file_extension)

def pad(img, filename, args):
    #define some border constants
    border_type = cv2.BORDER_REPLICATE # stretch edges
    # border_type = cv2.BORDER_CONSTANT # solid color (color is BGR!)
    # border_type = cv2.BORDER_REFLECT # reflect edge

    c = [0,255,0] # define a color !! IN BGR !!

    padded_img = cv2.copyMakeBorder(img,100,100,100,100,border_type,value=c)

    save_image(padded_img, args.output, filename, args.file_extension)

def process(img, filename, args):
    if(args.process=='resize'):
        resize(img, filename, args)
    elif(args.process=='crop'):
        crop(img, filename, args)
    elif(args.process=='pad'):
        pad(img, filename, args)

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
                process(img, file, args)

                # save_image(img, out_path, file, args.file_extension)
    else:
        #process image
        img = cv2.imread(args.input)
        save_image(img, args.ouput, file, args.file_extension)



if __name__ == "__main__":
    main()