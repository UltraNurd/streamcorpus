#!/usr/bin/env python
'''
A command line utility for printing out information from
streamcorpus.Chunk files.

This software is released under an MIT/X11 open source license.

Copyright 2012 Diffeo, Inc.
'''

import os
import sys
from ._chunk import Chunk

def _dump(fpath, args):
    '''
    Reads in a streamcorpus.Chunk file and prints the metadata of each
    StreamItem to stdout
    '''
    if args.count:
        num_stream_items = 0
        num_labeled_stream_items = set()

    for si in Chunk(path=fpath, mode='rb'):
        if args.count:
            num_stream_items += 1
            if not args.labels_only:
                continue

        if args.labels_only:
            if si.body.sentences:
                for tagger_id in si.body.sentences:
                    for sent in si.body.sentences[tagger_id]:
                        if args.count and si.stream_id in num_labeled_stream_items:
                            break
                        for tok in sent.tokens:
                            if tok.labels:
                                if args.count:
                                    num_labeled_stream_items.add(si.stream_id)
                                    break
                                else:
                                    print tok.token, tok.labels

        elif not args.show_all:
            si.body = None
            if si.other_content:
                for oc in si.other_content:
                    si.other_content[oc] = None

        elif args.show_content_field and si.body:
            
            print getattr(si.body, args.show_content_field)

        else:
            print si

    if args.count:
        print '%d\t%d\t%s' % (num_stream_items, len(num_labeled_stream_items), fpath)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input_path', 
        help='Path to a single chunk file, or directory of chunks, or "-" for receiving paths over stdin')
    parser.add_argument('--show-all', action='store_true', 
                        default=False, dest='show_all')
    parser.add_argument('--show-content-field', 
                        default=None, dest='show_content_field')
    parser.add_argument('--count', action='store_true', 
                        default=False, help='print number of StreamItems')
    parser.add_argument('--labels-only', action='store_true', 
                        default=False, dest='labels_only')
    args = parser.parse_args()

    if args.input_path == '-':
        for fpath in sys.stdin:
            _dump(fpath.strip(), args)

    elif os.path.isdir(args.input_path):
        for fname in os.listdir(args.input_path):
            fpath = os.path.join(args.input_path, fname)
            _dump(fpath, args)

    else:
        _dump(args.input_path, args)
