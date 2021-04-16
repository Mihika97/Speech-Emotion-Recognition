def get_emotion(file_path):


    item = file_path
    if item[20:-16] == '02' and int(item[32:-4]) % 2 == 0:
        return 'shrill_calm'
    if item[20:-16] == '02' and int(item[32:-4]) % 2 == 0:
        return 'shrill_calm'
    if item[20:-16] == '02' and int(item[32:-4]) % 2 == 1:
        return 'low_calm'
    if item[20:-16] == '03' and int(item[32:-4]) % 2 == 0:
        return 'shrill_happy'
    if item[20:-16] == '03' and int(item[32:-4]) % 2 == 1:
        return 'low_happy'
    if item[20:-16] == '04' and int(item[32:-4]) % 2 == 0:
        return 'shrill_sad'
    if item[20:-16] == '04' and int(item[32:-4]) % 2 == 1:
        return 'low_sad'
    if item[20:-16] == '05' and int(item[32:-4]) % 2 == 0:
        return 'shrill_angry'
    if item[20:-16] == '05' and int(item[32:-4]) % 2 == 1:
        return 'low_angry'
    if item[20:-16] == '06' and int(item[32:-4]) % 2 == 0:
        return 'shrill_fearful'
    if item[20:-16] == '06' and int(item[32:-4]) % 2 == 1:
        return 'low_fearful'
    if item[20:-16] == '01' and int(item[32:-4]) % 2 == 0:
        return 'shrill_neutral'
    if item[20:-16] == '01' and int(item[32:-4]) % 2 == 1:
        return 'low_neutral'
    if item[20:-16] == '07' and int(item[32:-4]) % 2 == 0:
        return 'shrill_disgusted'
    if item[20:-16] == '07' and int(item[32:-4]) % 2 == 1:
        return 'low_disgusted'
    if item[20:-16] == '08' and int(item[32:-4]) % 2 == 0:
        return 'shrill_surprised'
    if item[20:-16] == '08' and int(item[32:-4]) % 2 == 1:
        return 'low_surprised'
    if item[:1] == 'a':
        return 'low_angry'
    if item[:1] == 'f':
        return 'low_fearful'
    if item[:1] == 'h':
        return 'low_happy'
    if item[:1] == 'n':
        return 'low_neutral'
    if item[:2] == 'su':
        return 'low_surprised'





