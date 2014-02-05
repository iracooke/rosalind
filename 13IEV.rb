#!/usr/bin/env ruby
require 'matrix'

input="16928 19691 19265 16718 16229 16795".split(/\s+/).collect { |e| e.to_i }

n_couples=Matrix.column_vector(input)

expected_dominant_offspring=Matrix[[2,2,2,1.5,1,0]]

puts expected_dominant_offspring*n_couples
