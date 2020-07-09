import random

InningFile = open("Inningfile.txt","a")

for i in range(0,8):
    for j in range(0,6):
        h_hits = random.randint(0, 10);
        h_runs = h_hits - 1;
        h_errors = random.randint(0,2);

        v_hits = random.randint(0, 10);
        v_runs = h_hits - 1;
        v_errors = random.randint(0, 2);

        line = "INSERT INTO INNING  VALUES('000" + str(i) + "', '" + str(j) + "', '" + str(h_hits) + "', '" + str(h_runs) + "', '" + str(h_errors) + "', '" + str(v_hits)   + "', '" + str(v_runs) + "', '" + str(v_errors) + "');\n"
        InningFile.write(line)
