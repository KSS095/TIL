def adult(user_list):
    over_eighteen = []
    for user in user_list:
        if user["age"] >= 18:
            over_eighteen.append(user)
    return over_eighteen