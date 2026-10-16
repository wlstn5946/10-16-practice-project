import argparse
import random
from pathlib import Path

DATA_FILE = Path(__file__).parent / "restaurant.txt"
KIND_OPTIONS = {"korean": "한식", "chinese": "중식", "western": "양식"}


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


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="식당을 랜덤으로 추천합니다.")
    group = parser.add_mutually_exclusive_group()
    for option, kind in KIND_OPTIONS.items():
        group.add_argument(
            f"--{option}", dest="kind", action="store_const", const=kind,
            help=f"{kind} 중에서 추천",
        )
    return parser.parse_args(argv).kind


def filter_by_kind(restaurants, kind):
    if kind is None:
        return restaurants
    return [r for r in restaurants if r[1] == kind]


def main():
    kind = parse_args()
    restaurants = filter_by_kind(load_restaurants(DATA_FILE), kind)
    picked = pick_restaurant(restaurants)
    if picked is None:
        print("추천할 식당이 없습니다.")
        return
    name, kind = picked
    print(f"{name} - {kind}")


if __name__ == "__main__":
    main()
