--Relearning haskell
{-Multiline
Hello-}
--Important and amazing: :t <functName>

import Data.List
import System.IO

maxNum = maxBound :: Int

minNum = minBound :: Int

sumofnums = sum [1..500]

sqroot10 =sqrt (fromIntegral 10)

trunVal = [truncate 9.98, floor 5.50, ceiling 5.50]

listofValues = [("not True",not(True)),("and",True && False),("or", True || False),("implic", implic True False),("equiv", equiv True False)]

implic a b = if a==True then b else True
equiv a b = if a==True then b else not(b)

prodX= [[(x,y) | x <- ['A','B','C']] | y <-[1,2,3,4]]
multTab = [[x*y | x<-[1..10]] | y<-[1..10]]
combine = zipWith (^) [1,2,3,4] [2,3,4,5]

main = do
     putStrLn "What's your name"
     name <- getLine
     putStrLn ("Hello  " ++ name)

is3 n
     | n == 3 = True
     | otherwise = False
