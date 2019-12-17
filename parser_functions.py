def parse_cigar(cigar):
	l = 0
	for c in cigar:
		if c in '0123456789':
			l = 10*l + int(c)
		else:
			yield (l, c)
			l = 0

def cigar2len(cigar, ops='HSM=XI'):
	return sum(l for l, o in parse_cigar(cigar) if o in ops)

import gzip
def read_fasta(path, attributes=None):
	with gzip.open(path, 'rt') if path.endswith('.gz') else open(path, 'r') as fasta:
		name = None
		for line in fasta:
			if line.startswith('>'):
				if name is not None:
					yield name, ''.join(seqs)
				name = line[1:].rstrip()
				seqs = []
			else:
				seqs.append(line.rstrip())
	yield name, seq

