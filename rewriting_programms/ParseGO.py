#!/usr/bin/python
import sys
import argparse as argparse

# source: https://github.com/irusri/ParseGO/blob/master/ParseGO.py

parser = argparse.ArgumentParser(description='Parse go relation OBO file and create go relation and go gene database file', add_help=False)
req = parser.add_argument_group('required arguments')
req.add_argument('obo_file', type=str, help='The latest obo file')
req.add_argument('out_file', type=str, help='name of output')

opt = parser.add_argument_group('optional arguments')
opt.add_argument('-r', '--relation_file',default="go_relation_file.txt",type=str, help='Choose name of relation file, default to go_relation_file.txt', metavar='')
opt.add_argument('-h','--help', action='help', help='show this help message and exit')

args = parser.parse_args()

class ParseOBO(object):
    """ This class is taking an OBO file as input and will output a file with GO relations. """
    def __int__(self):
        super(ParseOBO, self).__init__()

    def _writeRow(self,info,outf):
        if len(info) > 0:
            outf.write("\t".join(info)+"\n")

    def parseOBO(self,infile,outf,relation_file):
        with open(infile,"r") as in_f:
            relF = open(relation_file, "w")
            outf = open(outf, "w")
            relF.write("\t".join(["go_c","go_p"])+"\n")
            info = []
            go = ""
            for row in in_f:
                row = row.strip("\n")
                if row == "[Term]":
                    self._writeRow(info,outf)
                    info = []
                inf = row.split(": ")
                if inf[0] == "id":
                    if go == "GO:2001317":
                        print(go)
                    go = inf[1]
                    info.append(inf[1])
                if inf[0] == "name":
                    info.append(inf[1])
                if inf[0] == "namespace":
                    info.append(inf[1])
                if inf[0] == "def":
                    info.append(inf[1])
                if inf[0] == "alt_id":
                    self._writeRow(info,outf)
                    info[0] = inf[1]
                if inf[0] == "is_a":
                    goR = inf[1].split(" ")[0]
                    try:
                        relF.write(go+"\t"+goR+"\n")
                    except KeyError:
                        pass
                if row == "[Typedef]":
                    """ Stop reading file when trailing type definitions are explained, no more terms exist after these."""
                    self._writeRow(info,outf)
                    break

            outf.close()

        return

if __name__=="__main__":
    """ Parse the obo file to retrieve the necessary GO information for each term and the go relation file"""
    parseOBO = ParseOBO()
    parseOBO.parseOBO(args.obo_file,args.out_file,args.relation_file)


                    

