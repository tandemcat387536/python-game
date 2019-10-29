# Python Game

Simple game based on something like _ticktacktoe_

Game starts after calling function **play** with **two** arguments -> _MODE_, _ROWS_.
**ROWS** -> Generates plan _ROW x ROW_

**MODES**.
* **1** : Two-player game
* **2** : One-player game against AI

**Simple rules** :
* If player is on move, he picks some position in plan (left up corner is _"1 1"_)
* All eight blocks around player's pick are *destroyed*
* Wins player, who picks last *free blocks*