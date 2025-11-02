# # import shared.validators.boolean
# # import shared.validators.date
# # import shared.validators.numeric
# # import shared.validators.json
# #
# shared.validators.json.is_json('{}')
# shared.validators.date.is_date('2018-01-01')
#
#
# print('\n\n****** self ******')
# for k in dict(globals()).keys():
#     print(k)
#
# print('\n\n****** shared ******\n\n')
#
# for k in shared.__dict__.keys():
#     print(k)
#
#
# print('\n\n****** Validatores ******\n\n')
#
# for k in shared.validators.__dict__.keys():
#     print(k)
#
#
# print('\n\n****** numeric ******\n\n')
#
# for k in shared.validators.numeric.__dict__.keys():
#     print(k)

## linking all the sub-package

# import common
# import common.models
# import common.validators as validators
# import common.models.posts.post
# import common.models.posts.posts
# import common.models.users.user
#
#
# validators.is_boolean('True')
# validators.is_json('{}')
# validators.is_numeric('10')
# validators.is_date('2018-01-01')
#
# john_post = common.models.posts.post.Post()
# john_posts = common.models.posts.posts.Posts()
# john = common.models.users.user.User()
#
# print('\n****** self ******\n')
# for k in dict(globals()).keys():
#     print(k)
#
# print('\n****** common ******\n')
#
# for k in common.__dict__.keys():
#     print(k)
#
#
# print('\n****** model ******\n')
#
# for k in common.models.__dict__.keys():
#     print(k)
#
# print('\n****** Validatores ******\n')
#
# for k in validators.__dict__.keys():
#     print(k)
#
#
# print('\n****** numeric ******\n')
#
# for k in validators.numeric.__dict__.keys():
#     print(k)

# ## cleaning up the sub-packages
#
# import common
# import common.models
# import common.validators as validators
# import common.models.posts
# # import common.models.posts.posts
# import common.models.users
#
#
# validators.is_boolean('True')
# validators.is_json('{}')
# validators.is_numeric('10')
# validators.is_date('2018-01-01')
#
# john_post = common.models.posts.Post()
# john_posts = common.models.posts.Posts()
# john = common.models.users.User()
#
# print('\n****** self ******\n')
# for k in dict(globals()).keys():
#     print(k)
#
# print('\n****** common ******\n')
#
# for k in common.__dict__.keys():
#     print(k)
#
#
# # print('\n****** model ******\n')
# #
# # for k in common.models.__dict__.keys():
# #     print(k)
#
# # print('\n****** Validatores ******\n')
# #
# # for k in validators.__dict__.keys():
# #     print(k)
#
#
# print('\n****** Posts (package_ ******\n')
#
# for k in common.models.posts.__dict__.keys():
#     print(k)


## cleaning up the sub-packages and to be able to call as import common.models

import common
import common.models
import common.validators as validators
import common.models as models
# import common.models.posts.posts
# import common.models.users
import common.helpers as helpers


validators.is_boolean('True')
validators.is_json('{}')
validators.is_numeric('10')
validators.is_date('2018-01-01')

john_post = models.Post()
john_posts = models.Posts()
john = models.User()

print('\n****** self ******\n')
for k in dict(globals()).keys():
    print(k)

print('\n****** common ******\n')

for k in common.__dict__.keys():
    print(k)


# print('\n****** model ******\n')
#
# for k in common.models.__dict__.keys():
#     print(k)

# print('\n****** Validatores ******\n')
#
# for k in validators.__dict__.keys():
#     print(k)


print('\n****** Posts (package) ******\n')

for k in common.models.posts.__dict__.keys():
    print(k)


print('\n****** models ******\n')

for k in common.models.__dict__.keys():
    print(k)


# calc = helpers.Calc()
print(helpers.say_hello("Python"))
print(helpers.factorial(10))