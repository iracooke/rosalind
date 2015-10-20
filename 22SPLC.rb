#!/usr/bin/env ruby

require 'bio'

entries=[]

Bio::FastaFormat.open("inputs/21SPLC.fasta").each do |entry|
  entries << entry
end

pre_rna = entries.shift
introns = entries

pre_rna_seq = pre_rna.seq

introns.each do |intron|
  pre_rna_seq.slice!(intron.seq)
end

puts Bio::Sequence.auto(pre_rna_seq).translate