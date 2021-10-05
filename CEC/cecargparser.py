from niapy.util.argparser import get_argparser

cec_options = [8, 13, 14, 15, 16, 17, 18, 19, 21]


def positive_int(x):
    return abs(int(x))


def make_argparser_cec():
    parser = get_argparser()
    parser.add_argument('-c', '--cec', dest='cec',
                        default=cec_options[-1], choices=cec_options, type=int)
    parser.add_argument('-f', '--fnum', dest='fnum',
                        default=1, type=positive_int)
    parser.add_argument('-sr', '--srange', dest='srange',
                        nargs=2, default=[-100, 100], type=int)
    parser.add_argument('-rn', '--rnum', dest='runs',
                        default=51, type=positive_int)
    parser.add_argument('-o', '--wout', dest='wout', action='store_true')
    return parser
