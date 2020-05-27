""" Test pdf matching.
"""
import os
from pathlib import Path
import shutil
import unittest
from pdfMatcher import is_pdf_file, list_pdf_files, merge_pdfs
from PyPDF2 import PdfFileWriter


class TestPdfMatcher(unittest.TestCase):
  def setUp(self):
    self.root = "/tmp/pdf_matcher_tests"
    self.dir1 = os.path.join(self.root, "dir1")
    if not os.path.isdir(self.dir1):
      os.makedirs(self.dir1)

    self.dir2 = os.path.join(self.root, "dir2")
    if not os.path.isdir(self.dir2):
      os.makedirs(self.dir2)

    self.outdir = os.path.join(self.root, "output")
    if not os.path.isdir(self.outdir):
      os.makedirs(self.outdir)

    Path(self.dir1, 'file1.txt').touch()
    Path(self.dir1, 'pdf-file1.pdf').touch()

    Path(self.dir2, 'code.py').touch()
    Path(self.dir2, 'pdf-file1.pdf').touch()
    Path(self.dir2, 'pdf-file2.pdf').touch()

  def tearDown(self):
    shutil.rmtree(self.root)

  def test_is_pdf_file(self):
    path_to_file = Path(self.dir2, 'pdf-file2.pdf')
    self.assertTrue(is_pdf_file(str(path_to_file)))

    path_to_file = Path(self.dir2, 'file2.txt')
    self.assertFalse(is_pdf_file(str(path_to_file)))

  def test_list_pdf_files(self):
    files = list_pdf_files(self.dir1)
    self.assertEqual(['pdf-file1.pdf'], files)

    files = list_pdf_files(self.dir2)
    self.assertEqual(['pdf-file1.pdf', 'pdf-file2.pdf'], files)

    self.assertRaises(ValueError, list_pdf_files, "/random/path")

  def test_merge_pdfs(self):
    pdf_writer = PdfFileWriter()
    pdf_writer.addBlankPage(width=72, height=72)

    path1 = str(Path(self.dir1, 'pdf-file1.pdf'))
    path2 = str(Path(self.dir2, 'pdf-file1.pdf'))

    with open(path1, mode="wb") as output_file:
      pdf_writer.write(output_file)

    with open(path2, mode="wb") as output_file:
      pdf_writer.write(output_file)

    merge_pdfs(path1, path2, self.outdir)

    self.assertTrue(os.path.isfile(os.path.join(self.outdir, 'pdf-file1.pdf')))


if __name__ == '__main__':
  unittest.main()
