#!/usr/bin/env ruby

require 'bio'
require 'graphviz'

starts={}
ends={}

do_plot=true



# Create a new graph
g = GraphViz.new( :G, :type => :digraph )




Bio::FastaFormat.open("inputs/12GRPH.fasta").each do |entry| 
	id=entry.definition
	sequence=entry.seq.to_s

	if sequence.length >= 3

		g.add_nodes(id)

		start_triple=sequence[0,3]
		end_triple=sequence[sequence.length-3,3]

		starts[start_triple]=[] if starts[start_triple]==nil
		ends[end_triple]=[] if ends[end_triple]==nil

		# Define edges where our start overlaps with an end
		ends[start_triple].each { |e|  puts "#{e} #{id}"; g.add_edges(e,id) } unless ends[start_triple]==nil

		# Define edges where our end overlaps with a start
		starts[end_triple].each { |e|  puts "#{id} #{e}" ; g.add_edges(e,id) } unless starts[end_triple]==nil

		starts[start_triple]<<id
		ends[end_triple]<<id	
	end
	
end

# Generate output image
g.output( :png => "outputs/12GRPH.png" )

