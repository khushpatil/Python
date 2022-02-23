with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letters.docx") as template:
    template_data = template.read()
    for name in names:
        stripped_name = name.strip()
        new_data = template_data.replace("[name]",stripped_name)
        with open(f"./Output/Ready_to_send/letter_to_{stripped_name}.docx",mode = "w") as new_letter:
            new_letter.write(new_data)
