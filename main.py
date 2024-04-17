"""Main program"""

from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Animal:
    """Animal class"""

    type: str
    num_legs: int
    num_eyes: InterruptedError


def print_anmial(input_animal: Animal) -> None:
    print(f"My animal is a {input_animal.type}")
    print(
        f"It has {input_animal.num_legs} legs \
          and {input_animal.num_eyes} eyes"
    )


def main():
    """Main function"""
    my_animal: Animal = Animal(type="Dog", num_legs=4, num_eyes=2)
    print_anmial(my_animal)


if __name__ == "__main__":
    main()
