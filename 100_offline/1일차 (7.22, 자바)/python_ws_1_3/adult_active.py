def adult_active(user_list):
    over_activate = []
    for user in user_list:
        if user["age"] >= 18 and user["is_active"] == True:
            over_activate.append(user)
    return over_activate