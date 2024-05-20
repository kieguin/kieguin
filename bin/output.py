class Kieguin:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location

output = Kieguin("Kieran Heron", "Code Penguin & Shell Exploiter", "Glasgow, Scotland")

print("👋 Hello, I am " + output.name + "and I am a " + output.description + " from " + output.location)
