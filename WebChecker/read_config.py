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
    if len(sys.argv) > 1:
        if sys.argv[1] == 'commit':
            commit = config['FLAG']['RUN_ON_COMMIT']
            sys.exit(commit)
        elif sys.argv[1] == 'push':
            push = config['FLAG']['SKIP_ON_PUSH']
            sys.exit(push)
        elif sys.argv[1] == 'production':
            push = config['ENV']['PRODUCTION']
            sys.exit(push)
        elif sys.argv[1] == 'uat':
            push = config['ENV']['UAT']
            sys.exit(push)
        else:
            sys.exit("1")
    else:
        sys.exit("1")