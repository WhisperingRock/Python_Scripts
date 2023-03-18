import unittest
from logic_gates import buffer, inverter, and_gate, or_gate, nand_gate, nor_gate, xor_gate, xnor_gate


class logic_gates(unittest.TestCase):

    def test_buffer(self):
        self.assertTrue(buffer(1))
        self.assertFalse(buffer(0))

    def test_inverter(self):
        self.assertTrue(inverter(0))
        self.assertFalse(inverter(1))
        self.assertFalse(inverter(4))

    def test_and(self):
        self.assertEqual(and_gate(0,0), 0)
        self.assertEqual(and_gate(1, 0), 0)
        self.assertEqual(and_gate(0, 1), 0)
        self.assertEqual(and_gate(1, 1), 1)
        self.assertEqual(and_gate(7, 0), 0)
        self.assertEqual(and_gate(7, 100), 1)

    def test_or(self):
        self.assertEqual(or_gate(0,0), 0)
        self.assertEqual(or_gate(1, 0), 1)
        self.assertEqual(or_gate(0, 1), 1)
        self.assertEqual(or_gate(1, 1), 1)
        self.assertEqual(or_gate(7, 0), 1)
        self.assertEqual(or_gate(7, 100), 1)


    def test_nand(self):
        self.assertEqual(nand_gate(0,0), 1)
        self.assertEqual(nand_gate(1, 0), 1)
        self.assertEqual(nand_gate(0, 1), 1)
        self.assertEqual(nand_gate(1, 1), 0)
        self.assertEqual(nand_gate(7, 0), 1)
        self.assertEqual(nand_gate(7, 100), 0)

    def test_nor(self):
        self.assertEqual(nor_gate(0,0), 1)
        self.assertEqual(nor_gate(1, 0), 0)
        self.assertEqual(nor_gate(0, 1), 0)
        self.assertEqual(nor_gate(1, 1), 0)
        self.assertEqual(nor_gate(7, 0), 0)
        self.assertEqual(nor_gate(7, 100), 0)

    def test_xor(self):
        self.assertEqual(xor_gate(0,0), 0)
        self.assertEqual(xor_gate(1, 0), 1)
        self.assertEqual(xor_gate(0, 1), 1)
        self.assertEqual(xor_gate(1, 1), 0)
        self.assertEqual(xor_gate(7, 0), 1)
        self.assertEqual(xor_gate(7, 100), 0)


    def test_xnor(self):
        self.assertEqual(xnor_gate(0,0), 1)
        self.assertEqual(xnor_gate(1, 0), 0)
        self.assertEqual(xnor_gate(0, 1), 0)
        self.assertEqual(xnor_gate(1, 1), 1)
        self.assertEqual(xnor_gate(7, 0), 0)
        self.assertEqual(xnor_gate(7, 100), 1)

if __name__ == '__main__':
    unittest.main()