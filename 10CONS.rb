#!/usr/bin/env ruby

require 'bio'
require 'matrix'

def zero_consensus_matrix(length)
	consensus_matrix={}
	["A","C","G","T"].each { |base| consensus_matrix[base]= Array.new(length,0)}
	consensus_matrix
end

def consensus_sequence(consensus_matrix)
	seqlen=consensus_matrix["A"].length
	seq=""
	seqlen.times do |i| 
		bestkey="A"
		bestscore=consensus_matrix["A"][i]
		consensus_matrix.each_key do |key| 
			score=consensus_matrix[key][i]
			if score>bestscore
				bestkey=key
				bestscore=score
			end
		end
		seq<<bestkey
	end
	seq
end

consensus_matrix=nil

Bio::FastaFormat.open("input.txt").each do |entry| 
	sequence=entry.seq.to_s

	consensus_matrix=zero_consensus_matrix(sequence.length) if consensus_matrix==nil

	sequence.upcase.chars.each_with_index do |c, i|  

		consensus_matrix[c][i]+=1
	end

end

puts consensus_sequence(consensus_matrix)
consensus_matrix.each_key { |key| puts "#{key}: #{consensus_matrix[key].join(" ")}" }