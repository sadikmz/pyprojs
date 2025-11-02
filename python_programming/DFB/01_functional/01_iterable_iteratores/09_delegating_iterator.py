from collections import namedtuple

Person = namedtuple('Person', 'name age')

class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize()
                             + ' ' + person.last.capitalize()
                            for person in persons]
        except (TypeError, AttributeError):
            self.persons = []

persons = [Person('michaeL', 'paLin'), Person('eric', 'idLe'),Person('john', 'cLeese')]

person_names = PersonNames(persons)
print(person_names._persons)

# for name in person_names:
#     print(name)

# class PersonNames:
#     def __init__(self, persons):
#         try:
#             self._persons = [person.first.capitalize()
#                              + ' ' + person.last.capitalize()
#                              for person in persons]
#         except(TypeError, AttributeError):
#             self._persons = []
#             # self.person = []
#
#     def __iter__(self):
#         return iter(self._persons)
#
# # persons = [Person('michaeL','paLin'), Person('eric','idLe'),
# #            Person('john','cLeese')]
#
# person_names = PersonNames(persons)
#
# print(person_names._persons)
# print(dir(person_names))
# for name in person_names:
#     print(name)