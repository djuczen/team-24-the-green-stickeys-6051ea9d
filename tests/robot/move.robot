*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     5             5             1                     NORTH         5           6           2
Move on the edge of the board       0             0             5                     SOUTH         0           0           6
Move north sometime                 0             0             20                    NORTH         0           1           21
Bounce off wall in bottom           0             0             50                    WEST          0           0           51
Move E on bottom corner             0             0             1                     EAST          1           0           2
Move South from the top right       9             9             15                    SOUTH         9           8           16
Bounce off wall in top right        9             9             10                    EAST          9           9           11

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}