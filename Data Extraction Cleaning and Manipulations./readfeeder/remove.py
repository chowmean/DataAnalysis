#! /usr/bin/python
delete_list = ["href", " gt;&lt;img", "src", "lt;img", "/&gt;&lt;/a&gt;&" ,"lt;br/&gt;&lt;a", "lt;br/&gt;&", "/&gt;&", "]]>", "     ", "...&" ,"lt;p&gt;&lt;", "lt;/a&gt;at", "'", "&amp;#039;s", ".&"]
fin = open("/home/hduser/Desktop/final.txt", "r")
fout = open("/home/hduser/Desktop/outfile.txt", "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
