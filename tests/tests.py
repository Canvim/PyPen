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
    print(f"Running 'pyper {os.path.join('examples', os.path.split(example_path)[1])}'")
    timeout_time = 2

    return_code = call(["pyper", example_path, "--timeout", str(timeout_time)], timeout=timeout_time*2.5)
    return return_code


if __name__ == "__main__":
    main()