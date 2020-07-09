import random
metsFile = open("metsFile.txt","a")
philliesFile = open("philliesFile.txt","a")
cubsFile = open("cubsFile.txt","a")
RedsFile = open("RedsFile.txt","a")
fieldingFile = open("fieldingFile.txt","a")
pitchingFile = open("pitchingFile.txt","a")
battingFile = open("battingFile.txt","a")


team_names=[
    'New York Mets',
    'Philadelphia Phillies',
    'Chicago Cubs',
    'Cincinnati Reds',
]
first_names=['Leroy','David','Lila','Rosie','Christopher','Chad',
             'Lori','Doris','Kathleen','Ivy','Raymond','Dan','Jeffrey',
             'Robert','Mary','Evelyn','Catherine','Joseph','David','Howard',
             'Kathleen','Jennifer','Ashley','Elsie','Sally','Abel','William'
             ,'Donna','Anthony','Edward','Kenneth', 'Gabe', 'Erick', 'Brandon'
             ]

last_names=['Halliday','Jenkins','Mason','Ellis','Ahmann','Daniels','Hall','Stout','Ewing','Herzog','Moore',
            'Boyles','Fitzwater','Smith','Stahl','Randall','Barron','Jackson',
            'Moss','Young','Livoti','Johnson','Walker','Viator','Henry','Melena',
            'Brower','Shin','Midgley','Smith','Belle','Scott','Beauchamp','Barber']


#INSERT INTO PLAYER VALUES('0004','0002', '0004','37', 'Stephen', 'Strasburg' , '2008-07-20','Pitcher');
#INSERT INTO TEAM VALUES('0003','0003', '0003', '0004', 'Yankees', '0', '12');
#INSERT INTO FIELDING_STATS VALUES('0003','1','5','0','6');
#INSERT INTO PITCHING_STATS VALUES('0004', '8', '7', '6', '3', '65', '30', '3', '4');
#INSERT INTO BATTING_STATS VALUES('0002', '3', '2', '3', '2', '1', '0', '1', '1', '0', '2', '1', '0');

for team in team_names:
    if team=='New York Mets':
        creating="INSERT INTO TEAM VALUES('0004','0003', '0003', '0004','Mets', '10','2');\n"
        metsFile.write(creating)
        creating2 = "INSERT INTO STAFF VALUES('0004','0003', '0003');\n"
        metsFile.write(creating2)

        for i in range(0,8):
            id = (i + 5)
            str1="INSERT INTO PLAYER VALUES('000"+str(id)+"',"+",'0004', '0004','"+str(i)+"',"+"'"+first_names[i] +"',"+"'"+last_names[i] +"',"+"'2008-07-20','Pitcher');\n"
            metsFile.write(str1)
            fielding_insert = "INSERT INTO FIELDING_STATS VALUES('000" + str(id) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "');\n"
            fieldingFile.write(fielding_insert)
            pitching_insert = "INSERT INTO PITCHING_STATS VALUES('000" + str(id) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "','" + str(
                random.randint(30, 90)) + "','" + str(random.randint(15, 50)) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "');\n"
            batting_insert = "INSERT INTO BATTING_STATS VALUES('000" + str(id) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "');\n"
            pitchingFile.write(pitching_insert)
            battingFile.write(batting_insert)

    if team=='Philadelphia Phillies':
        creating = "INSERT INTO TEAM VALUES('0005','0002', '0002', '0004','Phillies', '10','2');\n"
        philliesFile.write(creating)
        creating2 = "INSERT INTO STAFF VALUES('0005','0002', '0002');\n"
        philliesFile.write(creating2)

        for i in range(9, 18):
            id = (i + 5)
            str1="INSERT INTO PLAYER VALUES('000"+str(id)+"',"+",'0005', '0004','"+str(i)+"',"+"'"+first_names[i] +"',"+"'"+last_names[i] +"',"+"'2008-07-20','Pitcher');\n"
            philliesFile.write(str1)
            fielding_insert="INSERT INTO FIELDING_STATS VALUES('000"+str(id)+"','"+str(random.randint(0,9))+"','"+str(random.randint(0,9))+"','"+str(random.randint(0,9))+"','"+str(random.randint(0,9))+"');\n"
            fieldingFile.write(fielding_insert)
            pitching_insert = "INSERT INTO PITCHING_STATS VALUES('000" + str(id) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "','" + str(
                random.randint(30, 90)) + "','" + str(random.randint(15, 50)) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "');\n"
            batting_insert = "INSERT INTO BATTING_STATS VALUES('000" + str(id) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "');\n"
            pitchingFile.write(pitching_insert)
            battingFile.write(batting_insert)

    if team=='Chicago Cubs':
        creating = "INSERT INTO TEAM VALUES('0006','0001', '0003', '0004','Cubs', '10','2');\n"
        cubsFile.write(creating)
        creating = "INSERT INTO STAFF VALUES('0006','0001', '0003');\n"
        cubsFile.write(creating2)

        for i in range(19, 26):
            id=(i + 5)
            str1="INSERT INTO PLAYER VALUES('000"+str(id)+"',"+",'0006', '0004','"+str(i)+"',"+"'"+first_names[i] +"',"+"'"+last_names[i] +"',"+"'2008-07-20','Pitcher');\n"
            cubsFile.write(str1)
            fielding_insert = "INSERT INTO FIELDING_STATS VALUES('000" + str(id) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "');\n"
            fieldingFile.write(fielding_insert)
            pitching_insert = "INSERT INTO PITCHING_STATS VALUES('000" + str(id) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "','" + str(
                random.randint(30, 90)) + "','" + str(random.randint(15, 50)) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "');\n"
            batting_insert = "INSERT INTO BATTING_STATS VALUES('000" + str(id) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "');\n"
            pitchingFile.write(pitching_insert)
            battingFile.write(batting_insert)

    if team=='Cincinnati Reds':
        creating = "INSERT INTO TEAM VALUES('0007','0003', '0002', '0004','Reds', '10','2');\n"
        RedsFile.write(creating)
        creating2 = "INSERT INTO STAFF VALUES('0007','0003', '0002');\n"
        RedsFile.write(creating2)
        for i in range(27, 34):
            id = (i + 5)
            str1="INSERT INTO PLAYER VALUES('000"+str(id)+"',"+",'0007', '0004','"+str(i)+"',"+"'"+first_names[i] +"',"+"'"+last_names[i] +"',"+"'2008-07-20','Pitcher');\n"
            RedsFile.write(str1)
            fielding_insert = "INSERT INTO FIELDING_STATS VALUES('000" + str(id) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "');\n"
            fieldingFile.write(fielding_insert)
            pitching_insert = "INSERT INTO PITCHING_STATS VALUES('000" + str(id) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "','" + str(
                random.randint(30, 90)) + "','" + str(random.randint(15, 50)) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 9)) + "');\n"
            batting_insert = "INSERT INTO BATTING_STATS VALUES('000" + str(id) + "','" + str(
                random.randint(0, 9)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "','" + str(
                random.randint(0, 5)) + "','" + str(random.randint(0, 5)) + "');\n"
            pitchingFile.write(pitching_insert)
            battingFile.write(batting_insert)