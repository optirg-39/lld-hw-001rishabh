# Create a Singleton class - LLD Design Pattern

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    
# Example usage
if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 is singleton2)  # Output: True  # Both variables point to the same instance

