import cv2
import os
import time
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("-f", "--file",             help="the name of the video to extract.", required=True)
parser.add_argument("-r", "--framereduction",   help="how many frames should be skipped between captures.", default=1)
parser.add_argument("-o", "--output",           help="output folder name.")
parser.add_argument("-s", "--start",            help="start from a specific frame.", default=0)
parser.add_argument("-e", "--end",              help="stop at a specific frame.", default=0)


args=parser.parse_args()

timestamp = int(time.time())
out_folder = args.file + "_" +str(timestamp)

if args.output:
    out_folder = out_folder

if args.file == None:
    print("usage: python extract_frames.py --file video1.mp4 -output video1_frames_out")

print(f"extracting frames from : {args.file}\nevery: {args.framereduction} frame(s)\nto location: {out_folder}")

if not os.path.exists(out_folder):
    os.makedirs(out_folder)
currentframe = 0
frame_counter = int(args.framereduction)
cam = cv2.VideoCapture(args.file)
try:
    while(True):
        # print({"currentframe": currentframe, "frame_counter": frame_counter, "start": args.start, "end": args.end})
        ret,frame = cam.read()
        if ret:
            if int(args.end) != 0 and currentframe >= int(args.end):
                break
            if currentframe >= int(args.start):
                if currentframe == 0 or frame_counter <= 1:
                    frame_counter = int(args.framereduction)
                    name = out_folder + '/(' + str(currentframe) + ').jpg'
                    cv2.imwrite(name, frame)
                else:
                    frame_counter -= 1
            currentframe += 1
        else:
            break
            
    cam.release()
    cv2.destroyAllWindows()

except KeyboardInterrupt:
    print("\nCTRL+C pressed ...")
    print("Shutting Down...")
    cam.release()
    cv2.destroyAllWindows()
    os._exit(1)

cam.release()
cv2.destroyAllWindows()