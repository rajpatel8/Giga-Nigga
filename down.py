import os 

for i in range(1, 9):
    os.system("wget https://zenodo.org/record/4010759/files/Adjectives_%s" % i + "of8.zip")

for i in range(1, 3):
    os.system("wget https://zenodo.org/record/4010759/files/Animals_%s" % i + "of2.zip")

for i in range(1, 3):
    os.system("wget https://zenodo.org/record/4010759/files/Clothes_%s" % i + "of2.zip")

for i in range(1, 3):
    os.system("wget https://zenodo.org/record/4010759/files/Colours_%s" % i + "of2.zip")

for i in range(1, 4):
    os.system("wget https://zenodo.org/record/4010759/files/Days_and_Time_%s" % i + "of3.zip")

for i in range(1, 3):
    os.system("wget https://zenodo.org/record/4010759/files/Electronics_%s" % i + "of2.zip")

for i in range(1, 3):
    os.system("wget https://zenodo.org/record/4010759/files/Greetings_%s" % i + "of2.zip")

for i in range(1, 5):
    os.system("wget https://zenodo.org/record/4010759/files/Home_%s" % i + "of4.zip")

for i in range(1, 3):
    os.system("wget https://zenodo.org/record/4010759/files/Jobs_%s" % i + "of2.zip")

for i in range(1, 3):
    os.system("wget https://zenodo.org/record/4010759/files/Means_of_Transportation_%s" % i + "of2.zip")

for i in range(1, 6):
    os.system("wget https://zenodo.org/record/4010759/files/People_%s" % i + "of5.zip")

for i in range(1, 5):
    os.system("wget https://zenodo.org/record/4010759/files/Places_%s" % i + "of4.zip")

for i in range(1, 3):
    os.system("wget https://zenodo.org/record/4010759/files/Pronouns_%s" % i + "of2.zip")

os.system("wget https://zenodo.org/record/4010759/files/Seasons_1of1.zip")

for i in range(1, 4):
    os.system("wget https://zenodo.org/record/4010759/files/Society_%s" % i + "of3.zip")

os.system("wget https://zenodo.org/record/4010759/files/Train_Test_Split.zip")

# save zip files in a folder
os.system("mkdir zip_files")
os.system("mv *.zip zip_files")
