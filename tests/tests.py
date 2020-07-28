import sys
import os
from unittest import main, TestCase
from subprocess import call, DEVNULL
from pypen.utils.math import *
from pypen import settings


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
        cool_print("Trying to run pypen command with timeout on all sketches in examples/")
        examples_dir_path = os.path.join(os.path.split(
            os.path.realpath(__file__))[0], "..", "examples")

        for example_filename in os.listdir(examples_dir_path):
            if os.path.splitext(example_filename)[1] == ".py":
                print()
                print("Running {}".format(example_filename))
                return_code = run_pypen_sketch(
                    os.path.join(examples_dir_path, example_filename))
                self.assertEqual(return_code, 0)
                print("OK")

    def test_all_test_scenes(self):
        cool_print("Trying to run pypen command with timeout on all sketches in tests/test_scenes/")
        test_scenes_dir_path = os.path.join(os.path.split(
            os.path.realpath(__file__))[0], "test_scenes")

        filename_to_return_code = {
            "test_empty_file.py": 1,
            "test_colors.py": 0,
            "test_no_start_or_update.py": 1
        }

        for test_filename in os.listdir(test_scenes_dir_path):
            if os.path.splitext(test_filename)[1] == ".py":
                print()
                print("Running {}".format(test_filename))
                return_code = run_pypen_sketch(
                    os.path.join(test_scenes_dir_path, test_filename))
                self.assertEqual(return_code, filename_to_return_code[test_filename] if test_filename in filename_to_return_code else 0)
                print("OK")

    def test_init(self):
        cool_print("Trying to run pypen --init")
        arguments = ["pypen", "--init", os.path.join(os.path.split(os.path.realpath(__file__))[0], "test_scenes", "test_init.py")]
        return_code = call(arguments, timeout=4000, stdout=DEVNULL, stderr=sys.stderr)
        print(' '.join(arguments))
        self.assertEqual(return_code, 0)
        print("OK")


def run_pypen_sketch(example_path, custom_timeout=2000, use_stdout=False):
    timeout_time = custom_timeout
    arguments = ["pypen", example_path, "--timeout", str(timeout_time)]

    print(' '.join(arguments))
    return_code = call(arguments, timeout=timeout_time*4, stdout=DEVNULL if not use_stdout else sys.stdout, stderr=sys.stderr)
    return return_code


def cool_print(message):
    print()
    print()
    print()
    print("==== {} ====".format(message))
    print()


if __name__ == "__main__":
    cool_print("STARTING PYPEN TESTS")
    main()
