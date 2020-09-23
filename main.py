"""
Named Entity Recognition
"""
import csv
import os

# Example File
exfile = os.path.abspath('data/input/Ep 33 Edburg_otter.ai.txt')
outputfolder = os.path.abspath('data/output')


def parseauthorline(line):
    """ return line dict for author """

    author = line[:line.find(" ")]
    time = line[line.find("  "):].lstrip()

    linedict = {'type': 'author',
                'author': author,
                'time': time}

    return linedict


def parsetranscriptline(line):
    """ return line dict for transcript """

    linedict = {'type': 'transcript',
                'transcript': line}

    return linedict


def parseline(line):
    """ return line and type """

    line = line.strip()

    pos_colon = line[-3:-2]
    pos_secs = line[-2:]

    if pos_colon == ':' and pos_secs.isnumeric():
        linedict = parseauthorline(line)
        return linedict

    elif pos_colon != ':' and len(line) > 1:
        linedict = parsetranscriptline(line)
        return linedict


def writecsv(*, file, header, linesdict):
    """ write csv """

    with open(file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')

        # write csvheader
        csvwriter.writerow(header)

        for linedict in linesdict.values():

            # print(f'linedict: {linedict}')
            # breakpoint()

            csvwriter.writerow(linedict.values())


def main():
    linesdict = {}

    with open(exfile, 'r') as f:

        # build list of all nonblank lines
        lines = [line for line in f if line.strip() != ""]

        authors = []
        transcripts = []
        episode = {'episode': os.path.basename(exfile)}
        header = ('type', 'author', 'time', 'transcript', 'episode')

        for idx, line in enumerate(lines, 1):
            if len(line) > 1:
                linedict = parseline(line)

                if linedict['type'] == 'transcript':
                    transcripts.append(linedict)
                elif linedict['type'] == 'author':
                    authors.append(linedict)

        for i in range(len(authors)):
            newdict = {**authors[i], **transcripts[i + 1], **episode}
            linesdict.update({i: newdict})

    # export to csv
    outputfile = os.path.join(outputfolder, os.path.basename(exfile).replace(".txt", ".csv"))
    writecsv(file=outputfile, header=header, linesdict=linesdict)


if __name__ == '__main__':
    main()
