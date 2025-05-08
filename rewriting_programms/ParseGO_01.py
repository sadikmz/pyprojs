#!/usr/bin/python

# Import necessary modules
import sys
import argparse

# source: https://github.com/irusri/ParseGO/blob/master/ParseGO.py

# Create an argument parser
parser = argparse.ArgumentParser(description='Parse go relation OBO file and create go relation and go gene database file', add_help=False)

# Add required arguments
req = parser.add_argument_group('required arguments')
req.add_argument('obo_file', type=str, help='The latest obo file')  # Argument for the OBO file
req.add_argument('out_file', type=str, help='name of output')  # Argument for the output file

# Add optional arguments
opt = parser.add_argument_group('optional arguments')
opt.add_argument('-r', '--relation_file', default="go_relation_file.txt", type=str, help='Choose name of relation file, default to go_relation_file.txt', metavar='')  # Argument for the relation file
opt.add_argument('-h', '--help', action='help', help='show this help message and exit')  # Argument for displaying help message

# Parse the arguments
args = parser.parse_args()

# Define the ParseOBO class
class ParseOBO(object):
    """ This class is taking an OBO file as input and will output a file with GO relations. """
    
    def __init__(self):
        """ Initialize the ParseOBO class. """
        super(ParseOBO, self).__init__()

    def _writeRow(self, info, outf):
        """ Write a row of information to the output file. """
        if len(info) > 0:  # Check if info is not empty
            outf.write("\t".join(info) + "\n")  # Write the info to the output file
            # add column separator and column names "GO_terms", "GO_name", "GO_namespace", "GO_definition"
            # outf.write("\t".join(["GO_terms", "GO_name", "GO_namespace", "GO_definition"]) + "\n")
            
    def parseOBO(self, infile, outf, relation_file):
        """ Parse the OBO file and write GO relations to the output files. """
        with open(infile, "r") as in_f:  # Open the input OBO file for reading
            relF = open(relation_file, "w")  # Open the relation file for writing
            outf = open(outf, "w")  # Open the output file for writing
            relF.write("\t".join(["go_c", "go_p"]) + "\n")  # Write the header to the relation file
            info = []  # Initialize an empty list for storing info
            go = ""  # Initialize an empty string for storing GO term
            for row in in_f:  # Iterate over each row in the input file
                row = row.strip("\n")  # Remove newline character from the row
                if row == "[Term]":  # Check if the row indicates a new term
                    self._writeRow(info, outf)  # Write the current info to the output file
                    info = []  # Reset the info list
                inf = row.split(": ")  # Split the row into key and value
                if inf[0] == "id":  # Check if the key is 'id'
                    if go == "GO:2001317":  # Debugging statement for a specific GO term
                        print(go)
                    go = inf[1]  # Store the GO term
                    info.append(inf[1])  # Add the GO term to the info list
                if inf[0] == "name":  # Check if the key is 'name'
                    info.append(inf[1])  # Add the name to the info list
                if inf[0] == "namespace":  # Check if the key is 'namespace'
                    info.append(inf[1])  # Add the namespace to the info list
                if inf[0] == "def":  # Check if the key is 'def'
                    info.append(inf[1])  # Add the definition to the info list
                if inf[0] == "alt_id":  # Check if the key is 'alt_id'
                    self._writeRow(info, outf)  # Write the current info to the output file
                    info[0] = inf[1]  # Update the GO term in the info list
                if inf[0] == "is_a":  # Check if the key is 'is_a'
                    goR = inf[1].split(" ")[0]  # Extract the related GO term
                    try:
                        relF.write(go + "\t" + goR + "\n")  # Write the relation to the relation file
                    except KeyError:
                        pass
                if row == "[Typedef]":  # Check if the row indicates the start of type definitions
                    """ Stop reading file when trailing type definitions are explained, no more terms exist after these. """
                    self._writeRow(info, outf)  # Write the current info to the output file
                    break  # Stop reading the file

            # Close the output files
            outf.close()
            relF.close()

# Main execution
if __name__ == "__main__":
    # Create an instance of ParseOBO
    parseOBO = ParseOBO()
    # Parse the OBO file
    parseOBO.parseOBO(args.obo_file, args.out_file, args.relation_file)