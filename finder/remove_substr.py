import os
import argparse
from typing import List


def get_filenames(path_to_folder: str) -> List[str]:
  """ Get the full path to all files in a given Folder.

  Args:
      path_to_folder (str)

  Returns:
      List[str]: Contains all files in specified directory
  """
  if not os.path.isdir(path_to_folder):
    raise ValueError("Folder does not exist.")

  filenames = []
  for filename in os.listdir(path_to_folder):
    path_to_file = os.path.join(path_to_folder, filename)
    if os.path.isfile(path_to_file):
      filenames.append(path_to_file)

  return filenames


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--dir", required=True, help="path to folder containing files")
  parser.add_argument("--substr", required=True, type=str, help="substr to be removed from filename")
  FLAGS, _ = parser.parse_known_args()

  filenames = get_filenames(FLAGS.dir)
  for filename in filenames:
    filename_purged = filename.replace(FLAGS.substr, "")
    os.rename(filename, filename_purged)
