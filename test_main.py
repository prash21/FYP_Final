import unittest
import main


class TestMain(unittest.TestCase):

    def test_get_input1(self):
        """Test for get_input1 function. Test for two different types of inputs. Basic testing
        is done for this function because comprehensive testing done when the UI takes these inputs
        in the first place."""

        # First test using the following values
        # input_values = "0", "8", "50", "20", "81", "53", "01", "83", "51", "0.0"
        # Below is the expected result
        expected_result = [0.0, 8.0, 50.0, 20.0, 81.0, 53.0, 1.0, 83.0, 51.0, 0.0]
        # Run the test
        input1_test1 = main.get_input1("0", "8", "50", "20", "81", "53", "01", "83", "51", "0.0")
        self.assertEqual(input1_test1, expected_result)

        # Second test using the following values
        # input_values = 0.0, "8", "50", "20.1", 81.33, "53", "01", 25, "51", "0.0"
        # Below is the expected result
        expected_result = [0.0, 8.0, 50.0, 20.1, 81.33, 53.0, 1.0, 25.0, 51.0, 0.0]
        # Run the test
        input1_test1 = main.get_input1(0.0, "8", "50", "20.1", 81.33, "53", "01", 25, "51", "0.0")
        self.assertEqual(input1_test1, expected_result)

    def test_get_input2(self):
        """Test for get_input2 function. Test for two different types of inputs. Basic testing
        is done for this function because comprehensive testing done when the UI takes these inputs
        in the first place."""

        # First test using the following values
        # input_values = "0", "8", "50", "20", "81", "53", "01", "83", "51", "No"
        # Below is the expected result
        expected_result = [0.0, 8.0, 50.0, 20.0, 81.0, 53.0, 1.0, 83.0, 51.0, "No"]
        # Run the test
        input2_test1 = main.get_input2("0", "8", "50", "20", "81", "53", "01", "83", "51", "No")
        self.assertEqual(input2_test1, expected_result)

        # Second test using the following values
        # input_values = 0.0, "8", "50", "20.1", 81.33, "53", "01", 25, "51", "SEVERE"
        # Below is the expected result
        expected_result = [0.0, 8.0, 50.0, 20.1, 81.33, 53.0, 1.0, 25.0, 51.0, "SEVERE"]
        # Run the test
        input2_test2 = main.get_input2(0.0, "8", "50", "20.1", 81.33, "53", "01", 25, "51", "SEVERE")
        self.assertEqual(input2_test2, expected_result)

    def test_classifier_model(self):
        """Test the classifier_model function. Various sets of inputs will be given as input,
        and the expected result will be tested. 3 different sets (3 tests) of input will be used here.
        Note that erroneous input is handled before values are passed onto this function, and testing
        for that is done separately (see documentation)"""

        df = main.df

        # Test 1
        # Expected output
        expected_result = "High Risk"
        # Run the test
        classifier_model_test1 = main.classifier_model(df, 53, 90, 175, 29.3, 1, 80, 0, 0, 0, 1, 0.7, 8, 7,
                                                       15.6, 4.7, 39, 261, 50, 0, 0, 0, 0, 0, 0, "No", 0, 0, 0, 0)
        self.assertEqual(classifier_model_test1, expected_result)

        # Test 2
        # Expected output
        expected_result = "High Risk"
        # Run the test
        classifier_model_test2 = main.classifier_model(df, 65, 72, 150, 32, 1, 70, 0, 0, 1, 1, 1, 18, 26,
                                                       12.4, 3.8, 45, 227, 50, 1, 0, 0, 0, 0, 0, "No", 0, 0, 0, 0)
        self.assertEqual(classifier_model_test2, expected_result)

        # Test 3
        # Expected output
        expected_result = "Low Risk"
        # Run the test
        classifier_model_test3 = main.classifier_model(df, 56, 73, 173, 24.39, 0, 75, 1, 1, 0, 0, 1.3, 22, 6,
                                                       14.4, 3.2, 28, 230, 35, 0, 0, 0, 0, 0, 0, "sEvEre", 0, 0, 0, 0)
        self.assertEqual(classifier_model_test3, expected_result)


if __name__ == '__main__':
    unittest.main()
