#!/bin/bash
# Calls the script on the cluster, which loads the moduels and creates the pvserver

ssh schurk1@juwelsvis03.fz-juelich.de "~/Public/startParaViewServer.sh" &

sleep 3

ssh -N -L 12347:localhost:12347 schurk1@juwelsvis03.fz-juelich.de &

paraview
