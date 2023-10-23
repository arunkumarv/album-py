#!/opt/local/bin/python
from move_duplicates import move_duplicates
import sys, getopt

def help():
   print ('python main.py -i <source folder> -o <destination folder>')
   print ('eg: main.py /Users/akv/MyPictures -o /Users/akv/Duplicates')

def main(argv):
   source_folder = ''
   destination_folder = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      help()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         help()
         sys.exit()
      elif opt in ("-i", "--ifile"):
         source_folder = arg
      elif opt in ("-o", "--ofile"):
         destination_folder = arg
   if not source_folder or not destination_folder:
      help()
   else:
      move_duplicates(source_folder=source_folder, destination_folder=destination_folder)

if __name__ == "__main__":
   main(sys.argv[1:])