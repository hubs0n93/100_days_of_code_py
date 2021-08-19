DATA = """root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
ivanovic:x:1002:1002:Иван Иванович:/home/ivanovic:/bin/bash
lewis:x:1003:1002:Melissa Lewis:/home/ivanovic:/bin/bash"""


# result: list = []
#
# for line in DATA.splitlines():
#     if int(line.split(":")[2]) < 1000:
#         result.append(line.split(":")[0])

result = [username
          for row in DATA.splitlines()
          if (line := row.split(":"))
          and (username := line[0])
          and (uid := line[2])
          and int(uid) < 1000]
print("\nExcercise to solve \n\nDATA:")	  
print(DATA)
print("read this multiline string\n")
print("Split `DATA` by lines and then by colon `:`, Extract system accounts (users with UID [third field] is less than 1000)")
print("return list of loggins\n\n")
print("****************************************************************************************************")
print("IMPLEMENTATION\n")
print("result = [username" + "\n"
          "     for row in DATA.splitlines()" + "\n"
          "     if (line := row.split(':'))" + "\n"
          "     and (username := line[0])" + "\n"
          "     and (uid := line[2])" + "\n"
          "     and int(uid) < 1000]" + "\n")
print("****************************************************************************************************")
		  
print(f"result: \n{result}")
		  
