#!/usr/bin/env ruby
require 'bio'


reference_seq=""
sequences=[]


def is_common(query_string,sequences)
	sequences.each do |seq| 
		unless seq.include? query_string
			return false  
		end
	end
	return true
end

# Read all sequences into memory and find the shortest one to use as a reference
#
min_len=10000000
Bio::FastaFormat.open("inputs/14LCSM.fasta").each do |entry| 
	sequence=entry.seq.to_s

	if sequence.length < min_len
		min_len=sequence.length
		reference_seq=sequence
	end

	sequences<<sequence
end

puts "Reference sequence has length #{min_len}"

# Starting with the entire reference sequence length check all other sequences
#
found_common=false
current_len=reference_seq.length
common_seq=""
until (found_common || current_len<=0)
	
	last_slice=reference_seq.length-current_len
	(0..last_slice).each do |start_i|
		query=reference_seq.slice(start_i,current_len)
		if is_common(query,sequences)
			common_seq=query
			found_common=true
			break;
		end
	end

	current_len-=1

end

puts common_seq