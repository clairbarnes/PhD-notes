#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()

ensembles = ["ecmf", "kwbc", "egrr", "babj", "cwao", "sbsj"]
for ens in ensembles:
	for y in range(2007,2017):
		server.retrieve({
			"class"		: "ti",
			"dataset"	: "tigge",
			"date"		: "{0}-12-01/to/{0}-12-31".format(y),
			"expver"	: "prod",
			"grid"		: "1/1",
			"area"		: "60/-6/50/2",
			"levtype"	: "sfc",
			"origin"	: "{0}".format(ens),
			"number"	: "all",
			"param"		: "167",
			"step"		: "0/24/48/72/96/120/144/168/192/216/240/264/288/312/336/360",
			"time"		: "00:00:00",
			"type"		: "pf",
			"target"	: "../{0}/{0}-temp-pf-{1}-12.grib".format(ens,y),
		})
