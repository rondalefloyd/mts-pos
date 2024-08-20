from PyQt5.QtGui import *
from PyQt5.QtCore import *

def tinValidator():
    return QRegExpValidator(QRegExp(r'^\d{50}$'))

def mobileNumberValidator():
    return QRegExpValidator(QRegExp(r'^\d{11}$'))

def quantityFormatValidator():
    return QIntValidator(0, 999999999)

def billFormatValidator():
    return QDoubleValidator(0, 999999999, 2)

def addressFormatValidator():
    return QRegExpValidator(QRegExp(r'^[A-Za-z\s]+,\s[A-Za-z\s]+,\s[A-Za-z\s]+$'))

def nonSpaceTextFormatValidator():
    return QRegExpValidator(QRegExp(r'^[A-Za-z]+$'))

def withSpaceTextFormatValidator():
    return QRegExpValidator(QRegExp(r'^[A-Za-z ]+$'))

def fullNameValidator():
    return QRegExpValidator(QRegExp(r'^[A-Za-z]+, [A-Za-z]\., [A-Za-z]+$'))

def nonSpaceTextWithDigitFormatValidator():
    return QRegExpValidator(QRegExp(r'^[A-Za-z0-9-]+$'))

def withSpaceTextWithDigitFormatValidator():
    return QRegExpValidator(QRegExp(r'^[A-Za-z0-9 -]+$'))

QRegExp(r'^[A-Za-z]+$')