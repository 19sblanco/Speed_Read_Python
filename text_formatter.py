def is_title(i, lines):
    if 1 < i < len(lines) - 1:
        if lines[i-1] == "\n" and lines[i-2] == "\n" and lines[i+1] == "\n" and lines[i+2] == "\n":
            return True
    return False


def buffer_length(buffer):
    total = 0
    for word in buffer:
        total += len(word)
    return total

"""
book titles get their own line
    * check if a line is a title before spliting it into words
don't add blank lines
lines are 70 characters otherwise
    * split lines into words
    * build up a buffer line
    * if adding the next word exceeds teh 70 char limit, add the new line to the list of lines then add the exra word to its own new blank line
"""
file_path = "/home/sblanco2465/codeProjects/personalProjects/speedRead/texts/gospel_text/temp_old_testament.txt"

new_lines = []
with open(file_path, "r") as file:
    lines = file.readlines()
    new_line = []
    for i in range(len(lines)):
        line = lines[i]
        if is_title(i, lines):
            cp_new_line = new_line[:]
            new_lines.append(cp_new_line)
            new_line = []
            new_line.append(line)
            cp_new_line = new_line[:]
            new_lines.append(cp_new_line)
            new_line = []
        else:
            words = line.split()
            for word in words:
                potential_length = buffer_length(new_line) + len(word)
                if potential_length < 55:
                    new_line.append(word)
                else:
                    cp_new_line = new_line[:]
                    new_lines.append(cp_new_line)
                    new_line = []
                    new_line.append(word)
    cp_new_line = new_line[:]
    new_lines.append(cp_new_line)


# print_list = new_lines[0:100]
# for i in range(len(print_list)):
#     print(print_list[i])

write_file_path = "/home/sblanco2465/codeProjects/personalProjects/speedRead/texts/gospel_text/BibleOldTestament.txt"
with open(write_file_path, "w") as file:
    for line in new_lines:
        str = ""
        for word in line:
            str += word + " "
        str += "\n"
        file.write(str)
    
