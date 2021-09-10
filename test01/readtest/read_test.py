def delblankline(infile, outfile):
    infopen = open(infile, 'r')
    outfopen = open(outfile, 'w')

    lines = infopen.readlines()
    for line in lines:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    infopen.close()
    outfopen.close()


if __name__ == '__main__':
    # print('---')
    # # f = open('log2.txt', 'r')
    # with open('log2.txt', 'r') as f:
    #     a = f.read()
    #
    # print(type(a), a)
    with open('log2.txt', 'r', encoding='GBK') as f:
        a = f.read()
    print(type(a),a)
