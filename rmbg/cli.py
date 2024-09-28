import argparse
import os
import glob
from rembg import remove
from PIL import Image, features
import sys

def check_webp_support():
    if not features.check('webp'):
        print("Warning: WebP support is not available in your Pillow installation.", file=sys.stderr)
        print("WebP files will be skipped.", file=sys.stderr)
        return False
    return True

def get_output_image(image, output_path, force_transparent):
    if force_transparent:
        # If force_transparent is set, always return the image as is (with transparency)
        return image
    # If output is JPEG, convert RGBA to RGB
    if output_path.lower().endswith(('.jpg', '.jpeg')):
        if image.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
            return background
        return image.convert('RGB')
    # For other formats (including WebP), return as is to preserve transparency
    return image

def process_single_image(input_path, force_transparent):
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        
        # Generate the output filename
        input_filename = os.path.basename(input_path)
        filename, ext = os.path.splitext(input_filename)
        if force_transparent:
            ext = f'.{force_transparent.lower()}'  # Use the specified transparent format
        output_filename = f"{filename}_no_background{ext}"
        output_path = os.path.join(os.path.dirname(input_path), output_filename)
        
        # Prepare the image for saving
        final_image = get_output_image(output_image, output_path, force_transparent)
        
        # Save the image with the highest quality (95) for JPEG
        if output_path.lower().endswith(('.jpg', '.jpeg')):
            final_image.save(output_path, quality=95)
        else:
            final_image.save(output_path)
        
        print(f"Background removed successfully. Output saved to {output_path}")
    except IOError as e:
        print(f"IOError processing {input_path}: {str(e)}", file=sys.stderr)
    except ValueError as e:
        print(f"ValueError processing {input_path}: {str(e)}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error processing {input_path}: {str(e)}", file=sys.stderr)

def remove_background(input_path, force_transparent):
    webp_supported = check_webp_support()
    if os.path.isdir(input_path):
        # Process all images in the directory
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
        if webp_supported:
            image_extensions.append('.webp')
        for ext in image_extensions:
            for image_path in glob.glob(os.path.join(input_path, f'*{ext}')):
                process_single_image(image_path, force_transparent)
    elif os.path.isfile(input_path):
        # Process single image
        _, ext = os.path.splitext(input_path)
        if ext.lower() == '.webp' and not webp_supported:
            print(f"Skipping WebP file {input_path} due to lack of WebP support.", file=sys.stderr)
        else:
            process_single_image(input_path, force_transparent)
    else:
        print(f"Error: {input_path} is not a valid file or directory", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Remove background from people's images")
    parser.add_argument("input", help="Path to the input image or directory")
    parser.add_argument("--force-transparent", choices=['png', 'webp'], help="Force save with transparent background in specified format (png or webp)")
    args = parser.parse_args()

    remove_background(args.input, args.force_transparent)

if __name__ == "__main__":
    main()