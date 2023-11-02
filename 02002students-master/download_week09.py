import os
import sys

if not os.path.split(os.getcwd())[1].startswith('02002students'):
    print("Oh no, you are not in the 02002students folder.")
    print("Please open the 02002students folder in VS code and run the script again.")
    sys.exit(1) # Exit with error code 1

try:
    import unitgrade # type: ignore
    import dtumathtools # type: ignore
except ImportError as e:
    print("Oh no, Python encountered a problem during importing unitgrade")
    print("This means that your current python has never had the cp package installed.")
    print("Please select a different Python through the Command Palette (Ctrl+Shift+P) and choose ""Python: Select Interpreter"".")
    print("Try all the Pythons you can choose and run the script from them")
    print("")
    print("If you have not yet followed step 5 of the installation instructions from week 1 please do so now. Here is a link:")
    print("https://cp.compute.dtu.dk/installation/installation.html#step-5-install-the-course-toolbox-and-software-packages")
    sys.exit(1) # Exit with error code 1
try:
    import cp.ex00 # type: ignore
except ImportError as e:
    print("Oh no, Python encountered a problem during importing cp.") 
    import site
    for site_path in site.getsitepackages():
        egg_path = os.path.join(site_path, "cp.egg-link")
        if os.path.exists(egg_path):
            with open(egg_path, "r") as f:
                print("It tried looking in the following folder, but could not find the cp package there:")
                print(f.read())
    print("")
    print("This most likely means that you have moved or renamed the 02002students folder since following step 5 of the installation guide.")
    print("Please move/rename the students folder back so it can be found at the this path again")
    print("If you have tried running the script with EVERY Python interpreter, and this does still not work, make sure you have followed the installation instructions from week 1. Here is a link:")
    print("https://cp.compute.dtu.dk/installation/installation.html#step-5-install-the-course-toolbox-and-software-packages")
    sys.exit(1) # Exit with error code 1

cp_path = os.path.dirname(cp.__file__)

print("cp folder located at", cp_path)
assert "02002public" not in cp_path, "Probably running on the lecturers computer, don't do that."

import base64
import io
import zipfile

# Replace this with your base64-encoded string


def add_new_files(encoded_zip_data):
    # Decode the base64 string to binary data
    zip_binary_data = base64.b64decode(encoded_zip_data)

    # Create an in-memory file-like object from the binary data
    zip_file_like = io.BytesIO(zip_binary_data)

    # You can now work with the zip file in memory
    with zipfile.ZipFile(zip_file_like, 'r') as zip_file:
        
        # Iterate over the file list
        for file in zip_file.namelist():
            if file == '.gitignore' or file.endswith('/'):
                continue
            assert file.startswith('cp/'), file

            # Extract the file from the zip archive (for example, the first file)
            file_content = zip_file.read(file)
            out_path = os.path.join(cp_path, file[3:])

            # Make sure we don't overwrite files that are already there, except for tests
            if (not os.path.exists(out_path)) or (file.startswith('cp/tests/')) or (file.startswith('cp/project')):
                os.makedirs(os.path.dirname(out_path), exist_ok=True)

                # Check if the file is already up to date
                if (os.path.exists(out_path)):
                    with open(out_path, "rb") as existing_file:
                        # Replace Windows line endings with Unix line endings
                        existing_content = existing_file.read().replace(b'\r\n', b'\n')
                    if existing_content == file_content:
                        continue
                # Write the file to disk
                with open(out_path, 'wb') as f:
                    f.write(file_content)
                    print("Writing to", out_path)

    # We don't need the binary data anymore, and close the in-memory file-like object
    zip_file_like.close()
    print("Files are up to date")
    print()
    print("Successfully completed!")

# Run the function on the base64-encoded version of the zip file
add_new_files("""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dGFuZ2xlLnBrbFVUBQABlGhBZWtgmVrFAAG1UzR6pMJTU7MNLEOKEvOKcxJLMvPSg1KTSxLz0nNSp/RwFaeWhBY45yQWF09pm9LDUpKZmwpkuNtLHwAbkMHYI1CSWlwSn5tflhpfBtSYXwRSyAbUkFpUAmTWTslgzGBrm5LBAtRm97UBrK1UDwBQSwECAAAKAAAAAABOrl9XAAAAAAAAAAAAAAAAAwAJAAAAAAAAABAAAAAAAAAAY3AvVVQFAAGUaEFlUEsBAgAACgAAAAAATq5fVwAAAAAAAAAAAAAAAAgACQAAAAAAAAAQAAAAKgAAAGNwL2V4MDkvVVQFAAGUaEFlUEsBAgAACgAAAAAATq5fV8STgtolAAAAJQAAABMACQAAAAAAAQAAAAAAWQAAAGNwL2V4MDkvX19pbml0X18ucHlVVAUAAZRoQWVQSwECAAAKAAAACABOrl9Xipd5AHMAAACZAAAAFAAJAAAAAAABAAAAAAC4AAAAY3AvZXgwOS9yZWN0YW5nbGUucHlVVAUAAZRoQWVQSwECAAAKAAAACABOrl9X0y9s/qkAAADvAAAAEQAJAAAAAAABAAAAAABmAQAAY3AvZXgwOS92ZWN0b3IucHlVVAUAAZRoQWVQSwECAAAKAAAAAABOrl9XAAAAAAAAAAAAAAAACQAJAAAAAAAAABAAAABHAgAAY3AvdGVzdHMvVVQFAAGUaEFlUEsBAgAACgAAAAgATq5fV63Q2qMMBQAAGx0AABgACQAAAAAAAQAAAAAAdwIAAGNwL3Rlc3RzL3Rlc3RzX3dlZWswOS5weVVUBQABlGhBZVBLAQIAAAoAAAAAAE6uX1cAAAAAAAAAAAAAAAAYAAkAAAAAAAAAEAAAAMIHAABjcC90ZXN0cy91bml0Z3JhZGVfZGF0YS9VVAUAAZRoQWVQSwECAAAKAAAACABOrl9X90h8PWMAAAB4AAAALQAJAAAAAAAAAAAAAAABCAAAY3AvdGVzdHMvdW5pdGdyYWRlX2RhdGEvV2VlazA5VGVzdENvcm5lcnMucGtsVVQFAAGUaEFlUEsBAgAACgAAAAgATq5fV0SVL7tvAAAAhQAAADgACQAAAAAAAAAAAAAAuAgAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1dlZWswOVRlc3RSZWN0YW5nbGVQZXJpbWV0ZXIucGtsVVQFAAGUaEFlUEsBAgAACgAAAAgATq5fVy0IfOJpAAAAewAAACwACQAAAAAAAAAAAAAAhgkAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1dlZWswOVRlc3RWZWN0b3IucGtsVVQFAAGUaEFlUEsBAgAACgAAAAgATq5fV1GrDWx2AAAAhQAAADYACQAAAAAAAAAAAAAAQgoAAGNwL3Rlc3RzL3VuaXRncmFkZV9kYXRhL1dlZWswOVRyYW5zbGF0aW5nUmVjdGFuZ2xlLnBrbFVUBQABlGhBZVBLBQYAAAAADAAMANcDAAAVCwAAKAA5NDE5ZWFmMDY3YTFlZTlkN2QyMjkwMzUxMTI5NmNlZmExZjVmMzU3""")