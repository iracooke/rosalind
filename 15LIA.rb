#!/usr/bin/env ruby
require 'rubystats'


k=5
n=7

# Each individual has this probability of being Aa Bb
#
p=0.25

# Total number of individuals in the kth gen
n_individuals=2**k

# Calculate probability of obtaining at least n individuals with AaBb genotype
#

binom=Rubystats::BinomialDistribution.new(n_individuals,p)

puts 1-binom.cdf((n-1))



