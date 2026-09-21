#!/usr/bin/env python3
import argparse
import sys
from move_duplicates import move_duplicates

def main():
    parser = argparse.ArgumentParser(
        description="Find and move duplicate files efficiently using 3-tier hash detection."
    )
    parser.add_argument("-i", "--ifile", "--source", required=True, help="Source folder to scan for duplicates")
    parser.add_argument("-o", "--ofile", "--destination", required=True, help="Destination folder to move duplicates to")
    parser.add_argument("-d", "--dry-run", action="store_true", help="Preview duplicates without actually moving them")

    args = parser.parse_args()

    move_duplicates(
        source_folder=args.ifile,
        destination_folder=args.ofile,
        dry_run=args.dry_run
    )

if __name__ == "__main__":
    main()