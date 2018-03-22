import sys
import os
import configparser

config = configparser.ConfigParser()
current_dir = os.getcwd().replace('\\WebChecker', '') + '\\WebChecker'    
config.read(current_dir + '\\config.ini')

def read_default():
    url = config['DEFAULT']['URL']
    out_dir = current_dir + config['DEFAULT']['OUT_DIR']
    log_dir = current_dir + config['DEFAULT']['LOG_DIR']
    return url, out_dir, log_dir

if __name__ == '__main__':
    commit = config['FLAG']['RUN_ON_COMMIT']
    push = config['FLAG']['SKIP_ON_PUSH']

    if len(sys.argv) > 1:
        if sys.argv[1] == 'commit':
            sys.exit(commit)
        else:
            sys.exit(push)
    else:
        sys.exit(commit)