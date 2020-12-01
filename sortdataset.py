import shutil
import os
import csv


def copyfiles(source_folder, train_csvfile, train_folder, valid_folder):
    """
    Move files listed in csv_file from origin folder to target folder
    """
    #get hotel to chain data

    
    if not os.path.exists(train_folder):
        os.mkdir(train_folder)

    if not os.path.exists(valid_folder):
        os.mkdir(valid_folder)

    #go through each image in train.csv
    with open(train_csvfile, 'r') as csvfile:
        images = csv.reader(csvfile)

        for row in images:
            #generate origin path??
            chain = hotel_to_chain[row[1]]
            filename = row[0]+'.'+row[2].split('.')[-1]
            origin = os.path.join(source_folder,chain,row[1],row[3],filename)
            if row[3].strip() == 'traffickcam':
                target = os.path.join(valid_folder,filename)
            else:
                target = os.path.join(train_folder,filename)
            #check if it exists in the origin but not in target, move
            if os.path.isfile(origin) and not os.path.exists(target):
                shutil.copyfile(origin, target)

if __name__ == '__main__':

    #create hotel to chain dictionary
    with open('./input/dataset/hotel_info.csv','r') as hotel_f:
        hotel_reader = csv.reader(hotel_f)
        _ = next(hotel_reader,None)
        hotel_to_chain = {}
        for row in hotel_reader:
            hotel_to_chain[row[0]] = row[2]

    #create folders for uk and not uk
    if not os.path.exists('./images/dataset/'):
        os.mkdir('./images/dataset')
        os.mkdir('./images/dataset/train')
        os.mkdir('./images/dataset/train/uk')
        os.mkdir('./images/dataset/train/not_uk')
        os.mkdir('./images/dataset/valid')
        os.mkdir('./images/dataset/valid/uk')
        os.mkdir('./images/dataset/valid/not_uk')

    

    source_folder = './images/train/'
    #move UK images
    print('Sorting UK images...')
    uk_train_csvfile = './input/uk_not_uk/train_uk.csv'
    train_uk_folder = './images/dataset/train/uk'
    valid_uk_folder = './images/dataset/valid/uk'
    copyfiles(source_folder, uk_train_csvfile, train_uk_folder, valid_uk_folder)
    print('Finished!')
        
    #move Not UK images 
    print('Sorting NOT UK images...')
    notuk_train_csvfile = './input/uk_not_uk/train_not_uk.csv'
    train_notuk_folder = './images/dataset/train/not_uk'
    valid_notuk_folder = './images/dataset/valid/not_uk'
    copyfiles(source_folder, uk_train_csvfile, train_notuk_folder, valid_notuk_folder)
    print('Finished!')
        