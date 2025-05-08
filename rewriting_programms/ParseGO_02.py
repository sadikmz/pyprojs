import argparse
import re
import logging
from typing import List, TextIO

# Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# Argument parser setup
parser = argparse.ArgumentParser(description='Parse OBO file and extract GO term relations.')
parser.add_argument('obo_file', type=str, help='Path to the input OBO file')
parser.add_argument('out_file', type=str, help='Path to the output file')
parser.add_argument('relation_file', type=str, help='Path to the relation file')

# Add optional arguments
opt = parser.add_argument_group('optional arguments')
opt.add_argument('-r', '--relation_file', default="go_relation_file.txt", type=str,
                 help='Choose name of relation file, default to go_relation_file.txt', metavar='')
# opt.add_argument('-h', '--help', action='help', help='show this help message and exit')
# opt.add_argument('-h', '--help', action='help', help='show this help message and exit')  # Argument for displaying help message

# Parse the arguments
args = parser.parse_args()


class ParseOBO:
    """ This class is taking an OBO file as input and will output a file with GO relations. """

    def __init__(self):
        """ Initialize the ParseOBO class. """
        super(ParseOBO, self).__init__()
        self.go_pattern = re.compile(r'^GO:\d{7}$')

    def _validate_go_term(self, go_term: str) -> bool:
        """Validate if string matches GO term format (GO:0000000)."""
        return bool(self.go_pattern.match(go_term))

    def _writeRow(self, info: List[str], outf: TextIO) -> None:
        """ Write a row of information to the output file. """
        if info:
            outf.write("\t".join(info) + "\n")

    def parseOBO(self, infile: str, outf: str, relation_file: str) -> None:
        """ Parse the OBO file and write GO relations to the output files. """
        try:
            with open(infile, "r") as in_f, \
                    open(relation_file, "w") as rel_f, \
                    open(outf, "w") as out_f:

                # Write headers
                rel_f.write("go_c\tgo_p\n")
                out_f.write("go_id\tdescription\tname_space\tdefinition\n")

                info = []
                go = ""

                for row in in_f:
                    row = row.strip()

                    if row == "[Term]":
                        self._writeRow(info, out_f)
                        info = []
                        continue

                    if row == "[Typedef]":
                        self._writeRow(info, out_f)
                        break

                    inf = row.split(": ", 1)
                    if len(inf) != 2:
                        continue

                    key, value = inf
                    if key == "id":
                        if go == "GO:2001317":
                            print(go)
                        go = value
                        info = [value]
                    elif key == "name":
                        info.append(value)
                    elif key == "namespace":
                        info.append(value)
                    elif key == "def":
                        info.append(value)
                    elif key == "alt_id":
                        self._writeRow(info, out_f)
                        info[0] = value
                    elif key == "is_a":
                        goR = value.split(" ")[0]
                        rel_f.write(f"{go}\t{goR}\n")

                # Write the last term if exists
                self._writeRow(info, out_f)

        except FileNotFoundError:
            logger.error(f"Input file not found: {infile}")
            raise
        except PermissionError:
            logger.error("Unable to write to output files")
            raise

            outf.close()
            # relF.close()

# Main execution
if __name__ == "__main__":
    # Create an instance of ParseOBO
    parseOBO = ParseOBO()
    # Parse the OBO file
    parseOBO.parseOBO(args.obo_file, args.out_file, args.relation_file)