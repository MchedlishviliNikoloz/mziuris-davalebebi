"""
10. შინაარსის შებრუნება ფაილში
დაწერეთ პროგრამა, რომელიც წაიკითხავს example.txt ფაილის შიგთავსს, შებრუნებს მას (ანუ
ბოლო ხაზი იქნება პირველი და პირველი - ბოლო) და ჩაწერს ახალ ფაილში
reversed_example.txt.
"""

with open("files/example.txt") as file:
    lines = file.readlines()

fixed_lines = []
for line in lines:
    if line.endswith("\n"):
        fixed_lines.append(line)
    else:
        fixed_lines.append(line+"\n")

with open("files/reversed_example.txt", "w") as file:
    file.writelines(reversed(fixed_lines))