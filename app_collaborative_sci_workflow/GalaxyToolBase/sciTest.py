
import subprocess
pipe = subprocess.Popen(["/usr/bin/perl", "filters/CreateInterval.pl", chrom, start, end, name, strand, out_file1]).communicate()

