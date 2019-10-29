#!/usr/bin/env python
#
# created by everettjf 20191029
# https://everettjf.github.io
#
# generate chromium's trace event format json file from directory content file size
#
# Trace Event Format
# https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/preview#heading=h.yr4qxyxotyw
#

import os
from optparse import OptionParser


class LogWriter:
    def __init__(self, output_path):
        self.output_path = output_path

        if os.path.exists(self.output_path):
            os.remove(self.output_path)

        self.output = open(self.output_path, 'w')
        self.output.write('[\n')

    def append_line(self, line):
        self.output.write(line)
        self.output.write(',\n')

    def append_trace(self, name, phase, ts):
        line = '{{"name":"{}","cat":"cat","ph":"{}","pid":0,"tid":0,"ts":{}}}'.format(name, phase, ts)
        self.append_line(line)

    def append_file(self, filename, filesize, ts):
        self.append_file_without_prefix('F_' + filename, filesize, ts)

    def append_file_without_prefix(self, filename, filesize, ts):
        # file begin
        self.append_trace(filename, 'B', ts)
        # file end
        self.append_trace(filename, 'E', ts + filesize)

    def append_dir_begin(self, dirname, ts):
        self.append_trace('D_' + dirname, 'B', ts)

    def append_dir_end(self, dirname, ts):
        self.append_trace('D_' + dirname, 'E', ts)


def dirtrace(path, outputfile):
    log = LogWriter(outputfile)

    # [(dir_path, ending_flag)]
    pending_dirs = [(path, False)]

    timestamp = 0
    while len(pending_dirs) > 0:
        # always get the last item
        parent_dir, ending_flag = pending_dirs.pop()
        print('> ' + parent_dir)

        if ending_flag:
            # end flag
            log.append_dir_end(dir_name, timestamp)
            continue

        # set ending flag
        pending_dirs.append((parent_dir, True))

        # begin dir
        dir_name = parent_dir.split('/')[-1]
        log.append_dir_begin(dir_name, timestamp)

        # loop dir
        items = os.listdir(parent_dir)
        if len(items) == 0:
            # empty dir
            # empty placeholder
            log.append_file_without_prefix('/empty-directory/', 1, timestamp)
            timestamp += 1
            continue

        for file_name in items:
            cur_path = os.path.join(parent_dir, file_name)

            if os.path.isfile(cur_path):
                file_info = os.stat(cur_path)
                file_size = file_info.st_size

                # print('  {:<10} {}'.format(file_size, cur_path))
                log.append_file(file_name, file_size, timestamp)

                timestamp += file_size

            elif os.path.isdir(cur_path):
                # print('  dir ' + cur_path)
                pending_dirs.append((cur_path, False))


def main():
    p = OptionParser(
        '\n'
        '%prog -d <directory-path>\n'
        '%prog -d <directory-path> -o <output-json-path>\n'
        '\n'
        'This script generates chromium\'s trace event format json file from directory content file size.\n'
        'Visit https://github.com/everettjf/DirTrace for more information.'
        )

    p.add_option('-d', '--dir', dest='dir', help='which directory do you want to trace')
    p.add_option('-o', '--out', dest='out', help='output json path')

    (options, args) = p.parse_args()
    if options.dir is None:
        p.print_help()
        return

    output_path = os.path.join(os.getcwd(), 'trace.json')
    if options.out is not None:
        output_path = options.out

    # print(output_path)
    dir_path = options.dir

    if not os.path.exists(dir_path):
        print('directory not exist : {}'.format(dir_path))
        return

    if not os.path.isdir(dir_path):
        print('directory path is not a directory : {}'.format(dir_path))
        return

    if os.path.exists(output_path):
        os.unlink(output_path)

    if os.path.exists(output_path):
        print('output file existed, and can not remove it')
        return

    dirtrace(dir_path, output_path)

    print('done:)')


def test():
    # path = '/Users/everettjf/Desktop/test/case0'
    # path = '/Users/everettjf/Desktop/test/case1'
    # path = '/Users/everettjf/Desktop/test/case2'
    # path = '/Applications/Sublime Text.app'
    path = '/Applications/Xcode.app'

    outputfile = '/Users/everettjf/Desktop/trace.json'
    dirtrace(path, outputfile)


if __name__ == '__main__':
    main()
    # test()
