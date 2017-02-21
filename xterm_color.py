#!/usr/bin/env python

import optparse
from random import randint

def main():
  parser = optparse.OptionParser(description='Dark colors for xterms.')
  parser.add_option('--favour', choices=["red", "green", "blue", "grey"])

  (options, args) = parser.parse_args()

  min_c1 = 0
  max_c1 = 96

  if (options.favour != None):
    min_c1 = 48

  if (options.favour == "grey"):
    i = randint(20, 60)
    c = [i, i, i]
  else:
    c = get_color(min_c1, max_c1)

  if (options.favour == "red"):
    print "rgb:%02x/%02x/%02x" % (c[0],c[1],c[2])
  elif (options.favour == "green"):
    print "rgb:%02x/%02x/%02x" % (c[1],c[0],c[2])
  elif (options.favour == "blue"):
    print "rgb:%02x/%02x/%02x" % (c[1],c[2],c[0])
  else:
    o = rand_order()
    print "rgb:%02x/%02x/%02x" % (c[o[0]],c[o[1]],c[o[2]])

def get_color(mn, mx):
  c1 = randint(mn, mx)
  mx = mx - c1

  c2 = randint(0, mx)
  c3 = mx - c2

  return (c1, c2, c3)

def rand_order():
  orders = ( (0, 1, 2),
             (0, 2, 1),
             (2, 0, 1),
             (2, 1, 0),
             (1, 0, 2),
             (1, 2, 0) )
             
  o = randint(0, 5)
  return orders[o]

main()
