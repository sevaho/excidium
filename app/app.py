#! /usr/bin/python

# -----------------------------------------------------------------------------------------------------------------------------
# GENERAL
# -----------------------------------------------------------------------------------------------------------------------------
#
# author: Sebastiaan Van Hoecke
# mail: sebastiaan@sevaho.io
#
# NOTE:
#
# -----------------------------------------------------------------------------------------------------------------------------

import sys
import getopt

# -----------------------------------------------------------------------------------------------------------------------------
# GLOBAL VARIABLES
# -----------------------------------------------------------------------------------------------------------------------------

target          = ""
port            = 0
wordlist_dir    = ""

# -----------------------------------------------------------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------------------------------------------------------


def usage ():

    print("Usage: %s [OPTIONS]... [ARGS]... \
            \n \
            \n  description\
            \n \
            \nOPTIONS:\
            \n \
            \n  -h, *       display the help and exit\
            \n \
            \nEXAMPLES:\
            \n \
            \nNOTE:\
            \n \
            " % (sys.argv[0]))

    sys.exit(1)


def banner ():

    print("\
            \n   _____  _____(_) __| (_)_   _ _ __ ___   \
            \n  / _ \ \/ / __| |/ _` | | | | | '_ ` _ \  \
            \n |  __/>  < (__| | (_| | | |_| | | | | | | \
            \n  \___/_/\_\___|_|\__,_|_|\__,_|_| |_| |_| \
            \n \
            \n By sevaho - sebastiaan@sevaho.io \
            \n \
            \n Pentest framework \
            \n \
            ")

# -----------------------------------------------------------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------------------------------------------------------


def main (argv):

    global target, port, wordlist_dir

    banner()

    # if not len(argv):
    #     usage()

    try:

        opts, args = getopt.getopt(argv, "h:t:p:w:", [
            "help",
            "target",
            "port",
            "wordlist_dir"])

    except getopt.GetoptError as err:

        print("error: %s" % (str(err)))
        usage()

    for opt, arg in opts:

        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-t", "--target"):
            target = arg
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-w", "--wordlist_dir"):
            wordlist_dir = arg
        else:
            assert False, "Unhandled Option"

    print("What would you like to do captain? \
            \n \
            \n  1) web \
            \n  2) netw \
            \n  3) shells \
            \n  4) auto \
            \n  99) exit \
            \n \
            ")

    mode = input()
    mode = int(mode)

    if mode == 1:
        print("web mode")

    elif mode == 2:
        print("network mode")

    elif mode == 3:
        print("shells mode")

    elif mode == 99:
        sys.exit(1)


if __name__ == "__main__":

    main(sys.argv[1:])
