# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import argparse
import os
import os.path
import sys

from nvget.controller import Controller


def _print(msg):
    sys.stderr.write('{}\n'.format(msg))
    sys.stderr.flush()


def nvget(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--user', type=str,
        help='e-mail address (NVGET_USER)')
    parser.add_argument(
        '--password', type=str,
        help='password (NVGET_PASSWORD)')
    parser.add_argument(
        '--timeout', type=int, default=15,
        help='operation timeout in seconds')
    parser.add_argument(
        '--chrome', type=str,
        help='path to google-chrome (NVGET_CHROME)')
    parser.add_argument(
        '--driver', type=str,
        help='path to chromedriver (NVGET_DRIVER)')
    parser.add_argument(
        '--output', type=str,
        help='path to save the downloaded file')
    parser.add_argument(
        'url', type=str,
        help='URL to download')

    args = parser.parse_args(args)
    for key in ['user', 'password', 'chrome', 'driver']:
        if getattr(args, key) is None:
            envkey = 'NVGET_{}'.format(key.upper())
            envvar = os.environ.get(envkey)
            if envvar is not None:
                setattr(args, key, envvar)
            else:
                parser.error(
                    '--{} option or environment variable {} '
                    'must be specified'.format(key, envkey))

    if args.output is None:
        args.output = os.path.basename(args.url)

    _print('Logging in...')
    ctrl = Controller(args.chrome, args.driver, int(args.timeout))
    ctrl.login(args.user, args.password)

    _print('Downloading {} to {}...'.format(args.url, args.output))
    ctrl.download_to(args.url, args.output)

    _print('Done!')


if __name__ == '__main__':
    nvget()
