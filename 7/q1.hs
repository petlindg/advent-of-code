import Data.Char

check :: Int -> [Int] -> Bool
check tar params = check' tar params 0
    where
        check' tar [] i     = i==tar
        check' tar (t:ts) i =
            i <= tar &&
            check' tar ts (i+t) ||
            check' tar ts (i*t)

splitOn :: Eq a => a -> [a] -> [[a]]
splitOn c ss = split' ss c []
    where
        split' [] _ sb     = [sb]
        split' (s:ss) c sb =
            if c==s
                then sb : split' ss c []
                else split' ss c (sb ++ [s])

main :: IO ()
main = do
    input <- readFile "input.txt"
    let result = sum $ map ((\z -> if check (head z) (tail z) then head z else 0) . (map (\y -> read y :: Int) . splitOn ' ' . filter (\x -> isDigit x || isSpace x))) (splitOn '\n' input)
    print result