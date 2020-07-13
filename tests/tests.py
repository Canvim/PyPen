import sys
import os
from unittest import main, TestCase
from subprocess import call

class TestExamples(TestCase):

    def test_all_examples(self):
        examples_dir_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "..", "examples")

        for example_filename in os.listdir(examples_dir_path):
            if os.path.splitext(example_filename)[1]  == ".py":
                return_code = run_individual_example(os.path.join(examples_dir_path, example_filename))
                self.assertEqual(return_code, 0)

def run_individual_example(example_path):
    timeout_time = 2
    arguments = ["pyper", example_path, "--timeout", str(timeout_time)]

    print(' '.join(arguments))
    return_code = call(arguments, timeout=timeout_time*2)
    return return_code


if __name__ == "__main__":
    main()