import pytest
class User:
    def __init__(self, username):
        if len(username) < 1:
            raise Exception("Username must not be empty.")
        self._username = username
    @property
    def username(self):
        return self._username


#BAD code
def test_user():
    username = 'johndoe'
    assert User(username).username == username

    username = ""
    with pytest.raises(Exception):
        User(username)

#GOOD code
def test_user_with_valid_username_can_be_initialized():
    username = "johndoe"
    assert User(username).username == username

def test_user_with_empty_username_cannot_be_initialised():
    username = ""
    with pytest.raises(Exception):
        User(Username)