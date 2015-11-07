#!/usr/bin/env ruby
require 'set'

alphabet=ARGV[0]

n = ARGV[1].to_i

letters = alphabet.split(" ")

ln = letters.length

# This is for position -1
s=""
n.times {|k| s << letters[0]}

puts s

# For each reverse position in the string we enumerate
# all possibilities to be gained by cycling our alphabet at that position
#
(0...n).each do |i|

  # Number of new strings at this position
  #
  nreps = (ln-1)*ln**i

 # p nreps

  # For each new string. 
  # Construct the string itself
  #
  (0...nreps).each do |j|  
    s = ""

    # Prefix will repeat first letter in the alphabet
    # up to the current position
    #
    prefix_n = n-i-1
    prefix_n.times { |k| s << letters[0] }

    remainder = n-prefix_n

    # This allows us to convert from j and k into our current letter
    # 
    k_periods = (1..remainder).collect { |k| ln**(remainder-k) }

    # p k_periods

    offset = 0
    (0...remainder).each do |k|
      # require 'byebug';byebug
      lp = ((j-offset)/k_periods[k]).floor
      offset += k_periods[k]*lp
      if k==0
        lp=lp+1
      end

      # puts "#{lp}: #{j} , #{k_periods[k]}, #{k}"
      s << letters[lp]
    end
    puts s
  end

end