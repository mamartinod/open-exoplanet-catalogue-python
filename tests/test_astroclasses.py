import unittest
from astroclasses import Parameters


class TestListFiles(unittest.TestCase):

    def create_Parameter_object(self):

        params = {
            'RA': 111111,
            'DEC': 222222,
            'name': 'monty',
        }

        paramObj = Parameters()
        paramObj.params.update(params)

        return paramObj

    def test_addParam_works_no_duplicate(self):

        paramObj = self.create_Parameter_object()

        paramObj.addParam('radius', '12')

        self.assertEqual(paramObj.params['radius'], '12')

    def test_addParam_works_recognised_duplicate_name(self):  # ie name which is a known and accepted duplicate

        paramObj = self.create_Parameter_object()

        paramObj.addParam('name', 'python')

        self.assertEqual(paramObj.params['name'], 'monty')

        self.assertEqual(paramObj.params['altnames'], ['python'])

    def test_addParam_works_unrecognised_duplicate(self):  # a unknown duplicate to delete (and log)

        paramObj = self.create_Parameter_object()

        paramObj.addParam('RA', 333333)

        self.assertEqual(paramObj.params['RA'], 111111)

        # TODO test to ensure the rejection is logged


if __name__ == '__main__':
    unittest.main()

