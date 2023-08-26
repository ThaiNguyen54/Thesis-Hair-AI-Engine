import subprocess
import os
import shutil
import argparse

parser = argparse.ArgumentParser(description='generate_hair')
parser.add_argument('--image_name', type=str)
parser.add_argument('--hairstyle_name', type=str)
args = parser.parse_args()

command = ['python', './main.py', '--input_dir', './ffhq_image/', '--im_path1', str(args.image_name), '--im_path2',
           str(args.hairstyle_name), '--output_dir', './style_your_hair_output', '--warp_loss_with_prev_list',
           'delta_w', 'style_hair_slic_large', '--save_all', '--version', 'final', '--W_steps', '450', '--FS_steps', '50',
           '--align_steps1', '50', '--align_steps2', '25', '--warp_steps', '100']
try:
    process = subprocess.Popen(command)
    for line in process.stdout:
        print(line)
    process.communicate()
except subprocess.CalledProcessError as e:
    print(e)
# process.wait()
# stdout, stderr = process.communicate()

if process.returncode == 0:
    print('finish')
else:
    print('error')
