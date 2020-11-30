""" Simple way to output errors to a file. """
import os

from datetime import datetime

import config

output_file = "{}/{}".format(config.output_path, config.output_finm)
if not os.path.exists(config.output_path):
  os.makedirs(config.output_path)

msg_fmt  = "{}  --  {}"
date_fmt = "%Y/%m/%d %H:%M:%S"

def append(msg):
  """ Append a string to the output file. """
  out_msg = msg_fmt.format(datetime.now().strftime(date_fmt), msg)
  with open(output_file, "a+") as outfile:
    outfile.write(out_msg)
