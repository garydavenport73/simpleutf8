# simpleutf8.py
#
# A python script that generates UTF-8 Unicode Tables
# Gary Davenport 2/4/2021
#
# This is a python script to generate ut-8 codeblock charts. It works reasonably well 
# for its purpose. It was tested in Python 3.8.6 64-bit.
# I mainly made this so I could inspect characters for video games and ther uses by 
# visually scanning through single condensed text file containing utf-8 characters.
# It opens ok for me in notepad, but the output file is 299kb and 5120 lines long.
# If the file is too large, you can change the numbers 
# in the range(2,4096) to different starting/ending numbers.
#
# Input-none
#
# Output-a text file that writes to the current directory of the simpleutf8.py file.
#
# The output file is named simpleutf8out.txt
#
# Output can be checked against the website: https://www.ssec.wisc.edu/~tomw/java/unicode.html
def main():
    outFile=open("simpleutf8out.txt","w",encoding="utf-8")                                  #open file for writing tables
    print("\nSimple Unicode Block Generator for UTF-8")
    outFile.write("Simple Unicode Block Generator for UTF-8\n")
    for i in range(2,4096):                                                                 # start at 2, because 0 and 1 are mainly nonsense and don't format well
        string=""           
        hexString=hex(i*16)[0:2]+ (6-len(hex(i*16)))*"0" + hex(i*16)[2:-1] + "x"            # this is a hex in 6 character form
        pythonString="\\u"+hexString[2:]                                                    # replace 0x with \u to create python string which can be printed
        if i%16==0 or i==2:                                                                 # print periodic headings to keep track of tables
            print("\n\tpython\t\t\tx =\nhex\tstring\tdecimal\t\t0123456789ABCDEF\n"+
                "------------------------------------------------")                         
            outFile.write("\n\tpython\t\t\tx =\nhex\tstring\tdecimal\t\t0123456789ABCDEF\n"+
            "------------------------------------------------\n")                           # print same to file with carriage return
        for j in range(16):
            if (i*16+j)>=65534:break                                                        # last character in "plane 0 BMP" utf-8 is 65533
            try:                                                                            # try to add on char to string
                string=string+chr(i*16+j)
            except:                                                                         # if not add blank space
                string=string+" "
        try:                                                                                # print line tab formatted
            print(hexString+"\t"+pythonString+"\t"+str(i*16)+" - "+str(i*16+j)+" \t"+string)
            outFile.write(hexString+"\t"+pythonString+"\t"+str(i*16)+" - "+str(i*16+j)+" \t"+string+"\n")   #same to file but add carriage return
        except:
            print(hexString+"\t"+pythonString+"\t"+ str(i*16)+" - "+str(i*16+j)+" \t"+"not printable") # if line won't print, say so
            outFile.write(hexString+"\t"+pythonString+"\t"+str(i*16)+" - "+str(i*16+j)+" \t"+"not printable\n") # same to file with carriage return
    outFile.close()
main()
