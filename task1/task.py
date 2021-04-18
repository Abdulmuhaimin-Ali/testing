# Replace the placeholders with code and run the Python program

class Banana:
    bananaID =0
    def __init__(self):
        Banana.bananaID += 1
        self._ID = Banana.bananaID
    def __str__(self):
        return "This banana has an id of "+ str(self._ID)

# Create two banana objects
create Banana b1
create Banana b2

print(b1)
print(b2)

