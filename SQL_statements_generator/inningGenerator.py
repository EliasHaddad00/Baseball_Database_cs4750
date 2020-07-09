import random

InningFile = open("Inningfile.txt","w")

for i in range(4, 11):
    for j in range(1, 7):
        h_hits = random.randint(0, 10);
        if h_hits > 0:
            h_runs = h_hits - 1;
        else:
            h_runs = 0
        h_errors = random.randint(0,2);

        v_hits = random.randint(0, 10);
        v_runs = h_hits - 1;
        if v_hits > 0:
            v_runs = v_hits - 1;
        else:
            v_runs = 0
        v_errors = random.randint(0, 2);

        line = "INSERT INTO INNING  VALUES('000" + str(i) + "', '" + str(j) + "', '" + str(h_hits) + "', '" + str(h_runs) + "', '" + str(h_errors) + "', '" + str(v_hits)   + "', '" + str(v_runs) + "', '" + str(v_errors) + "');\n"
        InningFile.write(line)
