from Clss.Model.Records import Records
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import unittest


class TestRecords(unittest.TestCase):

    def setUp(self):
        self.seq1 = SeqRecord("CGGG", id="o1", description="organism1")
        self.seq2 = SeqRecord("ACGA", id="o1", description="organism1")
        self.seq3 = SeqRecord("ATGATCGA", id="o2", description="organism2")
        self.sequences = Records([self.seq1, self.seq2, self.seq3])

    def test_group(self):
        groups = self.sequences.group(6)
        expected_keys = set()
        expected_keys.add("cds")
        expected_keys.add("o1")
        # expect_groups = {"cds": [self.sequences.seqs[-1]], "o1": [[self.sequences.seqs[0]], [self.sequences.seqs[1]]]}
        self.assertEqual(expected_keys, groups.keys())
        self.assertEqual([self.seq3], groups["cds"])

    def test_filtr_organism_by_size(self):
        filtrated = self.sequences.filtr_organism_by_size("organism1", 2, 7)
        self.assertEqual([self.seq1, self.seq2], filtrated)