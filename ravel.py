#!/usr/bin/env python

import os
import sys
from optparse import OptionParser

DB='mininet'
DBUSER='mininet'

# add ravel to path
if 'PYTHONPATH' in os.environ:
    sys.path = os.environ['PYTHONPATH'].split(':') + sys.path
    raveldir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.abspath(raveldir))

def parseArgs():
    desc = ( "Ravel console." )
    usage = ( '%prog [options]\n'
              '(type %prog -h for details)' )

    parser = OptionParser(description=desc, usage=usage)
    parser.add_option('--remote', '-r', action='store_true', default=False,
                      help='start remote controller')
    parser.add_option('--user', '-u', type='string', default=DBUSER,
                      help='postgresql username (default: %s)' % DBUSER)
    parser.add_option('--db', '-d', type='string', default=DB,
                      help='postgresql username (default: %s)' % DB)
    parser.add_option('--password', '-p', action='store_true', default=False,
                      help='postgresql password')
    parser.add_option('--custom', type='string', default=None,
                     help='mininet: read custom classes or params from py file(s)')
    parser.add_option('--topo', '-t', type='string', default=None,
                      help='mininet: topology argument')
    parser.add_option('--verbosity', '-v',  type='choice',
                      choices=LEVELS.keys(), default='info',
                      help='|'.join(LEVELS.keys()))

    options, args = parser.parse_args()
    if args:
        parser.print_help()
        sys.exit(0)

    if not options.topo:
        parser.error("No topology specified")

    logger.setLogLevel(options.verbosity)

    return options
    
if __name__ == "__main__":
    from ravel.cli import RavelCLI
    from ravel.log import LEVELS, logger
    opts = parseArgs()
    RavelCLI(opts, opts.remote)
