import argparse
import configparser

def parse_arguments():
    parser = argparse.ArgumentParser(description='Script to automate MadAnalysis 5 recasting.')
    parser.add_argument('-p', '--config', type=str, required=True, help='Path to the configuration file.')
    args = parser.parse_args()
    return args.config  # Asegúrate de devolver sólo el string del path al archivo de configuración.

def parse_config(config_file):
    """Parse the given configuration file."""
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

