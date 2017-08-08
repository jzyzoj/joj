
def Check_privilege(user,pri):
    return (user.privileges & (1<<pri))==1

