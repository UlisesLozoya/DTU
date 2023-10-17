import os
import urllib.request
import shutil

try:
    import cp.ex00
    import dtumathtools
    import unitgrade
except ImportError as e:
    print("Oh no, Python encountered a problem during importing.")
    print("This is required for being able to submit the projects.")
    print("Please make sure that you followed the installation instructions from last week, especially steps 4 and 5.")
    print("Are you SURE that you have done those steps?")
    print("")
    print("If you are sure, it might be because this script is running with a different python than the one you installed the cp module for.")
    print("Try with ""python3 download_week02.py"" instead of ""python download_week02.py"".")
    print("You can start doing the exercises by implementing the functions yourself, and asking one of the TAs for help once they arrive.")

    print("The error message was:")
    raise e

cp_path = os.path.dirname(cp.__file__)

try:
    import cp.ex02.taylor
except ImportError:
    pass
else: # If the import succeeded
    print("You have downloaded the 02002students folder a bit earlier than expected, so we will now move the extra files to a folder called ""unused_files"".")
    paths_to_move = ["ex02/fibonacci.py",
                     "ex02/taylor.py",
                     "ex02/taylor_variant1.py",
                     "ex02/taylor_variant2.py",
                     "ex03", 
                     "ex04",
                     "ex09",
                     "ex10",
                     "project2",
                     "project5",
                     "ex01/examples.py",
                     ] + [f"tests/tests_week{i:02d}.py" for i in range(1, 13)]

    unused_dir = os.path.join(cp_path, "unused_files")
    for local_path in paths_to_move:
        path = os.path.join(unused_dir, local_path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        os.rename(os.path.join(cp_path, local_path), path)

download_files = ["ex02/__init__.py",
                  "ex02/full_name.py",
                  "ex02/name_length.py",
                  "ex02/next_thousand.py",
                  "ex02/normal_weight.py",
                  "ex02/survival_temperature.py",
                  "ex02/unit_conversion.py",
                  "ex02/wind_chill.py",
                  "project0/project0_grade.py",
                  "project0/unitgrade_data/HelloWorld.pkl",
                  "project1/__init__.py",
                  "project1/project1_grade.py",
                  "project1/project1_tests.py",
                  "project1/unitgrade_data/TestHadlock.pkl",
                  "project1/unitgrade_data/TestNormalWeight.pkl",
                  "project1/unitgrade_data/TestSurvivalTemperature.pkl",
                  "project1/unitgrade_data/TestUnitConversion.pkl",
                  "tests/tests_week02.py",
                  "tests/unitgrade_data/SayHelloWorld.pkl",
                  "tests/unitgrade_data/Week02FullName.pkl",
                  "tests/unitgrade_data/Week02Hadlock.pkl",
                  "tests/unitgrade_data/Week02NameLength.pkl",
                  "tests/unitgrade_data/Week02NextThousand.pkl",
                  "tests/unitgrade_data/Week02NormalWeight.pkl",
                  "tests/unitgrade_data/Week02SurvivalTemperature.pkl",
                  "tests/unitgrade_data/Week02UnitConversion.pkl",
                  "tests/unitgrade_data/Week02WindChill.pkl",
                  "ex02/hadlock.py"]

try: 
    import cp.ex02.hadlock
except ImportError:
    pass
else:
    print("Script has already successfully run once, so we will not download the files again.")
    exit()

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

base_url = "https://gitlab.compute.dtu.dk/cp/02002students/-/raw/master/cp/"

print("Downloading files...")
for file_name in download_files:
    out_path = os.path.join(cp_path, file_name)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with urllib.request.urlopen(base_url + file_name) as response, open(out_path, 'wb') as out_file:        
        shutil.copyfileobj(response, out_file)
print("Sucessfully updated files to week 02")