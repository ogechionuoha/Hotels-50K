import shutil
import os
import csv


def copyfiles(csv_file, origin_folder, target_folder, countryname=None):
    """
    Move files listed in csv_file from origin folder to target folder
    """
    #get hotel to chain data

    
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)

    #go through each image in uk.csv
    with open(csv_file, 'r') as csvfile:
        images = csv.reader(csvfile)

        for row in images:
            if countryname==None or countryname==(row[-1]).strip():
                #generate origin path??
                chain = hotel_to_chain[row[1]]
                filename = row[0]+'.'+row[2].split('.')[-1]
                origin = os.path.join(origin_folder,chain,row[1],row[3],filename)
                target = os.path.join(target_folder,filename)
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
    if not os.path.exists('../notebooks/images/'):
        os.mkdir('../notebooks/images/')
    if not os.path.exists('../notebooks/images/uk_not_uk'):
        os.mkdir('../notebooks/images/uk_not_uk')
    if not os.path.exists('../notebooks/images/uk_not_uk/train'):
        os.mkdir('../notebooks/images/uk_not_uk/train')
        #os.mkdir('./images/uk_not_uk/test')

    train_source_folder = './images/train/'
    #move UK images
    print('Sorting UK images...')
    uk_train_csvfile = './input/uk_not_uk/train_uk.csv'
    uk_train_target_folder = '../notebooks/images/uk_not_uk/train/uk'
    copyfiles(uk_train_csvfile, train_source_folder, uk_train_target_folder)
    print('Finished!')
        
    #move Not UK images 
    print('Sorting NOT UK images...')
    notuk_train_csvfile = './input/uk_not_uk/train_not_uk.csv'
    notuk_train_target_folder = '../notebooks/images/uk_not_uk/train/not_uk'
    copyfiles(notuk_train_csvfile, train_source_folder, notuk_train_target_folder)
    print('Finished!')
        
