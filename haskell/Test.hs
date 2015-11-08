--module Main where
--main = do
--  print (func 1)
--  print "shit"
--
---- the following line CAN be removed.
--func :: Integer -> Integer
--func x = x
--
--
--fib1 :: Integer -> Integer
--fib1 n
--  | n == 0  = 0
--  | n == 1  = 1
--  | n > 1   = fib (n-1) + fib (n-2)
--
import Data.List
import System.IO

fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib(n-1) + fib(n-2)
-- Int - 2^63 2^63
maxInt = maxBound :: Int
-- Integer Float Double
bigFloat = 3.999999999 + 0.000000000000005
-- Bool True False
-- Char '
-- Tuple ...
always5 :: Int -- immutable
always5 = 5

sumOfNums = sum [1..1000]

addEx = 5 + 4
subEx = 5 - 4
multEx = 5 * 4
divEx =  5 / 4

modEx = mod 5 4
modEx2 = 5 `mod` 4

negNumEx = 5 + (-4)
------
num9 = 9 :: Int
sqrtOf9 = sqrt (fromIntegral num9) -- from integer to float
-- because sqrt only takes float check :t sqrt for more info

-- Build in math functions
piVal = pi
ePow9 = exp 9
logOf9 = log 9
squared9 = 9 ** 2 -- same to python
truncateVal = truncate 9.999 -- output 9
roundVal = round 9.999 -- 10
ceilingVal = ceiling 9.999 -- 10
floorVal = floor 9.999 -- 9

trueAndFalse = True && False
trurOrFalse = True || False
notTrue = not(True)
notTrue1 = not True

---------- list ----------
primeNumbers = [3, 5, 7, 11]
morePrimes = primeNumbers ++ [13, 17, 19, 23, 29]
favNums = 2 : 7 : 21 : 66 : []
multList = [[3, 5, 7], [11, 13, 17]]
morePrimes2 = 2 : morePrimes

lenPrime = length morePrimes2
revPrime = reverse morePrimes2
isListEmpty = null morePrimes2
secondPrime = morePrimes2 !! 1
lastPrime = last morePrimes2
primeInit = init morePrimes2
fire3Primes = take 3 morePrimes
removePrimes = drop 3 morePrimes
is7InList = elem 7 morePrimes
maxPrime = maximum morePrimes
sumPrime = sum morePrimes
zeroToTen = [0..10]
eventList = [2, 4..20]
letterList = ['A','C'..'Z']

infinPow10 = [10,20..] -- lazy
many2s = take 10 (repeat 2) -- lazy
many3s = replicate 10 3
listTimes2 = [x * 2 | x <- [1..10]]
listTimes3 = [x * 3 | x <- [1..10], x * 3 <= 50]
--- this is cool: even python can not do the same here comma is a filter.
divisBy9N13 = [x | x <- [1..500], x `mod` 13 == 0 && x `mod` 9 == 0]
-- we can also do this: apply two filters:
divisBy9N13_2 = [x | x <- [1..500], x `mod` 13 == 0 , x `mod` 9 == 0]

----------
sortedList = sort [3,1,2,5,1,2,8,2]
sumOfLists = zipWith (+) [1,2,3,4,5] [6,7,8,9,10] -- zipWith is very powerful!!
-----
listBiggerThan5 = filter (>5) morePrimes
listBiggerThan5_1 = [x | x <- morePrimes, x > 5]
eventsUpTo20 = takeWhile (<=20) [2,4..]
eventsUpTo20_1 = filter (<=20) [2,4..] -- gonna hang after 20, because its lazy
-- to fold up the list together and each multi by 2 and multi them all
multOfList = foldl (*) 2 [2,3,4,5] -- foldr is from right to left (output 240)

-------------- List comprehension -------
pow3List = [3^n | n <- [1..10]]
multTable = [[x * y | y <- [1..10]] | x <- [1..10]] -- NOTE interesting
-- above in python is : [[x * y for x in xrange(1, 11)] for y in xrange (1, 11)]

randTuple = (1,"Random Tuple")
bobSmith = ("Bob Smith", 52)
bobsName = fst bobSmith
bobsAge = snd bobSmith

names = ["Bob", "Mary", "Tom"]
addresses = ["123 Main", "234 North", "567 South"]
namesNAddress = zip names addresses

------- Functions --------
-- main = do
--   putStrLn "What's your name"
--   name <- getLine -- take info from console
--   putStrLn ("Hello " ++ name)
-------
addMe :: Int -> Int -> Int
-- function name param1 param 2 = operations (return value)
addMe x y = x + y
-- sice we did not define types we can add floats or doubles etc.
sumMe x y = x + y

