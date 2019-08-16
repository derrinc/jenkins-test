#!/usr/bin/env python
################################################################################
##
## NAME
##	hello-test.py - Validate hello.py
##
## DESCRIPTION
##	Use unittest to validate return values from hello.py
##
################################################################################


### Import modules
import unittest
import hello


# ============================================================================ #
class TestHello( unittest.TestCase ):

    def setUp( self ):
        hello.hello.testing = True
	self.hello = hello.app.test_client()

    def testRoot( self ):
        rv = self.hello.get( '/' )
	self.assertEqual( rv.status, '200 OK' )
	self.assertEqual( rv.data, b'Index!\n' )

    def testHello( self ):
        rv = self.hello.get( '/hello' )
	self.assertEqual( rv.status, '200 OK' )
	self.assertEqual( rv.data, b'Hello world!\n' )

    def testHello( self ):
        rv = self.hello.get( '/members' )
	self.assertEqual( rv.status, '200 OK' )
	self.assertEqual( rv.data, b'Members, hello!\n' )

#    def testHello( self ):
#        name = 'Simon'
#        rv = self.hello.get( f"/members/{name}" )
#        self.assertEqual( rv.status, '200 OK' )
#        self.assertIn( bytearray( f"Hello, {name}!\n", 'utf-8' ), rv.data )

# ============================================================================ #


# ---------------------------------------------------------------------------- #
def main():
    if( __name__ == '__main__' ): unittest.main()
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
main()
