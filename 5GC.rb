#!/usr/bin/env ruby

require 'bio'

max_gc = 0

best_entry=""

Bio::FastaFormat.open("input.txt").each do |entry| 
	id=entry.definition
	sequence=entry.seq.to_s

	seq_len=sequence.length
	nc = sequence.count('C')
	ng = sequence.count('G')
	gc = (nc+ng)/seq_len.to_f
	if gc > max_gc
		best_entry=id
		max_gc=gc
	end

end

puts "#{best_entry}\n#{max_gc*100}"