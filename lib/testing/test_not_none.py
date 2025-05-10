from lib.not_none_functions import return_not_none

def test_return_not_none():
    '''Test that return_not_none() does not return None.'''
    assert return_not_none() is not None
