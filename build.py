import os
import shutil
import subprocess
import sys

SIZE_DECLARATION_STUB = "SIZE = "
SIZE_DECLARATION_DEFAULT = SIZE_DECLARATION_STUB + "1000000"
COMPILATION_COMMAND = "g++"
BINARY_DIRECTORY = "bin"
GENERATED_SOURCE_DIRECTORY = "gensrc"

class microBenchPermutation:
    def __init__(self, benchmarkArrayCount, fileName):
        self.Count = benchmarkArrayCount
        self.FileName = fileName
        self.Args = self.GenerateArguments()

    def GenerateArguments(self):
        suffix = ""
        if sys.platform == "win32":
            suffix = ".exe"
        outputArgument = "-o " + BINARY_DIRECTORY + "/" + self.FileName + suffix
        compilationTargetArgument = GENERATED_SOURCE_DIRECTORY + "/" + self.FileName + ".cpp"
        return [compilationTargetArgument, outputArgument]

def generateDefaultPermutations():
    milli = microBenchPermutation( 10000000, "millibench")
    nano = microBenchPermutation( 1000000, "nanobench")
    pico = microBenchPermutation( 100000, "picobench")
    return [milli, nano, pico]

def createBinaryDirectory():
    try:
        shutil.rmtree(BINARY_DIRECTORY)
    except:
        None
    try:
        os.mkdir(BINARY_DIRECTORY)
    except:
        print("FATAL: Could not create binary directory. Is it open?")
        quit()

def createGeneratedSourceDirectory():
    try:
        shutil.rmtree(GENERATED_SOURCE_DIRECTORY)
    except:
        None
    try:
        os.mkdir(GENERATED_SOURCE_DIRECTORY)
    except:
        print("FATAL: Could not create generated source directory. Is it open?")
        quit()

def getMicroBenchContents():
    microBenchFile = None
    try:
        microBenchFile = open("microBench.cpp", "r")
    except:
        print("FATAL: Could not open source file. Did you rename it? Is it locked?")
        quit()
    microBenchContents = microBenchFile.read()
    microBenchFile.close()
    return microBenchContents

def createBuildTargetSourceFiles(sourceContents, microBenchPermList):
    for permutation in microBenchPermList:
        targetContents = sourceContents.replace(SIZE_DECLARATION_DEFAULT, SIZE_DECLARATION_STUB + str(permutation.Count))
        fileName = GENERATED_SOURCE_DIRECTORY + "/" + permutation.FileName + ".cpp"
        targetFile = open(fileName, "w")
        targetFile.write(targetContents)
        targetFile.close()

def compileBinaryFiles(microBenchPermList):
    for permutation in microBenchPermList:
        subprocess.run(COMPILATION_COMMAND, permutation.Args)

def main():
    createBinaryDirectory()
    createGeneratedSourceDirectory()
    contents = getMicroBenchContents()
    defaultPermList = generateDefaultPermutations()
    createBuildTargetSourceFiles(contents, defaultPermList)
    compileBinaryFiles(defaultPermList)

main()
    





