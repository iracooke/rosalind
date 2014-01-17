#!/usr/bin/env ruby

k=28
m=17
n=22

#28 17 22

$n_pop=k+m+n

$type_pops={'k'=>28,'m'=>17,'n'=>22}

#Possible pairings with probability of offspring having dominant phenotype

kk=1
km=1
kn=1
mm=0.75
mn=0.5
nn=0

def pair_selection_prob(type1,type2)
	p1=$type_pops[type1]/$n_pop.to_f

	if type1==type2
		p2=($type_pops[type2]-1)/($n_pop-1).to_f		
	else		
		p2=$type_pops[type2]/($n_pop-1).to_f
	end
	p1*p2
end

def pair_dominant_prob(type1,type2)
	if type1=='k' || type2=='k'
		return 1
	end

	if ( type1=='m' ) && (type2 == 'm')
		return 0.75
	end

	if type1=='m' || type2=='m'
		return 0.5
	end

	return 0
		
end

pp=0
['k','m','n'].each { |t1| 
	['k','m','n'].each { |t2| 
		pp+=pair_selection_prob(t1,t2)*pair_dominant_prob(t1,t2)
	}
 }

puts pp