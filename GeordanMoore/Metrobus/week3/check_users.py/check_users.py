def check_users(current_users, new_users):

    pass

    current_users = []
    new_users = []

    current_users = [user.lower() for user in current_us]
    new_users = new_us

    for new_user in new_users:
        if new_user.lower() in current_users:
            print("Username " + new_user + " is taken".format(current_users))
        else:
            print("Username " + new_user + " is available".format(new_users))


if __name__ == "__main__":
    current_us = ['george','chris','haritha', 'sally', 'darnell', 'superman', 'john']

    new_us = ['george', 'ringo', 'superman', 'hannibal', 'chris', 'JOHN']

    check_users(current_us, new_us)