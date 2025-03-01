=========================================
DigiElectrum - Electrum DGB
=========================================

.. image:: https://img.shields.io/github/v/release/josansorex/Electrum-DGB?style=flat-square
   :target: https://github.com/josansorex/Electrum-DGB/releases/tag/v1.3.4
   :alt: Release

.. image:: https://img.shields.io/github/v/tag/josansorex/Electrum-DGB?style=flat-square
   :target: https://github.com/josansorex/Electrum-DGB/releases/tag/v1.3.4
   :alt: Tags

.. image:: https://img.shields.io/github/license/josansorex/Electrum-DGB?style=flat-square
   :target: https://github.com/josansorex/Electrum-DGB/blob/master/LICENCE
   :alt: License

Download
--------

.. raw:: html

   <table style="border: 2px solid #ccc; border-collapse: collapse; margin: 1em 0;">
     <tr>
       <td style="border: 1px solid #ccc; padding: 10px; vertical-align: top;">
         <strong>Windows</strong><br>
         <a href="LINK_WINDOWS">
           <img src="https://img.shields.io/badge/DigiElectrum%20for-Windows-blue?style=for-the-badge&logo=windows" alt="Download DigiElectrum for Windows">
         </a>
       </td>
       <td style="border: 1px solid #ccc; padding: 10px; vertical-align: top;">
         <strong>macOS</strong><br>
         <a href="LINK_MACOS">
           <img src="https://img.shields.io/badge/DigiElectrum%20for-macOS-silver?style=for-the-badge&logo=apple" alt="Download DigiElectrum for macOS">
         </a>
       </td>
       <td style="border: 1px solid #ccc; padding: 10px; vertical-align: top;">
         <strong>Linux</strong><br>
         <a href="LINK_LINUX">
           <img src="https://img.shields.io/badge/DigiElectrum%20for-Linux-green?style=for-the-badge&logo=linux" alt="Download DigiElectrum for Linux">
         </a>
       </td>
     </tr>
   </table>




Overview
--------

DigiElectrum is a lightweight DigiByte client that prioritizes speed, reliability, and user security. Unlike traditional full-node wallets, DigiElectrum does not require downloading the entire DigiByte blockchain. This ensures swift setup and low resource usage, making it an ideal solution for users with limited bandwidth or storage.

- **Licence**: GNU GPL v3  
- **Electrum Author**: Thomas Voegtlin  
- **Electrum Digibyte Author**: DigiByte Team  
- **Language**: Python  
- **Electrum Digibyte Homepage**: TBD  

Compatibility & Requirements
---------------------------

- **Best with:** Python 2.7 and PyQT/QT4  
- **Not supported:** Python 3 or QT5  
- A stable internet connection to synchronize with remote servers.  
- Basic command-line knowledge is recommended to follow the installation steps below.

Key Features
------------

1. **Fast and Lightweight**  
   - Connects to remote DigiByte nodes, avoiding long blockchain downloads.
   - Designed for quick startup and minimal resource consumption.

2. **Enhanced Security**  
   - Private keys are stored locally and never leave your device.
   - Supports passphrase encryption to secure your wallet file.

3. **Multiple Seed Options**  
   - Standard and SegWit seeds for enhanced address capabilities (if relevant to DigiByte).
   - Easy seed backup and restoration.

4. **Customizable Fees**  
   - Adjust network fees per transaction based on current network conditions.
   - Estimate fees in real-time for faster or cheaper transactions.

5. **Portable and Flexible**  
   - Run directly from source or install system-wide.
   - Perfect for USB or offline usage when combined with cold storage best practices.


.. _Getting Started:

1. GETTING STARTED
------------------

This section outlines the basic steps needed to install dependencies and run DigiElectrum on your system.

.. code-block:: bash

   # Install required Python dependencies:
   sudo pip install ecdsa slowaes ltc-scrypt pyasn1 pyasn1-modules

   # Clone and install qubit-hash-python:
   git clone https://github.com/obigal/qubit-hash-python
   cd qubit-hash-python
   sudo python setup.py install
   cd ..

   # Clone and install groestl_hash_python:
   git clone https://bitbucket.org/cryptopools/groestl_hash_python
   cd groestl_hash_python
   sudo python setup.py install
   cd ..

   # Clone and install python_skein_hash:
   git clone https://github.com/CryptoRepairCrew/python_skein_hash
   cd python_skein_hash
   sudo python setup.py install
   cd ..

   # Finally, clone and prepare electrum-dgb:
   git clone https://github.com/digibyte/electrum-dgb
   cd electrum-dgb
   pyrcc4 icons.qrc -o gui/qt/icons_rc.py

   # You can run DigiElectrum from the current directory:
   ./digielectrum

   # Or install DigiElectrum so it's available globally:
   sudo python setup.py install
   digielectrum

