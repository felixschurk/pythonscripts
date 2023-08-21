#!/bin/bash

ssh -L 12345:login18-2.hpc.itc.rwth-aachen.de:12345 id12345@login18-2.hpc.itc.rwth-aachen.de ".local/tools/startParaviewServer.sh" &

sleep 3

scp cluster:~/Public/.paraviewConnectID.txt ~/Documents/.paraviewConnectID.txt

CONNECT_ID=$( cat ~/Documents/.paraviewConnectID.txt)

echo $CONNECT_ID

/Applications/ParaView.app/Contents/MacOS/paraview --connect-id=$CONNECT_ID
