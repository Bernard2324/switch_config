#!/usr/bin/env python

from time import sleep
import argparse
import manage
import sys

def get_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--host',
        required=True,
        action='store',
        help="Type 11 or 12 for the target Switchstack", default=None
    )

    parser.add_argument('-p', '--port',
        required=False,
        action='store',
        help="Provide Interface Number: e.g. 3/0/21"
    )

    parser.add_argument('-t', '--type',
        required=False,
        action='store',
        help="Port Type.  data (e.g. 11.D.005) or voice (e.g. 11.V.005)"
    )

    parser.add_argument ('-r', '--remove',
        required=False,
        action='store_true',
        help="Dissasociate learned MAC's from interface"
    )

    parser.add_argument('-i', '--interactive',
        required=False,
        action='store_true',
        help="Enter Interactive Mode to Submit Multiple results"
    )

    args = parser.parse_args()
    return args

def main():
    args = get_args()

    #if (args.type is None) and ((not args.remove) or (not args.interactive)):
    #    raise AttributeError("You Must Provide Type (-t, --type) or Removal (-r, --remove) flags!\n")

    run = manage.configInterface(args.host)
    def runcommands(command_set, maximum='3'):
        run.getConfigure()
        try:
            run.commands(cmd_set)
        except:
            print "Failed to Execute Command Set on Interface GigabitEthernet{}".format(i)
        print "Successfull Implementation!"

    if not args.interactive:
        interface_set = args.port.split()
        for i in interface_set:
            run.escalate()
            if args.remove:
                print "Dissasociating Learned MAC for Interface GigabitEthernet{}".format(i)
                clear_set = run.clearall(i)
                run.commands(clear_set)
            elif args.type is not None:
                if not any(i in ['data', 'voice'] for i in args.type):
                    raise AttributeError("Invalid Argtype: Type - Must be voice or data")
                if args.type == 'data':
                    maxi = '3'
                else:
                    maxi = '1'
                print "Configuring Interface GigabitEthernet{}".format(i)
                cmd_set = run.dataconfigset(i, maxi)
                runcommands(cmd_set, maximum=maxi)
        run.end()
    else:
        print "Entering Interactive Schell.  Configuration Support Only!"
        sleep(5)
        while True:
            try:
                inter = raw_input("(Please Enter the Interface)>> ").strip()
                if inter is not None:
                    run.escalate()
                    cmd_set = run.dataconfigset(inter, '3')
                    runcommands(cmd_set)
                else:
                    pass
            except KeyboardInterrupt:
                run.end()


main()
