#!/usr/bin/env ruby

#91 19

n=93
m=17

k=1

$generation_cache={1=>1,2=>1}


def dead(n,k,m)

	# Number born in month n+1-m
	if n<=m
		return 0
	end
	if n==(m+1)
		return 1
	end
	return fib(n-m-1,k,m)*k
end

def fib(n,k,m)
	if $generation_cache[n]!=nil
		return $generation_cache[n]
	end

	if n==1 || n==2
		return 1
	end

	v=fib(n-2,k,m)*k+fib(n-1,k,m)-dead(n,k,m)
	$generation_cache[n]=v
	return v

end

puts fib(n,k,m)