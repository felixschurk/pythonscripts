#!/bin/bash
# To connect with that server you have to use the ID on the client side as well
# by starting paraview with paraview --connect-id=$CONNECTID. This strategy
# ensures, that only your client is able to connect with the pvserver you
# have started. Without other clients are able to connect to your server by
# having full access to your data.
#
# The most comfortable way to use the script is to copy it into $HOME/bin.
# By modifying your environment path by PATH=$HOME/bin:$PATH afterwards,
# you can use pvserver as before.

ml purge
ml Stages/2023 GCC ParaStationMPI ParaView/5.11.0-EGL ParaViewPlugin-Nek5000/20230208-EGL


pvserver --sp=12347

