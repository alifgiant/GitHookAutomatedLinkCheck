import sys
import configparser
import pickle
import glob
import os
import datetime
from collections import Counter
from pylinkvalidator.api import crawl_with_options

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(os.getcwd() + '\config.ini')
    
    url = config['DEFAULT']['URL']
    out_dir = os.getcwd() + config['DEFAULT']['OUT_DIR']
    log_dir = os.getcwd() + config['DEFAULT']['LOG_DIR']

    addr_1 = out_dir + '2018-03-21 11-22-59.879077.pkl'
    addr_2 = out_dir + '2018-03-21 11-37-50.879244.pkl'
    result_1 = pickle.load(open(addr_1, "rb" ))
    result_2 = pickle.load(open(addr_2, "rb" ))
    
    format_unknown = lambda val, is_status: val if (val if is_status else val.status) is not None else 1

    count_1 = Counter({str(format_unknown(val,False)) : format_unknown(val.status, True) for _, val in result_1.items()})
    count_2 = Counter({str(format_unknown(val,False)) : format_unknown(val.status, True) for _, val in result_2.items()})

    pass
