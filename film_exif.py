# References
# [Exchangeable Image File Format] | (http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf)
# [Piexif] | (https://github.com/hMatoba/Piexif)

# Import
import os
import sys
import copy

import piexif as pxf
from PIL import Image

# Constants
TAG = 'Film Exif Utility'
IPHOTOS_DIR = 'input'   # Path to input photos' directory
OPHOTOS_DIR = 'output'  # Path to output directory
IPHOTO_EXTS = ['.jpg', '.JPG', '.png', '.PNG']
OPHOTO_EXT = '.jpg'

AUTHOR = u'Le Huy Hoang'
CAMERA_MANUFACTURER = u'Kyocera Japan'
CAMERA_MODEL = u'Contax S2 Titanium 60 Years Limited'
CAMERA_SERIAL = u'003643'
LENS_MODEL = u'Carl Zeiss Planar 1,4/50 T* (C/Y)'
LENS_SERIAL = u'9552246'
LENS_FOCAL_LENGTH = 50
LENS_FOCAL_LENGTH_35MM = 50
FILM = u'Kodak Ultramax 400'

ImageIFDCustomized = {
    pxf.ImageIFD.Make:u'Kyocera Japan',
    pxf.ImageIFD.Model:u'Contax S2 Titanium 60 Years Limited',
    pxf.ImageIFD.ImageDescription:u'Kodak Ultramax 400',
}

ExifIFDCustomized = {
    pxf.ExifIFD.BodySerialNumber:u'003643',
    pxf.ExifIFD.CameraOwnerName:u'Le Huy Hoang',    
    pxf.ExifIFD.LensMake:u'Kyocera Japan',
    pxf.ExifIFD.LensModel:u'Carl Zeiss Planar 1,4/50 T* (C/Y)',
    pxf.ExifIFD.LensSerialNumber:u'9552246',
    pxf.ExifIFD.FocalLength:[5000, 100],
    pxf.ExifIFD.FocalLengthIn35mmFilm:50,
}

ExifCustomized = []
ExifCustomized.append(['0th', ImageIFDCustomized])
ExifCustomized.append(['Exif', ExifIFDCustomized])

# Local functions
def log(msg, tag = None, f = sys.stdout):
    if tag is not None:
        text = '[{0:s}] {1:s}\n'.format(tag, msg)
    else:
        text = '{0:s}\n'.format(msg)

    f.write(text)

def logErr(msg, tag = None):
    log(msg, f = sys.stderr)

def getFileExtension(filePath):
    ext = None
    if filePath is not None:
        SEPARATOR = '.'

        fileName = os.path.basename(filePath)
        _ext = '{0:s}{1:s}'.format('.', fileName.split(SEPARATOR)[-1])
        if(_ext in filePath):
            ext = _ext
        else:
            ext = None
    else:
        ext = None
    
    return ext

def dumpExif(photo):
    exif = pxf.load(photo)
    for ifd in ("0th", "Exif", "GPS", "1st"):
        for tag in exif[ifd]:
            print(ifd, pxf.TAGS[ifd][tag]["name"], exif[ifd][tag])

def updateExif(iPhotoPath):
    # Load photo and original Exif
    imgData = Image.open(iPhotoPath)
    exifOrg = pxf.load(imgData.info["exif"])

    # Clone Exif
    exifNew = copy.deepcopy(exifOrg)

    # Update Exif
    for ifd in ExifCustomized:
        for etag in ifd[1]:
            exifNew[ifd[0]][etag] = ifd[1][etag]

    photoName = os.path.basename(iPhotoPath)
    oPhotoPath = '{0:s}/{1:s}'.format(OPHOTOS_DIR, photoName)
    imgData.save(oPhotoPath, exif=pxf.dump(exifNew))

def main():
    # Scan through all images
    for f in os.listdir(IPHOTOS_DIR):
        fullPath = '{0:s}/{1:s}'.format(IPHOTOS_DIR, f)
        log('{0:s}'.format(fullPath), TAG)
        ext = getFileExtension(f)
        if ((ext is not None) and (ext in IPHOTO_EXTS)):
            updateExif(fullPath)

if __name__ == "__main__":
    main()
