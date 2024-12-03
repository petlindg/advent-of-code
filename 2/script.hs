import System.IO
import Data.Char

safeInc1 :: [Int] -> Bool
safeInc1 (x:[]) = True
safeInc1 (x1:(x2:xs)) = x1 < x2 && x1+3 >= x2 && safeInc1 (x2:xs)


safeDec1 :: [Int] -> Bool
safeDec1 (x:[]) = True
safeDec1 (x1:(x2:xs)) = x1 > x2 && x1 <= x2+3 && safeDec1 (x2:xs)

safeInc :: [Int] -> Bool
safeInc (x:[]) = True
safeInc (x1:(x2:xs)) = (x1 < x2 && x1+3 >= x2 && safeInc (x2:xs)) || safeInc1 (x1:xs)

safeDec :: [Int] -> Bool
safeDec (x:[]) = True
safeDec (x1:(x2:xs)) = (x1 > x2 && x1 <= x2+3 && safeDec (x2:xs)) || safeDec1 (x1:xs)

safe :: [Int] -> Bool
safe (x:xs) = safeInc (x:xs) || safeDec (x:xs) || safeInc1 xs || safeDec1 xs

trueCount :: [Bool] -> Int
trueCount []         = 0
trueCount (True:bs)  = 1 + trueCount bs
trueCount (False:bs) = trueCount bs

safeCount :: [[Int]] -> Int
safeCount xs = trueCount (map safe xs)

pow10 :: Int -> Int
pow10 0 = 1
pow10 e = 10 * pow10 (e-1)

ci :: [Char] -> Int -> Int
ci [] _     = 0
ci (c:cs) i = pow10 i * (digitToInt c) + ci cs (i+1)

test :: [[Int]]
test = [[7,6,4,2,1], [1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]

sii :: [Char] -> [Int] -> [Char] -> [[Int]]
sii []        ys cs = [(ci cs 0):ys]
sii ('\n':xs) ys cs = ((ci cs 0):ys):sii xs [] []
sii (' ':xs)  ys cs = sii xs ((ci cs 0):ys) []
sii (x:xs)    ys cs = sii xs ys (x:cs)
main :: IO ()
main = do
    input <- readFile "input.txt"
    let input' = sii input [] []
    let s = safeCount input'
    print s