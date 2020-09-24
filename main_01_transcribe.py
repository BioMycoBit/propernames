"""
Named Entity Recognition
"""
import csv
import os

# Example File
inputfolder = os.path.abspath('data/input')
outputfolder = os.path.abspath('data/output/episodes')


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

    files = [os.path.join(inputfolder, file) for file in os.listdir(inputfolder)]

    for file in files:

        print(f'file: {file}')

        with open(file, 'r') as f:

            # build list of all nonblank lines
            lines = [line for line in f if line.strip() != ""]

            authors = []
            transcripts = []
            episode = {'episode': os.path.basename(file)}
            header = ('type', 'author', 'time', 'transcript', 'episode')

            for idx, line in enumerate(lines, 1):
                if len(line) > 1:
                    linedict = parseline(line)

                    if linedict:
                        if linedict['type'] == 'transcript':
                            transcripts.append(linedict)
                        elif linedict['type'] == 'author':
                            authors.append(linedict)

            # range (0:lowest number (authors or transcripts -- should be same)
            for i in range(min(len(authors), len(transcripts))):

                newdict = {**authors[i], **transcripts[i], **episode}
                linesdict.update({i: newdict})

            # author qc
            author_qc = [author['author'] for author in authors if author['author'] == 'Unknown']

            if len(author_qc) > 0:
                print(f'{"":>5} Unknown Author Found [Occurrences: {len(author_qc)}]')


        # export to csv
        outputfile = os.path.join(outputfolder, os.path.basename(file).replace(".txt", ".csv"))
        writecsv(file=outputfile, header=header, linesdict=linesdict)


if __name__ == '__main__':
    main()
