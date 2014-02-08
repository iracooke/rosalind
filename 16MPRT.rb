#!/usr/bin/env ruby
require 'bio'
require 'rest-client'


def scan_str(str, pattern)
  res = []
  (0..str.length).each do |i|
    res << i+1 if str[i..-1] =~ /^#{pattern}/
  end
  res
end


File.foreach("inputs/16MPRT.txt") do |line| 
	line.chomp!

	entry_as_string=RestClient.get "http://uniprot.org/uniprot/#{line}.fasta"
	entry=Bio::FastaFormat.new(entry_as_string)

	matches=scan_str(entry.seq,/N[^P][ST][^P]/)

	if matches.length>0
		puts line
		puts matches.join(" ")
	end

end


# s=">sp|P07204|TRBM_HUMAN Thrombomodulin OS=Homo sapiens GN=THBD PE=1 SV=2
# MLGVLVLGALALAGLGFPAPAEPQPGGSQCVEHDCFALYPGPATFLNASQICDGLRGHLM
# TVRSSVAADVISLLLNGDGGVGRRRLWIGLQLPPGCGDPKRLGPLRGFQWVTGDNNTSYS
# RWARLDLNGAPLCGPLCVAVSAAEATVPSEPIWEEQQCEVKADGFLCEFHFPATCRPLAV
# EPGAAAAAVSITYGTPFAARGADFQALPVGSSAAVAPLGLQLMCTAPPGAVQGHWAREAP
# GAWDCSVENGGCEHACNAIPGAPRCQCPAGAALQADGRSCTASATQSCNDLCEHFCVPNP
# DQPGSYSCMCETGYRLAADQHRCEDVDDCILEPSPCPQRCVNTQGGFECHCYPNYDLVDG
# ECVEPVDPCFRANCEYQCQPLNQTSYLCVCAEGFAPIPHEPHRCQMFCNQTACPADCDPN
# TQASCECPEGYILDDGFICTDIDECENGGFCSGVCHNLPGTFECICGPDSALARHIGTDC
# DSGKVDGGDSGSGEPPPSPTPGSTLTPPAVGLVHSGLLIGISIASLCLVVALLALLCHLR
# KKQGAARAKMEYKCAAPSKEVVLQHVRTERTPQRL"

# entry=Bio::FastaFormat.new(s)

# entry.seq.to_s.scan(/N[^P][ST][^P]/) { |m| puts "#{m} #{($~.offset(0)[0]+1)}" }