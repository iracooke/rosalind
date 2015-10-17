#!/usr/bin/env ruby

def factorial(n)
	return 1 if n==1
	return n*factorial(n-1)
end

n=ARGV[0].to_i

puts factorial(n)

def permute(items)
  if items.count == 2
    return [items,items.reverse]
  end


  perms = []
  for item in items
    remaining = items.dup
    remaining.delete(item)
    perms << permute(remaining).collect {|p_remain| [item,p_remain].flatten }
  end
  return perms.flatten(1)
end

numarr = (1..n).collect { |e| e}

permute(numarr).each { |e| puts e.join(" ") }