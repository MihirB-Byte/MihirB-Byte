import os
import argparse

def main(database: str, url_list_file: str):
    print("we are going to work with in Page 1"+ database)
    print("we are going to scan _in Page 1"+ url_list_file)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db","--database", help="SQLite file name")
    parser.add_argument("-i","--input", help="file containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database = database_file, url_list_file= input_file)




