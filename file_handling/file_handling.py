"""
Järjestää tiedostosta luetut sanat ensisijaisesti pituuden mukaan ja toissijaisesti aakkosittain.
Kirjoittaa järkätyt sanat uuteen tiedostoon
"""

def read_the_file():
    with open("alkusanat.txt", "r") as the_file:
        words = []

        for word in the_file:
            words.append(word.rstrip("\n"))

    words.sort()
    words.sort(key=len)

    with open("loppusanat.txt", "w") as another_file:
        for word in words:
            another_file.write(f"{word}\n")


if __name__ == "__main__":
    read_the_file()