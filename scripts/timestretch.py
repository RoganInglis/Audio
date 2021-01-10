import os
import sys
import numpy as np
import soundfile as sf

from scipy.interpolate import interp1d
from argparse import ArgumentParser


def timestretch(data, stretch=1.25):
    x = np.linspace(0, 1, data.shape[0])
    f = interp1d(x, data, axis=0, kind='cubic')

    x_stretched = np.linspace(0, 1, int(data.shape[0] * stretch))
    data_stretched = f(x_stretched)

    # Re-normalise data
    data_stretched /= np.max(np.abs(data_stretched), axis=(0, 1))

    return data_stretched


def main(argv):
    parser = ArgumentParser()
    parser.add_argument('-f', '--filename', type=str, required=True, help='Path to file to timestretch')
    parser.add_argument('-s', '--stretch', type=float, default=1.25, help='Timestretch factor')
    args = parser.parse_args()

    # Load file
    data, rate = sf.read(args.filename)

    # Timestretch
    data_stretched = timestretch(data, stretch=args.stretch)

    # Write file
    file, ext = os.path.splitext(args.filename)
    out_filename = '{}_stretched_{}{}'.format(file, str(args.stretch).replace('.', '-'), ext)
    sf.write(out_filename, data_stretched, rate)
    print('Done!')


if __name__ == '__main__':
    main(sys.argv[1:])
