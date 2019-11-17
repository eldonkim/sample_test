#

import os
import sys

def search_dir( dirname ):
    try :
        filenames = os.listdir( dirname )
        for fname in filenames :
            full_name = os.path.join( dirname, fname)
            if os.path.isdir( full_name ) :
                search_dir(full_name)
            else :
                ext_name = os.path.splitext( full_name)[-1]
                if ext_name == '.py' :
                    print(full_name)
    except :
        print ('Can\'t access %s\n' % (dirname))


search_dir( sys.argv[1])
