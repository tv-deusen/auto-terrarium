import os
import sys

from setuptools import setup, find_packages, Extension

from app.dht import platform_detect

BINARY_COMMANDS = [
    'build_ext',
    'build_clib',
    'bdist',
    'bdist_dumb',
    'bdist_rpm',
    'bdist_wininst',
    'bdist_wheel',
    'install'
]


def is_binary_install():
    do_binary = [command for command in BINARY_COMMANDS if command in sys.argv]
    return len(do_binary) > 0


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# TODO: Eventually just remove the platform detection module
platform = platform_detect.platform_detect()
pi_version = 2


# Pick the right extension to compile based on the platform.
extensions = []
if not is_binary_install():
    print('Skipped loading platform-specific extensions (we are generating a cross-platform source distribution).')
elif platform == platform_detect.RASPBERRY_PI:
    # Get the Pi version (1 or 2)
    if pi_version is None:
        pi_version = platform_detect.pi_version()
    # Build the right extension depending on the Pi version.
    if pi_version == 1:
        print("Only Raspberry Pi v2 is supported")
        sys.exit(1)
    elif pi_version == 2:
        extensions.append(Extension("Adafruit_DHT.Raspberry_Pi_2_Driver",
                                    ["dht/ccode/Raspberry_Pi_2_Driver.c", "dht/ccode/common_dht_read.c", "dht/ccode/Raspberry_Pi_2/pi_2_dht_read.c", "dht/ccode/Raspberry_Pi_2/pi_2_mmio.c"],
                                    libraries=['rt'],
                                    extra_compile_args=['-std=gnu99']))
    elif pi_version == 3:
        extensions.append(Extension("Adafruit_DHT.Raspberry_Pi_2_Driver",
                                    ["dht/ccode/Raspberry_Pi_2_Driver.c", "dht/ccode/common_dht_read.c", "dht/ccode/Raspberry_Pi_2/pi_2_dht_read.c", "dht/ccode/Raspberry_Pi_2/pi_2_mmio.c"],
                                    libraries=['rt'],
                                    extra_compile_args=['-std=gnu99']))
    else:
        raise RuntimeError('Detected Pi version that has no appropriate driver available.')
else:
    print('Could not detect if running on the Raspberry Pi.  If this failure is unexpected, you can run again with --force-pi or --force-bbb parameter to force using the Raspberry Pi or Beaglebone Black respectively.')
    sys.exit(1)

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

# Call setuptools setup function to install package.
setup(name='auto-terrarium',
      version='0.1',
      author='Tom Van Deusen',
      author_email='tvdeusen0892@gmail.com',
      description='',
      long_description  = read('README.md'),
      license           = 'MIT',
      classifiers       = classifiers,
      url='',
      packages          = find_packages(),
      ext_modules=extensions, install_requires=['dht'])
