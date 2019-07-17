def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('avyakt', 'gaur',
                             location='ashburn',
                             age="14", favorite_color="green")
print(user_profile)