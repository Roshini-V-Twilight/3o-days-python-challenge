def login_required(func):
    def wrapper():
        is_logged_in = True

        if is_logged_in:
            return func()
        else:
            print("Please login first.")

    return wrapper


@login_required
def dashboard():
    print("Welcome to Dashboard!")


dashboard()