f = open("C:/Users/kj/Desktop/myGit/PYTHON101/problems/test.txt", "a")
for i in range(11,16):
    data = f"{i}번째 줄 추가\n"
    f.write(data)
f.close()

