import re, json

class Jasonify:
    def regex_replace(self, text):
        
        # Remove 'END OF ...' comment
        regex = re.compile(r' -- end of (.+)')
        text = re.sub(regex, "\n", text)

        # Remove {} Empty square brackets
        regex = re.compile(r'\s+{\s+}')
        text = re.sub(regex, '""', text)

        # Adding Qoutes to KEY that are digits
        regex = re.compile(r'\s(\d+) :')
        text = re.sub(regex, r'"\g<1>" :', text)

        # Remove , just before }
        regex = re.compile(r'(,\s+})')
        text = re.sub(regex, r'\n}', text)

        # Remove \" with \'
        regex = re.compile(r'(\\\")')
        text = re.sub(regex, "\'", text)

        # "Sequence"2"Red" -> "Sequence 2 Red"
        regex = re.compile('(mission) :')
        text = re.sub(regex, r'"\g<1>" :', text)

        return text
    
    def get_miz(self, filedata):
        with open(filename, 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('[', '')
        filedata = filedata.replace(']', '')
        filedata = filedata.replace('=', ':')
        filedata = self.regex_replace(filedata)
        # filedata = filedata.replace(r"{\n}", "''")
        filedata = "{\n" + filedata + "\n}"

        # Write the file out again
        with open('miz.json', 'w') as file:
            file.write(filedata)