from .models import person

class userBack:
    def authenticate(self, username=None, password=None):
        try:
            user = person.objects.get(username=username)
        except:
            try:
                user = person.objects.get(email=username)
            except:
                user = None
        if user:
            print("User " + user.username + " is trying to enter")
            if user.check_password(password):
                return user
            else:
                return None
        else:
            return None

    def get_user(self, username):
        try:
            return person.objects.get(username=username)
        except:
            return None
