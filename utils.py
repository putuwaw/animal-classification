import os


def combine_files(target_directory, output_file_name=None, file_ext=None):
    files = sorted(
        [
            os.path.join(target_directory, f)
            for f in os.listdir(target_directory)
            if os.path.isfile(os.path.join(target_directory, f))
        ]
    )

    if not files:
        print(f"No files found in target_directory {target_directory}")
        return

    combined_data = b""

    for file in files:
        with open(file, "rb") as f:
            combined_data += f.read()
        print(f"Added {file}")

    if output_file_name:
        output_file = f"{output_file_name}{file_ext}"
        with open(output_file, "wb") as output:
            output.write(combined_data)
        print(f"Combined all files into {output_file}")

    return combined_data


if __name__ == "__main__":
    tflite_model = combine_files(
        "tflite_chunks", output_file_name="tflite/model", file_ext=".tflite"
    )

    saved_model_variables = combine_files(
        "variable_chunks",
        output_file_name="saved_model/variables/variables",
        file_ext=".data-00000-of-00001",
    )
