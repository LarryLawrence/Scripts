__author__ = 'zhenfei.mzf@alibaba-inc.com'

import os
import sys

def help():
    print 'Usage:  get_linux_version.py [zImage FILE]\n'
    exit()

def main(argv):
    if len(argv)!=2:
        help()

    if os.path.exists(argv[1]):
        vmlinux = open(argv[1],'rb').read()
        linux_banner_file_offset = vmlinux.find('Linux version ')

        name = ''
        if linux_banner_file_offset:
            print '[+]linux_banner_file_offset: 0x%x' % linux_banner_file_offset

            while ord(vmlinux[linux_banner_file_offset]):
                name += '%c' % ord(vmlinux[linux_banner_file_offset])
                linux_banner_file_offset += 1

            print '[+]version: %s' % name

        else:
            print '[!]get linux_banner_file_offset error'
    else:
        print '[!]zImage file does not exist...'


if __name__ == '__main__':
    main(sys.argv)
