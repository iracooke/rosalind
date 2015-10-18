#!/usr/bin/env ruby

require_relative 'monoisotopic_mass_table.rb'

peptide = ARGV[0].chomp

protm = 0
amino_acids = peptide.split("").each { |aa| protm += $monoisotopic_mass_table[aa] }

p protm.round(3)