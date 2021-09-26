from niapy.util.argparser import get_argparser

ccecs = [8, 13, 14, 15, 16, 17, 18, 19]
creduces = [0.01, 0.02, 0.03, 0.05, 0.1, 0.2,
            0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]


def positive_int(x):
    return abs(int(x))


def make_argparser_cec():
    parser = get_argparser()
    parser.add_argument('-c', '--cec', dest='cec',
                        default=ccecs[-1], choices=ccecs, type=int)
    parser.add_argument('-f', '--fnum', dest='fnum',
                        default=1, type=positive_int)
    parser.add_argument('-sr', '--srange', dest='srange',
                        nargs=2, default=[-100, 100], type=int)
    parser.add_argument('-nr', '--nFESreduc', dest='reduc',
                        default=creduces[-1], choices=creduces, type=float)
    parser.add_argument('-rn', '--rnum', dest='runs',
                        default=51, type=positive_int)
    parser.add_argument('-o', '--wout', dest='wout', action='store_true')
    return parser
