import sys
import read_config
import pickle
import glob
import os
import datetime
from collections import Counter

try:
    from lib.pylinkvalidator.api import crawl_with_options
except ModuleNotFoundError:
    # get depedency
    import pip
    pip.main(['install', 'beautifulsoup4'])
    from lib.pylinkvalidator.api import crawl_with_options

if __name__ == '__main__':
    # configs
    url, out_dir, log_dir = read_config.read_default()
    
    # check wether the dir is exist, if not create it
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    format_unknown = lambda val, is_status: val if (val if is_status else val.status) is not None else 1
    
    # new crawled data
    crawled_site = crawl_with_options([url], {"workers": 5, 'ignore-bad-tel-urls': True})
    error_pages = crawled_site.error_pages
    new_counted_errors = Counter({str(format_unknown(val,False)) : format_unknown(val.status, True) for _, val in error_pages.items()})    
    
    git_error_status = 0 # no error
    out_results = glob.glob(out_dir+'\\*.pkl') # *.pkl means all .pkl files of old result    
    if len(out_results) > 0: # if any before result
        latest_file_addr = max(out_results, key=os.path.getctime)
        with open(latest_file_addr, "rb" ) as latest_file_object:
            last_result = pickle.load(latest_file_object)
            last_counted_errors = Counter({str(format_unknown(val,False)) : format_unknown(val.status, True) for _, val in last_result.items()})            
            
            # compare result
            diff = new_counted_errors - last_counted_errors
            if len(diff) > 0:
                print('---------Error Page Diff---------')
                for key, val in diff.items():
                    print(key, val)
                print('---------------------------------')
                git_error_status = 1 # has error, cancel push

    # save new result
    current_date = str(datetime.datetime.now()).replace(':', '-')
    new_file_addr = out_dir + current_date + '.pkl'
    with open(new_file_addr, "wb" ) as new_file_object:
        pickle.dump(error_pages, new_file_object)

    # logs error to csv
    new_log_addr = log_dir + current_date + '.csv'
    with open(new_log_addr, "w" ) as file_log:
        title = 'resource,status'
        print(title, file=file_log)
        for resource, status in new_counted_errors.items():
            source = str(resource).replace("\n", "").replace("Resource ", "")
            data = '{:s},{:s}'.format(source if status != '1' else 'Unknown', str(status) if status != 1 else 'Unknown')
            print(data, file=file_log)
    
    # git error status
    sys.exit(git_error_status)