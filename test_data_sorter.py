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
    if not os.path.exists('./images/uk_us'):
        os.mkdir('./images/uk_us')
        if not os.path.exists('./images/uk_us/test'):
            os.mkdir('./images/uk_us/test')
        #os.mkdir('./images/uk_not_uk/test')

    test_source_folder = './images/test/unoccluded'
    #move UK images
    print('Sorting UK images...')
    uk_test_csvfile = './input/uk_not_uk/test_uk.csv'
    uk_test_target_folder = './images/uk_not_uk/test/uk'
    copyfiles(uk_test_csvfile, test_source_folder, uk_test_target_folder)
    print('Finished!')
        
    #move Not UK images 
    print('Sorting NOT UK images...')
    notuk_test_csvfile = './input/uk_not_uk/test_not_uk.csv'
    notuk_test_target_folder = './images/uk_not_uk/test/us'
    copyfiles(notuk_test_csvfile, test_source_folder, notuk_test_target_folder)
    print('Finished!')

    #move UK images
    print('Sorting UK images...')
    uk_test_csvfile = './input/uk_not_uk/test_uk.csv'
    uk_test_target_folder = './images/uk_us/test/uk'
    copyfiles(uk_test_csvfile, test_source_folder, uk_test_target_folder)
    print('Finished!')
        
    #move Not UK images 
    print('Sorting US images...')
    notuk_test_csvfile = './input/uk_not_uk/test_not_uk.csv'
    notuk_test_target_folder = './images/uk_us/test/us'
    copyfiles(notuk_test_csvfile, test_source_folder, notuk_test_target_folder, 'United States of America')
    print('Finished!')
        