-- add tuples
addTuples :: (Int, Int) -> (Int, Int) -> (Int, Int)
addTuples (x, y) (x2, y2) = (x + x2, y + y2)

whatAge :: Int -> String
whatAge 16 = "you can drive"
whatAge 18 = "you can vote"
whatAge 21 = "you are an adult"
whatAge x = "nothing important"

--- recursion (IMP)
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)
-- easy way to do factorial:
prodFact n = product [1..n]

isOdd :: Int -> Bool
isOdd n
  | n `mod` 2 == 0 = False
  | otherwise = True

isOdd_1 n = not (n `mod` 2 == 0)

isEven n = n `mod` 2 == 0

whatGrade :: Int -> String
whatGrade age
  | (age >= 5) && (age <= 6) = "Kindergarten"
  | (age >= 6) && (age <= 10) = "Elementary School"
  | otherwise = "dont know"

batAvgRating :: Double -> Double -> String
batAvgRating hits atBats
  | avg <= 0.200 = "Terrible Batting Average"
  | avg <= 0.250 = "Average Player>"
  | avg <= 0.280 = "Your doing pretty good"
  | otherwise = "You are a super star!"
  where avg = hits / atBats

getListItems :: [Int] -> String
getListItems [] = "Your List is empty"
getListItems (x:[]) = "Your list starts with " ++ show x
getListItems (x:y:[]) = "Your List contains " ++ show x ++ " and " ++ show y
getListItems (x:xs) = "Your List contains " ++ show x ++ " and rest: " ++ show xs

getFirstItem :: String -> String
getFirstItem [] = "Empty String"
getFirstItem all@(x:xs) = "The first letter in " ++ all ++ " is " ++ [x]

-- NOTE: Wrote by myself
getNthItem :: String -> Int -> String
getNthItem [] n = "Empty String"
getNthItem list n
  | length list <= n = "Index out of range :)"
  | otherwise = [list !! n]

------- Higher order funcions -------
-- Python Example:
-- def twice (function):
--   return lambda x: function (function (x))
-- 
-- def f (x):
--   return x + 3
-- 
-- g = twice (f)
-- 		    
-- print g (7) # 13
-- print g (8) # 14

times4 :: Int-> Int
times4 x = x * 4

listTimes4 = map times4 [1,2,3,4,5]
multBy4 :: [Int] -> [Int]
multBy4 [] = []
multBy4 (x:xs) = times4 x : multBy4 xs
-- what's going on here ? 
-- [1,2,3,4] : x = 1 | xs = [2,3,4]
-- [2,3,4] : x = 2 | xs = [3,4]
-- ....

-- another recursion example
areStringsEq :: [Char] -> [Char] -> Bool
areStringsEq [] [] = True
areStringsEq (x:xs) (y:ys) = x == y && areStringsEq xs ys
areStringsEq _ _ = False

-- (Int -> Int) is to pass a function into a fuction
-- Hot to receive a function :
doMult :: (Int -> Int) -> Int
doMult func = func 3 -- actually times4 3
num3Times4 = doMult times4
-- reuslt : 12

-- How to return a function:
-- return a function that get a int and return a int
-- NOTE do not quite understand this
-- Explination : http://learnyouahaskell.com/higher-order-functions
getAddFunc :: Int -> (Int -> Int)
getAddFunc x y = x + y
adds3 = getAddFunc 3
fourPlus3 = adds3 4
-- use map
threePlusList = map adds3 [1,2,3,4,5]

-- regular function
compareWithHundred :: Double -> Ordering
compareWithHundred x = compare 100 x
-- higher-order function for this:
compareWithHundred_HighOrder :: Double -> Ordering
compareWithHundred_HighOrder = compare 100 -- return a function

-- 100 / 10 is (/10) 100
-- 5 - 4 is (subtract 4) 5

-- zipWith function implementation! Important!
myZipWith :: (a->b->c)->[a]->[b]->[c]
myZipWith _ [] _ = []
myZipWith _ _ [] = []
myZipWith f (x:xs) (y:ys) = f x y : myZipWith f xs ys


------------- lambdas ---------------
-- An anonymous function is a function without a name. 
-- It is a Lambda abstraction and might look like this:
-- \x -> x + 1. (That backslash is Haskell's way of expressing a 
-- λ and is supposed to look like a Lambda.)
dbl1To10 = map (\x -> x * 2) [1..10]

------ Conditionals -----------
-- < > <= >= == /= (not equal to)
doubleEvenNumber :: Int -> Int
doubleEvenNumber y = 
  if (y `mod` 2 /= 0)
	then y
  else y * 2

odd_num x = x `mod` 2 /= 0
