import sys
import subprocess

image_path = sys.argv[1]

# Run pose estimation script
coordinates, dimension = pose_est(image_path)

# Extract the patch and save as patch_1.jpg and patch_2.jpg
patch_extract(image_path, coordinates, dimension)

cluster = GMMClust(coordinates, dimension)

# Running YOLO
percentage = 0

cmd1 = "./yolo.sh images/patch_1.jpeg"
cmd2 = "./yolo.sh processed/patch_2.jpg"
p = subprocess.check_output(cmd1, shell=True)
temp = p.find("cell phone: ")

if temp != -1:
    temp += 12
    p = p[temp:]
    temp = p.find("%")
    p = p[0:temp]
    percentage = int(p)

if percentage == 0:
    print("Mobile Device not found in the image")
else:
    print("Mobile device found with an accuracy of "+str(percentage)+"%")

