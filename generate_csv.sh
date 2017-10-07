#!/usr/bin/env bash

rm uuids.csv
ls uuids | cut -d '.' -f 1 > uuids.csv
