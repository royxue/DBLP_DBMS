"""
Filter the first 3000 data for further extraction
"""


def main():
    xml = open('dblp.xml', 'r')
    output = open('new.xml', 'w+')

    count = 0

    lines = xml.readlines()
    for l in lines:
        if 'mdate' in l and 'key' in l:
            count += 1
        
        if count == 3001:
            break

        output.write(l)

    output.write('</dblp>')
    xml.close()
    output.close()


if __name__ == '__main__':
    main()