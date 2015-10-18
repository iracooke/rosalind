#!/usr/bin/env ruby

require 'bio'

dna_string = 'TCAATGCATGCGGGTCTATATGCAT'

dnaseq=Bio::Sequence.auto(dna_string)

seq = dnaseq.seq
rc_seq = dnaseq.reverse_complement.reverse

n = seq.length

(0..n-1).each do |start_i|
  lengths = (4..n-start_i)
  lengths.each do |j|
    s = start_i
    sseq = seq[start_i,j]
    rcseq = rc_seq[start_i,j].reverse
    if ( sseq == rcseq)
      p "#{start_i+1} #{j}"
    end
  end
end
