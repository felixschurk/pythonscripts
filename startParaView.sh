#!/bin/bash

ssh schurk1@juwelsvis03.fz-juelich.de "~/Public/startParaviewServer.sh" &

sleep 5

# CONNECT_ID=$(ssh juwelsvis03.fz-juelich.de "cat ~/Public/.paraviewConnectID.txt")

ssh -N -L 12347:localhost:12347 schurk1@juwelsvis03.fz-juelich.de &

paraview # --connect-id=$CONNECT_ID
