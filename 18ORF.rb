#!/usr/bin/env ruby
require 'bio'
require 'set'
# Checking that bioruby and rosalind use the same codon table
# They do
#
#require_relative 'codontable'
#$dna_codon_table={}
#$rna_codon_table.each_pair { |name, val| $dna_codon_table[name.gsub("U","T")]=val }
#bioruby_dna_codon_table = Bio::CodonTable.copy(1)
#bioruby_dna_codon_table.table.each_pair { |name, val|  puts "Mismatch #{name} #{val}" unless $dna_codon_table[name.upcase] == val }

def scan_str(str, pattern)
  res = []
  (0..str.length).each do |i|
    res << i+1 if str[i..-1] =~ /^#{pattern}/
  end
  res
end


dna_fasta=">Rosalind_1207
GTCTGTCTATTGCCGAATAGTATTCTTGTATGTCATTGAATACCTGACGACTATAAAGAG
ATGAAAACAATCGGTTAACCCCGCGATTGACACATATGCGTGCCATTACAGAAAGCCCAG
GCAGTGACTACGCCATGCGACAAACTAGCCGTCGCTTTTTTTTACTCGCTATGAAGTGGT
TGGGGTCATGATATACGAGCTGATAGGCTGAATTATCCTGCATATGTCCAAGAGCCGAGC
ACTCGCTTCTCTTTTGTAGTTGACGGTCCGCATAGAGTCTTTACACCCTGACTGGTTATG
CGATTAGCCAGACTTATCCGTGCTAGTATGACCATGTTATTATGCCTAAACTCGGAGTTG
GAGTTTGTCATGATGTCAGCGATATCAAACGCTCAACGAGGTATCCACCGCAGATCGCGC
AGGGAGCCAACAACACTAACTTTTGGGGAATGAGTCGGGATGCGTCTTGAGGATAGCTAT
CCTCAAGACGCATCCCGACTCATCGACGATTATTTAACGAGGAGCAGACCTTGTACGACA
GTAACTTAACAAAGTCGCAGTAAGTTGCAAACGGACGACTGTGTTGCTCGGCTGTGGGGA
CCGGGTTAAGTAACCAGTGGCTAACGACTCGCTATATCAAATATTCAGTGGGTAGGCCGC
TATGATACTATTAGTTAAGAAACTCTTGCCCGGAGCGTGTCGCGCTCTTTGCATGTTCGT
GATCTCCCTGTCGCAGGAATGATTCGATGCGAGCGGACACTAGTTAGTGAATGCTATCAG
GCCGTTTTTGTCGGGGAGGTTTTGTACACTTCCTATGACAGACCGAATGTCGTAAGGAGG
ATCCGATAGAAGGTGTCATTGGTGGACAGGTACAACCCGCATGTCTGGAGACGGATGCGA
TATTTTATTAGGTAGGACTAGTAAGACCCCATACAACCTTTAACGGGGTGCA"

#dna_fasta=">Rosalind_99
#AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

dna=Bio::FastaFormat.new(dna_fasta)

distinct_prots=Set.new()
(1...7).each do |f|
	translation=dna.naseq.translate(f)

#	puts "#{translation}\n\n"

	parts = translation.split("*")
	if translation[-1]!="*"
		parts = parts[(0..-2)]
	end

#	puts parts
	parts.each do |raw_orf|  
		start_mets = scan_str(raw_orf,"M")
		#puts start_mets
		start_mets.each do |start_met|  
#			puts raw_orf.slice((start_met-1..raw_orf.length))
			distinct_prots.add raw_orf.slice((start_met-1..raw_orf.length))
		end
	end
end

distinct_prots.each { |e| puts e }