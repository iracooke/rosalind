#!/usr/bin/env ruby

require 'set'
s="TAAAGATGGTCTCTTTTAAAGATAATTATAAAGATAAGCCTAAAGATCGCGTAAAGATGATAAAGATATGGTAAAGATTTAAAGATTAATATGGTGAATAAAGATTTAATTGGTAAAGATGTAAAGATGTCTAAAGATCTTAAAGATGTAAAGATATATTAAAGATTAAAGATTGTTAAAGATGACATAAAGATTAAAGATAGTAAAGATCTATAAAGATGTGGATAAAGATCTAAAGATGTAAAGATCGATCAGCTAAAGATTGTAAAGATATAAAGATACGTAAAGATTAAAGATAGTGTAAAGATATTAAAGATTAAAGATTAAAGATCCATAAAGATTTGGGGCACGTACCCAAGCGTAAAGATTTCTAAAGATTTAAAGATTACGTCGATAAAGATTAAAGATCAGCGCACTAAAGATAGAGTAAAGATTAAAGATTATAAAGATTAAAGATGTAAAGATCACTGTAAAGATGTAAAGATTTATAAAGATTTTAAAGATAATAAAGATTAATAAAGATAAGTAAAGATTAAAGATTAAAGATATAAAGATTAAAGATGATAAAGATTCTCATAAAGATTAAAGATTCCTAAAGATTATTGCGTAAAGATTTAAAGATGGGTACATAAAGATGCCTTGAGTAAAGATTAAAGATTAAAGATGTAAAGATTAAAGATTAAAGATCTAAAGATTTAAAGATTAAAGATATAAAGATGTAAAGATTGTACTAAAGATTTAAAGATATTGCCCACTAAAGATGACCTAAAGATCTAAAGATCTGCTAAAGATGCGTAAAGATATAAAGATTAAAGATAGCCTTAAAGATGTAAAGATATATAAAGATACGTAAAGATCAGTTTTGATAAAGAT"

t="TAAAGATTA"

positions=Set.new

s.length.times do |i| 
	ind = s.index(t,i).to_i
	positions.add(s.index(t,i).to_i+1) 	if ind>=i
end

output=""

positions.each { |e| output << "#{e.to_s} " }

puts output