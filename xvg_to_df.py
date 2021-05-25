import os


def xvg_2_csv(input):
    with open(input) as file, open('foo.csv', 'w') as f:
        for line in file:
            if line.startswith(('#', '@')):
                continue
            print(','.join(line.split()), file=f)
    df = pd.read_csv('foo.csv', header=None)
    os.remove('foo.csv')
    return df
