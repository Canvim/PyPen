import sys
import os
from unittest import main, TestCase
from subprocess import call, DEVNULL
from pyperlib.utils.math import *

class TestExamples(TestCase):

    def test_util_functions(self):
        cool_print("Testing util functions...")
        # Constants ok
        self.assertAlmostEqual(PI, 3.141, 2)
        self.assertAlmostEqual(TAU, 6.283, 2)
        self.assertAlmostEqual(E, 2.718, 2)
        print("constants OK")

        # clamp ok
        self.assertEqual(clamp(110, 0, 100), 100)
        self.assertEqual(clamp(-110, 0, 100), 0)
        print("clamp OK")

        # lerp ok
        self.assertEqual(lerp(0, 100, 1), 100)
        self.assertEqual(lerp(0, 100, 1.5), 100)
        self.assertEqual(lerp(100, 200, 1.5), 200)
        self.assertEqual(lerp(100, 200, 0.1), 110)
        self.assertNotEqual(lerp(0, 100, 1.5), 150)
        print("lerp OK")

        # lerp_unclamped ok
        self.assertEqual(lerp_unclamped(0, 100, 1.5), 150)
        self.assertEqual(lerp_unclamped(100, 200, 1.1), 210)
        print("lerp_unclamped OK")

    def test_all_examples(self):
        cool_print("Trying to run pyper command with timeout on all sketches in examples/")
        examples_dir_path = os.path.join(os.path.split(
            os.path.realpath(__file__))[0], "..", "examples")

        for example_filename in os.listdir(examples_dir_path):
            if os.path.splitext(example_filename)[1] == ".py":
                print()
                print(f"Running {example_filename}")
                return_code = run_pyper_sketch(
                    os.path.join(examples_dir_path, example_filename))
                self.assertEqual(return_code, 0)
    
    def test_test_scene(self):
        cool_print("Running tests/test_scene.py")
        return_code = run_pyper_sketch(os.path.join(os.path.split(
            os.path.realpath(__file__))[0], "..", "tests", "test_scene.py"))
        
        self.assertEqual(return_code, 0)


def run_pyper_sketch(example_path, custom_timeout=2):
    timeout_time = custom_timeout
    arguments = ["pyper", example_path, "--timeout", str(timeout_time)]

    print(' '.join(arguments))
    return_code = call(arguments, timeout=timeout_time*2, stdout=DEVNULL, stderr=sys.stderr)
    return return_code


def cool_print(message):
    print()
    print()
    print()
    print(f"==== {message} ====")
    print()

if __name__ == "__main__":
    cool_print("STARTING PYPER TESTS")
    main()
