from unittest.mock import patch, Mock, MagicMock

class cA():
    def __init__(self):
        pass
    
    def method():
        pass

class cB():
    def __init(self):
        pass



# def change_to_none(func):
#     def none_func():
#         print("I'm none")
#     return none_func

@patch('__main__.cB')
@patch('__main__.cA')
def test_foo(num, mock_A, mock_B):
    print(num)
    print(mock_A)
    print(mock_B)

test_foo(1)

def test_bar(num):
    with patch('__main__.cA') as mock_A:
        print(num)
        print(mock_A)

test_bar(2)

thing = MagicMock(return_value=3)
print(thing())
@patch.object(cA, 'method')
def baz(mock_method):
    c = cA()
    c.method(1,1,1)
    mock_method.assert_called_with(1,1,1)
    print('finished')

baz()