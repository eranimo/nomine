from nomine import Nomine

if __name__ == "__main__":
    name = Nomine(preset="countries")

    for _ in range(10):
        print(name.get(length=5))
