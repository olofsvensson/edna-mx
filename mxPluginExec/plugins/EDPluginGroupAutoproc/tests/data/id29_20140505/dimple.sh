#!/bin/sh

if [ $# -eq 1 ]; then
        ssh mxnice /scisoft/bin/cctbx_python_debian6.sh /scisoft/bin/run-dimple-autoproc.py /mntdirect/_scisoft/users/svensson/git/edna-mx/mxPluginExec/plugins/EDPluginGroupAutoproc/tests/data/id29_20140505 `readlink -f "$1"`;
else
        ssh mxnice /scisoft/bin/cctbx_python_debian6.sh /scisoft/bin/run-dimple-autoproc.py /mntdirect/_scisoft/users/svensson/git/edna-mx/mxPluginExec/plugins/EDPluginGroupAutoproc/tests/data/id29_20140505 1238863
fi
