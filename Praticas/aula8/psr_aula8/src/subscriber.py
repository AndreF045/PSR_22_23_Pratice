#!/usr/bin/env python3

import argparse

def msgReceivedCallback(msg):
    rospy.loginfo('I received\n:' + str(msg) + '\n')


def main():

    #.........................................
    #initialize the node
    #.........................................

    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('-t', '--topic', type=str, required=False, default='chatter')
    args = vars(parser.parse_args())

    #initilize the node ros

    rospy.init_node('subscriber', anonymous=True)

    #INNITIALIZE THE SUBSCRIBER
    rospy.Subscriber(args['topic'], Dog, msgReceivedCallback)

    #.........................................
    #execute the node
    #.........................................
    rospy.spin()

    #.........................................
    #terminate the node
    #.........................................












if __name__ == '__main__':
    main()#