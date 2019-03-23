from pylab import *


def TwoPass(data):
   linked = []
   labels =  np.zeros(data.shape)


   for row in data:
       for column in row:
           if data[row][column] is not 0:

               neighbors = connected elements with the current element's value

               if neighbors is empty:
                   linked[NextLabel] = set containing NextLabel
                   labels[row][column] = NextLabel
                   NextLabel += 1

               else:

                   Find the smallest label

                   L = neighbors labels
                   labels[row][column] = min(L)
                   for label in L:
                       linked[label] = union(linked[label], L)


   for row in data:
       for column in row:
           if data[row][column] is not Background:
               labels[row][column] = find(labels[row][column])

   return labels