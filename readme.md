# EXIF Editor for Film Photography

## Installation
* Dependencies
  * Python
  * piexif
    ```
    pip install piexif
    ```
  * PIL
    ```
    pip install Pillow
    ```

* Download the tool
  ```
  git clone https://github.com/AR0EN/film-exif.git
  ```

## Usage
* Step 1: customize input configuration in film_exif.py
  * Paths to input photos' directory, and output directory
  ```
  IPHOTOS_DIR = <Path to input photos' directory>
  OPHOTOS_DIR = <Path to output directory>
  ```
  * EXIF information in ImageIFDCustomized and ExifIFDCustomized

* Step 2: execute the script
  ```
  python film_exif.py
  ```
  Output photos with updated EXIF are saved into OPHOTOS_DIR

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
