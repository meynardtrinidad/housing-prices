import pandas as p


input_path = "./input/melb_data.csv"
output_path = "./output/result.txt"


def main():
    csv_data = p.read_csv(input_path)
    result = csv_data.describe()

    with open(output_path, "w") as f:
        f.write(result.to_string())


if __name__ == "__main__":
    main()
