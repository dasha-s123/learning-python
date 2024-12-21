import AdminAndPrivieges

user_1 = AdminAndPrivieges.Admin('Даша', "Севостьянова", "Shypiece", 7, 17, "женщина")
user_1.describe_user()
user_1.greet_user()
user_1.show_login_attemps()
user_1.increment_login_attemps()
user_1.show_login_attemps()
user_1.reset_login_attemps()
user_1.show_login_attemps()
user_1.privileges.determine_privileges('банить ользователей', "добавлять сообщения",
                                       "удалять сообщения", "удалять пользователей"
                                       )
user_1.privileges.show_privileges()