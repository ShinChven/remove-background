# RMBG - Remove Background CLI

RMBG is a command-line tool that removes the background from a person's photo using the `rembg` library.

## Features

- Remove background from photos or images
- Simple command-line interface
- Supports various image formats (JPEG, PNG, WebP, etc.)
- Option to force transparent background output in PNG or WebP format

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

To install the latest version directly from the GitHub repository, run:

```
pip install git+https://github.com/ShinChven/remove-background.git
```

This will install the `rmbg` command-line tool and all required dependencies.

## Upgrading

To upgrade RMBG to the latest version, you can use the following command:

```
pip install --upgrade git+https://github.com/ShinChven/remove-background.git
```

This will fetch and install the most recent version of RMBG from the GitHub repository.

## Usage

After installation, you can use the `rmbg` command to remove the background from images:

```
rmbg input_path [--force-transparent {png,webp}]
```

- `input_path`: Path to the input image or directory
- `--force-transparent`: (Optional) Force save with transparent background in specified format (png or webp)

### Examples

1. Remove background from a single image:

```
rmbg photos/image.jpg
```

This command will remove the background from `image.jpg` in the `photos` directory and save the result as `image_no_background.jpg` in the same directory.

2. Remove background and force transparent output in PNG format:

```
rmbg photos/image.jpg --force-transparent png
```

This command will remove the background from `image.jpg`, save the result as `image_no_background.png` with a transparent background.

3. Remove background and force transparent output in WebP format:

```
rmbg photos/image.jpg --force-transparent webp
```

This command will remove the background from `image.jpg`, save the result as `image_no_background.webp` with a transparent background.

4. Process all images in a directory:

```
rmbg photos/
```

This command will process all supported image files in the `photos` directory, removing backgrounds and saving the results with `_no_background` appended to the original filenames.

## Image Quality

- For PNG and WebP outputs (when using `--force-transparent`), the image quality is preserved as these are lossless formats.
- For JPEG outputs (when not using `--force-transparent`), the tool always uses the highest quality setting (95) to ensure the best possible output.

## Troubleshooting

If you encounter any issues, make sure that:

1. You have Python 3.7 or higher installed
2. All dependencies are correctly installed
3. The input image exists and is readable
4. You have write permissions for the output directory
5. Your Pillow installation supports WebP if you're using the WebP format

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

This tool uses the `rembg` library for background removal. Special thanks to the developers of `rembg` for their excellent work.