"""
11. რამდენიმე ფაილის გაერთიანება
დაწერეთ პროგრამა, რომელიც გახსნის რამდენიმე ფაილს (მაგალითად, file1.txt, file2.txt,
file3.txt) და მათი შიგთავსი გააერთიანებს ერთ ახალ ფაილში combined.txt.
"""
with open("files/file1.txt") as file1:
    lines1 = file1.readlines()
with open("files/file2.txt") as file2:
    lines2 = file2.readlines()
with open("files/file3.txt") as file3:
    lines3 = file3.readlines()

lines1 = [line if line.endswith("\n") else line + "\n" for line in lines1 ]
lines2 = [line if line.endswith("\n") else line + "\n" for line in lines2 ]
lines3 = [line if line.endswith("\n") else line + "\n" for line in lines3 ]

with open("files/combined.txt", "w") as combined:
    combined.writelines(lines1 + lines2 + lines3)