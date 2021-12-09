from learningflask.models import User


def test_new_user():
    """
    GIVEN a user model
    WHEN a user is created
    THEN check that the username, email, hashed_password fields are defined correctly
    """
    user = User(
        username='chris',
        email='chris@gmail.com',
        password='FlaskIsAwesome'
    )
    assert user.username == 'chris'
    assert user.email == 'chris@gmail.com'
