import argparse
import logging
import numpy
import numpy as np


def read_imu(filename):
    ACC = []
    GYRO = []
    MAG = []
    try:
        with open(f"{filename}", "r") as f:
            lines = f.readlines()
            for line in lines:
                if "acc" in line.lower():
                    ACC.append(list(map(float, line.split(":")[1].split(","))))

                if "rot" in line.lower():
                    GYRO.append(list(map(float, line.split(":")[1].split(","))))

                if "mag" in line.lower():
                    MAG.append(list(map(float, line.split(":")[1].split(","))))

        print("Data storage complete")

    except Exception as e:
        logging.error(e)
        logging.warning("File doesn't exist!")

    return np.array(ACC)*9.8, np.array(GYRO), np.array(MAG)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="input file")
    args = parser.parse_args()

    acc, gyro, mag = read_imu(args.input)
    print(len(acc), len(gyro), len(mag))
    print(acc)
