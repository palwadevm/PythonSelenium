# Define global myList
global ExecPropertes
class TestProperties:
    # Test Run Id
    strTestRunId = ""

    # Project Name
    strProjectName = ""

    def __init__(self, strProperiesFilePath):
        dictPropertiesFromFile = self.__ParseTestConfgFile(strProperiesFilePath)

    def __ParseTestConfgFile(self, strProperiesFilePath):
        ExecPropertes = {}
        try:
            with open(strProperiesFilePath) as configFile:
                lines = configFile.readlines()
            for line in lines:
                blnStartComment = False
                blnEndComment = True
                if line.find("<!--") == -1:
                    blnStartComment = True
                    blnEndComment = False
                if line.find("-->") == -1:
                    blnStartComment = False
                    blnEndComment = True
                if blnStartComment == False and blnEndComment == True :
                    if line.find("=") != -1:
                        ExecPropertes[line.split("=")[0]] = line.split("=")[1]
            return lines
        except(FileNotFoundError, IOError):
            print("Invalid Test Config File - " + strProperiesFilePath)
