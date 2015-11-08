import Data.List
import Data.Array
import System.IO

fib n = fib' n
	where 
	fib' 0 = 1
	fib' 1 = 0
	fib' 2 = 1
	fib' n = fibs !! (n-1) + fibs !! (n-2)
	fibs  = listArray(0, n)[fib' x | x <- 0:[0..n]]
