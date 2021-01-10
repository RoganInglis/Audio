import os
import sys
import soundfile as sf

from argparse import ArgumentParser

from src.utils.utils import timestretch


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
