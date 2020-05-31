# Merge PDF files
Assumptions:
- You are given two folders with pdf files - lets call them dir1 and dir2
- The filenames of corresponding pdfs are identical in both folders

Prerequisties:
```
$ conda create -n pdfmerge python=3.7
$ conda activate pdfmerge
$ conda install -c conda-forge pypdf2
```

Run
```
python pdfMatcher.py --dir1 /path/to/dir1 --dir2 /path/to/dir2 --output_dir /path/to/output/dir
```
- This will append all pdf files in dir2 to the corresponding files in dir1
- Note that all files in dir1 and dir2 will NOT be removed
- You can find the merged files at */path/to/output/dir*

