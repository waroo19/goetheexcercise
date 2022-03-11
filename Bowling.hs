
-- Thi Tuong Vy Vu



--Aufgabe 1

import Data.List

data Frame = Strike | Roll Int Int | Bonus Int
type Game = [ Frame ]

-- Frame= Strike ?
isStrike :: Frame -> Bool
isStrike (Roll x y) 
    | x == 10     = True
    | otherwise  = False
isStrike Strike  = True
isStrike (Bonus x)  = False
-- Frame= Spare ?
isSpare :: Frame -> Bool
isSpare (Roll x y)
    | and [(x<10),(x+y==10)] == True = True
    | otherwise                   = False 
isSpare Strike = False
isSpare (Bonus x) = False
-- Game valid?
isValid :: Game -> Bool
isValid game 
    | length game >= 10  = True
    | otherwise          = False
-- Wert ?
wert :: Frame -> Int
wert  (Roll x y) = x+y
wert   Strike    = 10
wert  (Bonus x)  = x 
 
--Bonus für Spare
bospare :: Frame -> Int
bospare (Roll x y) = x
bospare  (Bonus x) = x
bospare Strike     = 10

checkspare game =   elemIndices True (map (\x -> isSpare x ) game)
punktspare game =  [bospare( game!!(x+1))| x <- (checkspare game) ]
 
--Bonus für Strike
bostrike :: Frame -> Int
bostrike (Roll x y)= x+y
bostrike  (Bonus x)= x
bostrike  Strike = 10
 
checkstrike game = elemIndices True (map (\x -> isStrike x ) game)
punktstrike game = [if bostrike( game!!(x+1))/= bospare( game!!(x+1)) then bostrike( game!!(x+1))
                      else bostrike( game!!(x+1)) + bostrike( game!!(x+2))| x <- (checkstrike game) ]




--Frame= Bonus ?
isBonus :: Frame -> Bool
isBonus (Roll x y) = False
isBonus  Strike     = False  
isBonus (Bonus x ) = True

nobo game =  (map (\x -> isBonus x ) game)
nobo1 game = [ wert(game!!x)| x <- (elemIndices False (nobo game)) ]

--Finalscore
score game = (foldr(\x acc -> acc + x) 0 (nobo1 game)) 
               + (foldr(\x acc -> acc + x) 0 (punktspare game))
               + (foldr(\x acc -> acc + x) 0 (punktstrike game))
  
-- [ Roll 9 1 , Roll 8 2 , Strike , Roll 9 1 , Roll 8 0 ,Roll 8 2 , Roll 9 0 , Strike , Strike , Strike ,Bonus 9 , Bonus 1 ]