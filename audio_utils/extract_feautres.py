import os
import os.path
import subprocess


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
files_list = os.listdir(os.path.join(ROOT_DIR, 'Audio_ang'))


def preprocess(some_file):

    """ output_file_name - a .csv file contains an annotation
    f_config - config file in opensmile, see openSMILE-2.1.0/config/ to chose another configuration"""

    output_dir_name = os.path.join(ROOT_DIR)
    output_file_name = str('audiofeatures_ang.csv')
    output_file = os.path.join(output_dir_name, output_file_name)
    f_config = os.path.join(ROOT_DIR, 'openSMILE-2.1.0', 'config', 'IS13_ComParE.conf')


    """ Check the system to provide equivalent functionality across platforms (Windows/Unix) """

    if os.name == 'nt':
        process = os.path.join(ROOT_DIR, 'openSMILE-2.1.0', 'bin', 'Win32', 'SMILExtract_Release.exe')
    else:
        process = os.path.join(ROOT_DIR, 'openSMILE-2.1.0', 'bin', 'linux_x64_standalone_static', 'SMILExtract')

    """ Start openSMILE: path_to_opensmilie -C config_file -I path_to_input_file -O path_to_output_file -args """

    subprocess.call([str(process), "-C", str(f_config), "-I", str(some_file), "-csvoutput", str(output_file),
                     "-instname", str(some_file)])


for audiofiles in files_list:
    if str(audiofiles).endswith('.wav'):
        input_file = os.path.join(ROOT_DIR, 'Audio_ang', str(audiofiles))
        print('Processing %s' % input_file)
        preprocess(input_file)
