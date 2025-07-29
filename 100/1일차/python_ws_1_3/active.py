def active(user_list):
    activate = []
    for user in user_list:
        if user["is_active"] == True:
            activate.append(user)
    return activate