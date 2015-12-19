#!/usr/bin/env ruby

inputs = []
open("inputs/24LGIS.txt", "r").each_line { |line| inputs << line }

n = inputs[0].to_i

seq = inputs[1].split(' ').collect { |e| e.to_i }

def longest_monotonic_subseq(seq, direction = 'increasing')

  length = []
  predecessor = []

  (0...seq.length).each do |i|  
    length[i]=0
    if direction=='increasing'
      scores = (0..i).collect { |j| (seq[j] < seq[i] ? length[j]+1 : 1 )}
    else
      scores = (0..i).collect { |j| (seq[j] > seq[i] ? length[j]+1 : 1 )}
    end

    length[i],predecessor[i] = scores.each_with_index.max
    predecessor[i] = -1 if length[i]==1


  end

  longest,last = length.each_with_index.max

  previous = predecessor[last]

  lseq=[]
  lseq << seq[last]
  while previous > -1 do
    lseq << seq[previous]
    previous = predecessor[previous]  
  end


  lseq.reverse.join(" ")
end

puts longest_monotonic_subseq(seq,'increasing')
puts longest_monotonic_subseq(seq,'decreasing')
