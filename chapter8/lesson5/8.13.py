def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе"""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info


user_profile = build_profile('dasha', 'sevostianova',
                             location='Lipetsk',
                             age=17,
                             field='math'
                             )
print(user_profile)