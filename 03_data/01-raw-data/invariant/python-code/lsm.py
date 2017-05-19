#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()

server.retrieve({
    "class"	: "ei",
    "dataset"	: "interim",
    "date"	: "1989-01-01",
    "expver"	: "1",
    "grid"	: "1/1",
    "levtype"	: "sfc",
    "param"	: "172.128",
    "step"	: "0",
    "stream"	: "oper",
    "time"	: "12:00:00",
    "type"	: "an",
    "format"	: "netcdf",
    "target"	: "../lsm.nc",
})
