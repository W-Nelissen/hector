# hector
Codebase voor het seminarie "Programmeren in Python" van de zesdejaars van het Sint-Pieterscollege in Jette 
Project: schaakbot.

## Progress:
* 12 Maart: Tekenen van chessboard+pieces
* 12 Maart: Basisklassen voor klok (chess_clock.py)
* 12 Maart: Basismechanisme voor moves (chess_board.py)
* 14 Maart: Implementatie van classes voor sound en video (handle_sound.py; handle_video.py)
* 15 Maart: Implementatie van move + slaan, pion kan 2 vakjes bij start
* 16 Maart: Pion move + slaan. (nog niet en passant)
* 17 Maart: Na move switchen we van speler. (enkel speler aan zet kan stukken verzetten)
* 20 Maart: Bijhouden en tonen van historiek van zetten
* 20 Maart: Kleurenschema verbeterd
* 20 Maart: Optie om steeds wit onderaan te hebben of steeds te flippen bij zet
* 22 Maart: Check of je schaak staat en onmogelijk om jezelf schaak te zetten
## TODO: (in willekeurige volgorde)
* Alle mogelijke moves implementeren (rokade, pion aan eind)(lastmoved,lastmove bijhouden)
* Slaan voor Pionnen (en passant)
* Detectie stalemate
* Rokade: Toren mee verzetten
* Console implementeren (messages en later commands)
* klok laten switchen bij zet
* Eigen file formaat (als tussenstap)
* History area: bord terugzetten naar vorige toestand (multiple undo)
* Uittesten background routines
* Uittesten dialog boxes
* Evaluatie: class voor stukken + class voor positie (modifier)
* Alpha-Beta pruning routine
* PC laten spelen tegen speler