.. note::

   If you encounter permission issues on Linux or macOS, consider adding ``--user`` flag or using a virtual environment.  

.. _Usage Guide:

2. USAGE GUIDE
--------------

Once installed, DigiElectrum offers a range of command-line and graphical options to manage your DigiByte wallet.

- **Graphical Interface**:  
  Launch using the ``digielectrum`` command (or ``./digielectrum`` if running from source).  
  1. Create a new wallet or restore from an existing seed.  
  2. Set a strong passphrase for encryption (optional but recommended).  
  3. Sync with remote servers and start sending or receiving DigiByte.

- **Command Line Usage**:  
  DigiElectrum also supports a command-line version. Simply run:
  .. code-block:: bash

     digielectrum -v

  Use the ``--help`` option to see available parameters and subcommands.

- **Backup and Seed**:  
  Make sure to securely store your 12- or 24-word seed phrase. This is crucial for wallet recovery.

- **Fee Adjustment**:  
  In the settings, you can choose your fee rate. A higher fee results in faster confirmations during network congestion.

Recommended Setup
~~~~~~~~~~~~~~~~

- **Virtual Environment**:  
  Creating a dedicated virtual environment in Python 2.7 ensures dependency conflicts are minimized:
  .. code-block:: bash

     virtualenv -p /usr/bin/python2.7 digielectrum-env
     source digielectrum-env/bin/activate

     # Then run the installation commands within this environment
     pip install ecdsa slowaes ltc-scrypt pyasn1 pyasn1-modules
     ...

- **Hardware Wallets**:  
  DigiElectrum can be configured to work with certain hardware wallets for increased security. Consult official documentation or check for additional plugins/modules if needed.

.. _Creating Official Packages:

3. HOW OFFICIAL PACKAGES ARE CREATED
------------------------------------

For maintainers or contributors looking to package DigiElectrum for distribution, the following commands outline the process:

.. code-block:: bash

   python mki18n.py
   pyrcc4 icons.qrc -o gui/qt/icons_rc.py
   python setup.py sdist --format=zip,gztar

   # On Mac OS X:
   # Port-based installs
   sudo python setup-release.py py2app

   # Brew installs
   ARCHFLAGS="-arch i386 -arch x86_64" sudo python setup-release.py py2app --includes sip

   sudo hdiutil create -fs HFS+ -volname "DigiElectrum" -srcfolder dist/DigiElectrum.app dist/digielectrum-VERSION-macosx.dmg

4. TROUBLESHOOTING & FAQ
------------------------

Below are some common questions and issues users might encounter:

**Q: DigiElectrum won't start on Python 3.x.**  
A: DigiElectrum is designed for Python 2.7. Please install Python 2.7 and ensure it is set as the default environment.

**Q: I'm getting a 'Permission Denied' error when installing.**  
A: Try running the command with ``sudo``, or use a virtual environment with ``--user`` to avoid permission issues.

**Q: Why can't I see my funds immediately after receiving them?**  
A: DigiElectrum needs to synchronize with remote servers. Wait for the wallet to finish syncing and confirm at least one block after receiving a transaction.

**Q: How do I recover my wallet if I lose my device?**  
A: Use the seed phrase you created during wallet setup. It’s critical to keep this seed phrase secure and offline.  

.. _Issues: https://github.com/josansorex/Electrum-DGB/issues

Additional Resources
--------------------

For more detailed information on DigiByte, visit the official DigiByte community channels and documentation. Stay updated with new releases on the `GitHub release page`_.

.. _GitHub release page: https://github.com/josansorex/Electrum-DGB/releases

Contributing
------------

We appreciate all contributions from the community. Whether it’s code submissions, bug reports, or feature requests, your help is invaluable. Please follow the guidelines below when contributing:

- Fork the repository and create a new branch for your changes.
- Test your code thoroughly before submitting a Pull Request.
- Provide a clear description of the issue or feature in the Pull Request comments.

Acknowledgments
---------------

Thanks to the original Electrum author, **Thomas Voegtlin**, and the **DigiByte Team** for their dedication and support in developing open-source cryptocurrency solutions. Your efforts continue to empower users worldwide.

License
-------

DigiElectrum is released under the `GNU GPL v3`_ license. For details, see the `License file`_.

.. _GNU GPL v3: https://www.gnu.org/licenses/gpl-3.0.html
.. _License file: https://github.com/josansorex/Electrum-DGB/blob/main/LICENSE
