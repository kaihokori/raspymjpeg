import argparse
from core.process import start_background_process


def main(args):
    """Main function to start the background process using provided config file."""
    config_filepath = args.config_filepath
    try:
        start_background_process(config_filepath)
    except KeyboardInterrupt:
        print("Server stopped.")


if __name__ == "__main__":
    # Argument parser for reading config file from command line input
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        nargs=1,
        default=None,
        dest="config_filepath",
        help="Provide a filepath to the configuration file. If none provided, will use defaults.",
    )
    args = parser.parse_args()
    main(args)
