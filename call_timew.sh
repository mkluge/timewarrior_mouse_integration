#!/bin/bash

unset LANG

HOMEPATH='\Users\mkluge'
INFOPATH=/usr/local/info:/usr/share/info:/usr/info
PATH='/home/mkluge/bin:/usr/local/bin:/usr/bin:/cygdrive/c/Python27:/cygdrive/c/Python27/Scripts:/cygdrive/c/ProgramData/Oracle/Java/javapath:/cygdrive/c/Program Files/Haskell/bin:/cygdrive/c/Program Files/Haskell Platform/7.10.3/lib/extralibs/bin:/cygdrive/c/Program Files/Haskell Platform/7.10.3/bin:/cygdrive/c/Windows/system32:/cygdrive/c/Windows:/cygdrive/c/Windows/System32/Wbem:/cygdrive/c/Windows/System32/WindowsPowerShell/v1.0:/cygdrive/c/Program Files (x86)/GTK2-Runtime/bin:/cygdrive/c/Program Files/Haskell Platform/7.10.3/mingw/bin:/cygdrive/c/Program Files/TortoiseGit/bin:/cygdrive/c/Program Files (x86)/Skype/Phone:/cygdrive/c/Leksah/bin:/cygdrive/c/Program Files (x86)/Brackets/command:/cygdrive/c/Program Files/Intel/WiFi/bin:/cygdrive/c/Program Files/Common Files/Intel/WirelessCommon:/cygdrive/c/Program Files/LLVM/bin:/cygdrive/c/HashiCorp/Vagrant/bin:/cygdrive/c/Program Files/Git/cmd:/cygdrive/c/Users/mkluge/AppData/Roaming/cabal/bin:/cygdrive/c/Program Files/Intel/WiFi/bin:/cygdrive/c/Program Files/Common Files/Intel/WirelessCommon:/cygdrive/c/Users/mkluge/AppData/Local/atom/bin:/usr/lib/lapack'

cd /home/mkluge
bash -l -c "/usr/local/bin/timew $*" 1>>call_timew.sh.out 2>&1

