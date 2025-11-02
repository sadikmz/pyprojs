class StarCookies:
    milk = 0.1

    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

# star_cookie1 = StarCookies("red",16)
# print(star_cookie1)
# print(star_cookie1.color)
# print(star_cookie1.weight)
# print(star_cookie1.milk)

class Youtube:
    def __init__(self, username, subscribers=0,subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions


    def subscribe(self, user):
        user.subscribers +=1
        self.subscriptions += 1


user1 = Youtube("user1")
user2 = Youtube("user2")
user1.subscribe(user2)
print(user1.subscribers)