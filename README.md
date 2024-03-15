# hector
Codebase voor het seminarie "Programmeren in Python" van de zesdejaars van het Sint-Pieterscollege in Jette 
Project: schaakbot.

## Progress:
* 12 Maart: Tekenen van chessboard+pieces
* 12 Maart: Basisklassen voor klok (chess_clock.py)
* 12 Maart: Basismechanisme voor moves (chess_board.py)
* 14 Maart: Implementatie van classes voor sound en video (handle_sound.py; handle_video.py)
* 15 Maart: Implementatie van move + slaan, pion kan 2 vakjes bij start
## TODO: (in willekeurige volgorde)
* Alle mogelijke moves implementeren
* Console implementeren (messages en later commands)
* klok laten switchen bij zet (enkel speler aan zet kan stukken verzetten)
* Detectie van schaak en stalemate
* History van zetten bijhouden
* Eigen file formaat (als tussenstap)
* History area: Weergeven van historiek (chess_area_history.py)
    +bord terugzetten naar vorige toestand (multiple undo)
* Uittesten background routines
* Uittesten dialog boxes
* Evaluatie: class voor stukken + class voor positie (modifier)
* Alpha-Beta pruning routine
* PC laten spelen tegen speler
