#!/usr/bin/env ruby

n=30
k=5

def fib(n,k)
	if n==1 || n==2
		return(1)
	end
	(fib(n-2,k)*k)+fib(n-1,k)
end

puts fib(n,k)