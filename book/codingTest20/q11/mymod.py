class MyMode:

    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"my mode ({self.name}) class"
    

if __name__ == "__main__":
    a = MyMode("temperary")
    print(a)