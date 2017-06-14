import unittest
import os
from time import sleep


class Testequal(unittest.TestCase):

    def setUp(self):
        print 'start'

    def test_equal(self):
        dir1 = 'C:\\Users\\sting\\Desktop\\testpath\\'
        dir2 = 'C:\\Users\\sting\\Desktop\\answernew\\'
        for i in range(16):
            traindir1 = dir1 + 'case' + str(i) + '.txt'
            traindir2 = dir2 + 'case' + str(i) + '.txt'
            # print traindir1
            fd1 = open(traindir1, 'r')
            fd2 = open(traindir2, 'r')
            a = fd1.readlines()
            b = fd2.readlines()
            # print file
            self.assertEqual(a, b, msg='False')
            print str(i) + ' is True'
            # sleep(3)

    def tearDown(self):
        print 'end'

if __name__ == "__main__":
    unittest.main()
