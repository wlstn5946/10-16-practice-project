import random
from pathlib import Path

DATA_FILE = Path(__file__).parent / "restaurant.txt"


def load_restaurants(path):
    restaurants = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        name, sep, kind = line.partition(",")
        name, kind = name.strip(), kind.strip()
        if not sep or not name or not kind:
            continue
        restaurants.append((name, kind))
    return restaurants


def pick_restaurant(restaurants):
    if not restaurants:
        return None
    return random.choice(restaurants)


def main():
    picked = pick_restaurant(load_restaurants(DATA_FILE))
    if picked is None:
        print("추천할 식당이 없습니다.")
        return
    name, kind = picked
    print(f"{name} - {kind}")


if __name__ == "__main__":
    main()
