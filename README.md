A welcome screen for Ubuntu MATE that provides links to helpful resources, utilities and a selection of software packages.

Development
===========

Clone this repository, then initialize the sub module :
```bash
git clone https://github.com/ubuntu-mate/boutique-2.0
cd boutique-2.0
git submodule init
git submodule update
```

Build the software index and copy it to the source tree :
```bash
cd software-boutique-curated-apps
./script/build.sh
cp -a dist ../src/apps
cd ..
```
