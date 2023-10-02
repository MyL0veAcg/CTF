import hashlib
for i in range(65,91):
    for j in range(65,91):
        for k in range(65,91):
            string="TASC"+chr(i)+"O3RJMV"+chr(j)+"WDJKX"+chr(k)+"ZM"
            md5obj=hashlib.md5()
            md5obj.update(string.encode("utf-8"))#要encode一下
            hexmd5=md5obj.hexdigest()
            if hexmd5[0:4].upper() == "E903":
                print("The string is:"+string)
                print("The md5 is:"+hexmd5.upper())