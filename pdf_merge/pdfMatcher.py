""" Merge all pdf files in two directories based on their filename.
"""
import argparse
import os
from typing import List
from PyPDF2 import PdfFileMerger


def is_pdf_file(path_to_file: str) -> bool:
  """ Check whether path to file is a pdf

  Args:
      path_to_file (str): [description]

  Returns:
      bool: [description]
  """
  if path_to_file.endswith(".pdf"):
    return True
  else:
    return False


def list_pdf_files(path_to_dir: str) -> List[str]:
  """ List all pdf files in a directory.

  Args:
      path_to_dir (str): path to directory with pdf files

  Returns:
      List[str]: list of pdf files in alphabetic order, filename only
  """
  if not os.path.isdir(path_to_dir):
    raise ValueError("Invalid folde")

  pdf_files = []
  for filename in os.listdir(path_to_dir):
    if is_pdf_file(filename):
      pdf_files.append(filename)

  pdf_files = sorted(pdf_files)

  return pdf_files


def merge_pdfs(path_to_pdf1: str, path_to_pdf2: str, output_dir: str):
  """ Create a new pdf file which contains concatenated content of 1st and 2nd pdf

  Args:
      path_to_pdf1 (str): path to 1st pdf file
      path_to_pdf2 (str): path to 2nd pdf file
      output_dir (str): path to output directory
  """
  pdf_merger = PdfFileMerger()
  print("Merging: ", path_to_pdf1, path_to_pdf2)
  pdf_merger.append(path_to_pdf1, import_bookmarks=False)
  pdf_merger.append(path_to_pdf2, import_bookmarks=False)

  path_to_merged = os.path.join(output_dir, os.path.basename(path_to_pdf1))

  with open(path_to_merged, "wb") as ostream:
    pdf_merger.write(ostream)


if __name__ == '__main__':

  parser = argparse.ArgumentParser(description="Merge pdf files of two dirs")
  parser.add_argument("--dir1", required=True, help="path to 1st dir.")
  parser.add_argument("--dir2", required=True, help="path to 2nd dir.")
  parser.add_argument("--output_dir", required=True, help="path to output dir")
  FLAGS, _ = parser.parse_known_args()

  if not os.path.exists(FLAGS.output_dir):
    os.makedirs(FLAGS.output_dir)

  files1 = list_pdf_files(FLAGS.dir1)
  files2 = list_pdf_files(FLAGS.dir2)
  common_files = list(set(files1) & set(files2))

  for filename in common_files:
    path_to_pdf1 = os.path.join(FLAGS.dir1, filename)
    path_to_pdf2 = os.path.join(FLAGS.dir2, filename)
    merge_pdfs(path_to_pdf1, path_to_pdf2, FLAGS.output_dir)
