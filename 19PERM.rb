#!/usr/bin/env ruby

def factorial(n)
	return 1 if n==1
	return n*factorial(n-1)
end

n=ARGV[0].to_i

puts factorial(n)



def print_permutations(n,position)

	prefix=(1..position-1).collect { |e| e } if position>1
	prefix=prefix.join(" ")

#	require 'debugger';debugger

	suffix=((position+1)..n).collect { |e| e } if position<n
	suffix=suffix.join(" ")

	(position..n).each do |i|  
		puts "#{prefix} #{i} #{suffix}"
	end
end

puts print_permutations(n,2)