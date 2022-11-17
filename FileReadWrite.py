
import os

def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists

def writeFile(filePath, textToWrite):
    fileHandle = open(filePath, 'w')
    fileHandle.write(textToWrite)
    fileHandle.close()
    
def readFile(filePath):
    if not fileExists(filePath):
        print ('The file, ' + filePath + ' does not exist - cannot read it.')
        return ""
    fileHandle = open(filePath, 'r')
    data = fileHandle.read()
    fileHandle.close()
    return data

def openFileForWriting(filePath):
    fileHandle = open(filePath, 'w')
    return fileHandle

def writeALine(fileHandle, lineToWrite):
    lineToWrite = lineToWrite + '\n'
    return fileHandle.write(lineToWrite)
    
def openFileForReading(filePath):
    if not fileExists(filePath):
        print('The file, ' + filePath + ' does not exist - cannot read it.')
        return ''
    fileHandle = open(filePath, 'r')
    return fileHandle

def readALine(fileHandle):
    theLine = fileHandle.readline()
    if not theLine:
        return False
    if theLine.endswith('\n'):
        theLine = theLine.rstrip('\n')
    return theLine

def writetoendofline(lines, line_no, append_txt):
    lines[line_no] = lines[line_no].replace('\n', '') + append_txt + '\n'
    
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'a')
    out.writelines(lines)
    out.close()

def closeFile(fileHandle):
    fileHandle.close()
