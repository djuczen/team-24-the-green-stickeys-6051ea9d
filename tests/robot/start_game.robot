*** Settings ***
Documentation     Test start of game. Let's play \n\n https://raw.githubusercontent.com/level-up-program/python-robot-reference/main/tests/robot/images/gamerErin.png
Test Template     Start new game
Library           StartGameLibrary.py

*** Test Cases ***      numPositions     startingPositionX    startingPositionY  startingMoveCount
Blank character name    100              0                    0                  0
CowboyHank              100              0                    0                  20
CowboyHanks             100              0                    0                  50
CowboyHanky             100              0                    0                  1
DonkeyFace              100              0                    0                  10
Jasonheadf              100              5                    5                  15
Carplond                100              9                    9                  1
Mondors                 100              9                    9                  10
Stinkface               100              2                    2                  100
Character               100              5                    0                  300

*** Keywords ***
Start new game
    [Arguments]    ${numPositions}  ${startingPositionX}  ${startingPositionY}  ${startingMoveCount}
    Initialize controller
    Number of map positions should be  ${numPositions}
    Starting X coordinate should be    ${startingPositionX}
    Starting Y coordinate should be    ${startingPositionY}
    Starting move count should be      ${startingMoveCount}
