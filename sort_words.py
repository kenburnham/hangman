#file = open("/home/psdcadmin/projects/developer-lab/words_alpha.txt", "r")
hangman_words = open("hangman_words.txt", "a")

h_c = 0

with open("/home/psdcadmin/projects/developer-lab/10k.txt") as file:
    for line in file:
        file_len = len(line) - 1
        if file_len > 5:
            hangman_words.write(line)
            h_c += 1


print("Words: ", h_c)

file.close()
hangman_words.close()