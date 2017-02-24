#!/usr/bin/env python
'''
In order to run a c# script from the command line
(without this program) you do the following:
mcs fileName.cs (this turns code into exectuable?)
dotnet new
dotnet run (this compiles the code)

'''
import os,sys

greet = "Hello Robo! <3 \n Using ean\'s Python script to run .net compiler"
fairWell = "Goodbye for now."

if (len(sys.argv) > 1):
    print(greet)
    prg = sys.argv[1]
    os.system("mcs %s"%(prg))
    os.system("dotnet new")
   #os.system("dotnet restore")
    os.system("dotnet run")

print(fairWell)
