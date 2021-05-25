def xvg_to_csv(input, output):
    with open(input) as file, open(output, 'w') as f:
        for line in file:
            if line.startswith(('#', '@')):
                continue
            print(','.join(line.split()), file = f)

    
    
