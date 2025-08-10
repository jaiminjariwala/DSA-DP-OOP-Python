#allow access only if a user is authorized

def require_auth(func):
    def wrapper(user, *args, **kwargs):
        if user!="admin":
            print(f"\nViewing dashboard as a guest!")
            print("Unauthorized!\n")
            return
        return func(user, *args, **kwargs)
    return wrapper


@require_auth
def view_dashboard(user):
    print(f"Welcome {user} to the dashboard!\n")

view_dashboard("guest") # unauthorized
view_dashboard("admin") # welcome