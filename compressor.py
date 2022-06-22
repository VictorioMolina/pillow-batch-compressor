"""
Easy image compressor w/ Pillow.

@description Recursivelly compresses all the images in a given folder.
@author <https://github.com/VictorioMolina>
@license MIT
"""

import os
import sys
from PIL import Image

"""
Compress an image applying the given quality.
"""
def compress_image(image_path, compressed_image_path, quality, scale_factor):
    print(f'> Compressing {image_path}...');
    picture = Image.open(image_path);
    
    # RGB
    rgb_picture = picture.convert('RGB');

    # Save a resized version as .jpg, temporally, as .png is a lossless format
    tmp_path = '/tmp/tmp_compressed_image.jpg';
    width, height = rgb_picture.size;
    new_dimensions = (int(width*scale_factor), int(height*scale_factor));
    rgb_picture.resize(new_dimensions, Image.LANCZOS).save(tmp_path, optimize=True, quality=quality);
    
    # Get the size in Bytes of the original file before replacing
    original_image_size = os.path.getsize(image_path);
        
    # Convert the temporal image to the correct format and remove it!
    tmp_picture = Image.open(tmp_path);
    tmp_picture.save(compressed_image_path);
    os.remove(tmp_path);
    
    # Get the size of the new image too
    compressed_image_size = os.path.getsize(compressed_image_path);
    
    # Compression difference
    saving_diff = compressed_image_size - original_image_size;
    print(f'[+] Image size change: {saving_diff/original_image_size*100:.2f}% of the original image size.');
    
  
"""
> python3 compressor.py images_dir quality scale_factor should_replace
"""
def main():
    # Read args
    images_dir = sys.argv[1];
    quality = int(sys.argv[2]);
    scale_factor = float(sys.argv[3]);
    should_replace = sys.argv[4].lower() == 'true';
    
    
    # Supported extensions
    supported_extensions = ['.jpg', '.jpeg', '.png'];

    # Get the current directory
    cwd = os.getcwd();

    # Get the non relative path of the images directory
    images_dir = cwd + '/' + images_dir;

    for filename in os.listdir(images_dir):
        image_path = images_dir + '/' + filename;
        name, extension = os.path.splitext(filename);

        # Compress supported images
        if extension in supported_extensions:
            if (not should_replace):
                out_path = f'{images_dir}/compressed_{filename}';
            else:
                out_path = f'{images_dir}/{filename}';

            compress_image(image_path, out_path, quality, scale_factor);


if (__name__ == '__main__'):
    main();
