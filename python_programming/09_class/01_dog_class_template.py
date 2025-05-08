# A dog has a name, a birthday, and a sound it makes when it barks

boyDog = Dog("Mesa", 5, 15, 2004, "WOOOF")
girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
print(boyDog.speak())
print(girlDog.speak())
print(boyDog.birthDate())
print(girlDog.birthDate())
boyDog.changeBark("woofywoofy")
print(boyDog.speak())