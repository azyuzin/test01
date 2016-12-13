import sys
import getopt

def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    i = 1
    for arg in args:
        print "argument", i, " = ", arg

        i=i+1
#        process(arg) # process() is defined elsewhere

if __name__ == "__main__":
    main()
