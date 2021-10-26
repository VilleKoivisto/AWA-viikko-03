"""
Järjestää tiedostosta luetut sanat ensisijaisesti pituuden mukaan ja toissijaisesti aakkosittain.
Kirjoittaa järkätyt sanat uuteen tiedostoon
"""

import argparse


def read_the_file(filename):
    try:
        with open(filename, "r") as the_file:
            words = []

            for word in the_file:
                words.append(word.rstrip("\n"))

        words.sort()
        words.sort(key=len)

        with open("loppusanat.txt", "w") as another_file:
            for word in words:
                another_file.write(f"{word}\n")

    except OSError:
        print("No such file dude!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    arguments = parser.parse_args()

    read_the_file(arguments.file)