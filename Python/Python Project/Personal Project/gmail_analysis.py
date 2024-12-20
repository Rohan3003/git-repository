import imaplib
import email
import yaml

import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt 
from email.header import decode_header

import numpy as np

username = 'rohanwatson44@gmail.com'
password = 'Rohan_s@3003'

imap_url = 'imap.gmail.com'
my_mail = imaplib.IMAP4_SSL(imap_url)
my_mail.login(username, password)