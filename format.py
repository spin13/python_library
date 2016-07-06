#-*- coding: utf-8 -*-
# required "rarfile"
# # easy_install rarfile
#
import os
import imghdr
import zipfile
import rarfile


def _get_img_type(path):
    return imghdr.what(path)


def is_dir(path):
    return os.path.isdir(path)


def is_jpg(path):
    return True if _get_img_type(path) == "jpeg" else False


def is_png(path):
    return True if _get_img_type(path) == "png" else False


def is_bmp(path):
    return True if _get_img_type(path) == "bmp" else False


def is_zip(path):
    return zipfile.is_zipfile(path)


def is_rar(path):
    return rarfile.is_rarfile(path)

