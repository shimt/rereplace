#! /usr/bin/env python3
# coding: utf-8

import argparse
import locale
import sys
import re


def build_argparser():
    parser = argparse.ArgumentParser(
        description='regex replacing tool'
    )

    group = parser.add_argument_group('regex matching flags')

    group.add_argument(
        '--re-ascii', '-a',
        dest='re_ascii',
        action='store_true',
        help='re.ASCII'
    )

    group.add_argument(
        '--re-debug',
        dest='re_debug',
        action='store_true',
        help='re.DEBUG'
    )

    group.add_argument(
        '--re-ignorecase', '-i',
        dest='re_ignorecase',
        action='store_true',
        help='re.IGNORECASE'
    )

    group.add_argument(
        '--re-locale', '-l',
        dest='re_locale',
        action='store_true',
        help='re.LOCALE'
    )

    group.add_argument(
        '--re-multiline', '-m',
        dest='re_multiline',
        action='store_true',
        help='re.MULTILINE'
    )

    group.add_argument(
        '--re-dotall', '-s',
        dest='re_dotall',
        action='store_true',
        help='re.DOTALL'
    )

    group.add_argument(
        '--re-verbose', '-x',
        dest='re_verbose',
        action='store_true',
        help='re.VERBOSE'
    )

    #

    parser.add_argument(
        '--multiline',
        dest='multiline',
        action='store_true',
        help='enable multi-line mode (read all the lines into a memory)'
    )

    #

    parser.add_argument('pattern', metavar='PATTERN')
    parser.add_argument('replacement', metavar='REPLACEMENT')

    return parser


def build_re_flags(args):
    flags = 0

    if args.re_ascii:
        flags |= re.ASCII

    if args.re_debug:
        flags |= re.DEBUG

    if args.re_ignorecase:
        flags |= re.IGNORECASE

    if args.re_locale:
        flags |= re.LOCALE

    if args.re_multiline or args.multiline:
        flags |= re.MULTILINE

    if args.re_dotall:
        flags |= re.DOTALL

    if args.re_verbose:
        flags |= re.VERBOSE

    return flags


def build_pattern(arg, encoding, re_flags):
    pattern = None

    if arg.startswith('@'):
        with open(arg[1:], encoding=encoding) as f:
            s = f.read()
        pattern = re.compile(s, flags=re_flags)
    else:
        pattern = re.compile(arg, flags=re_flags)

    return pattern


def build_replacement(arg, encoding):
    replacement = None

    if arg.startswith('@'):
        with open(arg[1:], encoding=encoding) as f:
            s = f.read()
        replacement = s
    else:
        replacement = arg

    return replacement


def build_inobject(args):
    return [sys.stdin.read()] if args.multiline else sys.stdin


def main():
    parser = build_argparser()

    args = parser.parse_args()

    encoding = locale.getpreferredencoding()
    re_flags = build_re_flags(args)

    inobject = build_inobject(args)
    outstream = sys.stdout

    pattern = build_pattern(args.pattern, encoding, re_flags)
    replacement = build_replacement(args.replacement, encoding)

    for line in inobject:
        line = pattern.sub(replacement, line)
        outstream.write(line)

if __name__ == '__main__':
    main()
