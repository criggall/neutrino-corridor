Here is what I did to convert our B-MAD files into MAD-X and eventually txt format!

First, I followed these instructions to install Tao via Conda: https://wiki.classe.cornell.edu/ACC/ACL/OffsiteDoc.

I also found a helpful tutorial on Tao and B-MAD here: https://www.classe.cornell.edu/bmad/tutorial\_bmad\_tao.pdf.

With Tao installed, I ran "bmad\_to\_mad\_sad\_elegant -madx ../projects/neutrino-corridor/RCS1\_lattice\_files/ref.bmad" in my terminal to first convert the reference file, and then the others.

I then had to install MAD-X via https://madx.web.cern.ch/.

Following the example in this document https://uspas.fnal.gov/materials/18ODU/Fund/using-mad-x.html, I modified our newly-converted MAD-X files to specify "Particle = posmuon" at the top of the file, and included the following lines at the bottom.
"lat: line = (line\_1, line\_2);
use, period = lat;
MATCH, SEQUENCE=lat;
TWISS, SAVE;
WRITE,TABLE=TWISS,FILE=ref.txt;"

With this, I was finally able to run "./madx ref.madx" to generate a .txt file that is able to be read by MINT. I imagine there was most certainly somewhere I could have short-cutted this whole procedure... but c'est la vie, now we have txt files! 