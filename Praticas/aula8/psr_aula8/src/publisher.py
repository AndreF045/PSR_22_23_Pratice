#!/usr/bin/env python3

import argparse


def main():

    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('-t', '--topic', type=str, required=False, default='chatter')
    parser.add_argument('-m', '--msg', type=str, required=False, default='Hello World')
    parser.add_argument('-f', '--frequency', type=int, required=False, default=1)

    args = var(parser.parse_args())

    dog = Dog() # Instanciando o objeto Dog
    dog.name = 'Rex'
    dog.color = 'Black'
    dog.age = 5
    dog.brothers.append('Bobby')
    dog.brothers.append('Bella')

    #initilize the node ros
    rospy.init_node('dog_publisher', anonymous=True)

    #.........................................
    #execute the node
    #.........................................
    rate = rospy.Rate(args['frequency'])

    while not rospy.is_shutdown():

        rospy,loginfo('Publishing ' + str(dog))
        publisher.publish(dog)
        rate.sleep()

    #.........................................
    #terminate the node
    #.........................................








if __name__ == '__main__':
    main()