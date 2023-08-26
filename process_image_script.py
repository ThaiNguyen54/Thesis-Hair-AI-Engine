import subprocess
import os
import shutil


aligned_face_output_dir = './input/face'
unprocessed_dir = './unprocessed'
input_style_your_hair_dir = '../StyleYourHair/ffhq_image'

arguments = ['-output_dir', './ffhq_image']
command = ['python', './align_face.py']

process = subprocess.Popen(command)
process.wait()
stdout, stderr = process.communicate()

if process.returncode == 0:
    for filename in os.listdir(unprocessed_dir):
        f = os.path.join(unprocessed_dir, filename)
        if os.path.isfile(f):
            print(f)
            os.remove(f)
else:
    print('error: ', stderr.decode())