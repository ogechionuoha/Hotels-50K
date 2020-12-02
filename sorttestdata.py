import shutil
import os
import csv


def copyfiles(origin_folder, csv_file,target_folder, countryname=None):
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
    if not os.path.exists('./images/dataset/test'):
        os.mkdir('./images/dataset/test')
        os.mkdir('./images/dataset/test/not_uk')
        os.mkdir('./images/dataset/test/uk')

    test_source_folder = './images/test/unoccluded'

    #move UK images
    print('Sorting UK images...')
    uk_test_csvfile = './input/uk_not_uk/test_uk.csv'
    test_uk_folder = './images/dataset/test/uk'
    copyfiles(test_source_folder, uk_test_csvfile, test_uk_folder)
    print('Finished!')
        
    #move Not UK images 
    print('Sorting NOT UK images...')
    notuk_test_csvfile = './input/uk_not_uk/test_not_uk.csv'
    test_notuk_folder = './images/dataset/test/not_uk'
    copyfiles(test_source_folder, notuk_test_csvfile, test_notuk_folder)
    print('Finished!')
        