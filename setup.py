#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('version', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

usr_share = '/usr/share'
if not os.access(usr_share, os.W_OK):
    usr_share = os.getenv("XDG_DATA_HOME", os.path.join(os.path.expanduser("~"), ".local", "share"))

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['digielectrum.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/digielectrum.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))


appdata_dir = util.appdata_dir()
if not os.access(appdata_dir, os.W_OK):
    appdata_dir = os.path.join(usr_share, "digielectrum")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]

for lang in os.listdir('data/wordlist'):
    data_files.append((os.path.join(appdata_dir, 'wordlist'), ['data/wordlist/%s' % lang]))


setup(
    name="DigiElectrum",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'pyasn1',
        'pyasn1-modules',
        'qrcode',
        'SocksiPy-branch',
        'tlslite'
    ],
    package_dir={
        'electrum_dgb': 'lib',
        'electrum_dgb_gui': 'gui',
        'electrum_dgb_plugins': 'plugins',
    },
    scripts=['digielectrum'],
    data_files=data_files,
    py_modules=[
        'electrum_dgb.account',
        'electrum_dgb.bitcoin',
        'electrum_dgb.blockchain',
        'electrum_dgb.bmp',
        'electrum_dgb.commands',
        'electrum_dgb.daemon',
        'electrum_dgb.i18n',
        'electrum_dgb.interface',
        'electrum_dgb.mnemonic',
        'electrum_dgb.msqr',
        'electrum_dgb.network',
        'electrum_dgb.network_proxy',
        'electrum_dgb.old_mnemonic',
        'electrum_dgb.paymentrequest',
        'electrum_dgb.paymentrequest_pb2',
        'electrum_dgb.plugins',
        'electrum_dgb.qrscanner',
        'electrum_dgb.scrypt',
        'electrum_dgb.simple_config',
        'electrum_dgb.synchronizer',
        'electrum_dgb.transaction',
        'electrum_dgb.util',
        'electrum_dgb.verifier',
        'electrum_dgb.version',
        'electrum_dgb.wallet',
        'electrum_dgb.x509',
        'electrum_dgb_gui.gtk',
        'electrum_dgb_gui.qt.__init__',
        'electrum_dgb_gui.qt.amountedit',
        'electrum_dgb_gui.qt.console',
        'electrum_dgb_gui.qt.history_widget',
        'electrum_dgb_gui.qt.icons_rc',
        'electrum_dgb_gui.qt.installwizard',
        'electrum_dgb_gui.qt.lite_window',
        'electrum_dgb_gui.qt.main_window',
        'electrum_dgb_gui.qt.network_dialog',
        'electrum_dgb_gui.qt.password_dialog',
        'electrum_dgb_gui.qt.paytoedit',
        'electrum_dgb_gui.qt.qrcodewidget',
        'electrum_dgb_gui.qt.qrtextedit',
        'electrum_dgb_gui.qt.receiving_widget',
        'electrum_dgb_gui.qt.seed_dialog',
        'electrum_dgb_gui.qt.transaction_dialog',
        'electrum_dgb_gui.qt.util',
        'electrum_dgb_gui.qt.version_getter',
        'electrum_dgb_gui.stdio',
        'electrum_dgb_gui.text',
        'electrum_dgb_plugins.btchipwallet',
        'electrum_dgb_plugins.cosigner_pool',
        'electrum_dgb_plugins.exchange_rate',
        'electrum_dgb_plugins.greenaddress_instant',
        'electrum_dgb_plugins.labels',
        'electrum_dgb_plugins.trezor',
        'electrum_dgb_plugins.virtualkeyboard',
    ],
    description="Lightweight Digibyte Wallet",
    author="dgb",
    author_email="myr@myr.myr",
    license="GNU GPLv3",
    url="http://digibyte.co",
    long_description="""Lightweight Digibyte Wallet"""
)
