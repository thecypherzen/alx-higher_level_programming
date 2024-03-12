#!/usr/bin/env bash
# A script deletes the database hbtn_0c_0 in your MySQL server.
#+ iff it exists
#+ use of `SHOW` or `SELECT` not allowed

DROP DATABASE IF EXISTS hbtn_0c_0;
