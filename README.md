# Conways_Game_Of_Life

//////////     English     //////////

* Introduction
  
Development of the game "Conway's Game of Life". The game 
is a cellular automaton designed in 1970 by the British mathematician John Horton Conway. 
was designed. The project was commissioned by Dr. Alexander Stolpmann and 
is to be developed in the Python programming language.


* Functional requirements

- Storage of the game field:
  To store the necessary game values, objects are created to store the specific
  values of each cell, these objects are stored in a two-dimensional array and are
  and are accessible through a coordinate index.

- Margins and neighboring fields:
  In order to apply the game rules, it is necessary that each cell in the grid can identify its
  neighboring cells can be identified. A function is created that identifies the neighbor cells of each
  cell in the game area can identify using the two-dimensional array index.

- Realization of the rules:
  The program must operate according to the previously established rules of the game of life
  function. For this purpose, "if-statements" are used, which, together with the information from the
  neighboring cells, enable the program to know whether a cell should live or die.


* Non-functional requirements

- Game Speed:
  By changing the value of the Fps variable in the program, you can change the speed at which
  the speed at which the images are processed during game time. a value of 5 is a slow speed, 60 is a very fast speed.

- Buttons for user interaction:
  There are buttons that allow the user to start, pause or reset the game at the desired time.
  
- User-friendly interface:
  the game window has a background image, the buttons have different colors, and
  the cells have random images that give the game more visual appeal.


* Technical requirements

The following resources were used to realize the project:
- A computer with the Windows 10 operating system
- Python 3.8.3
- Visual Studio code development environment
- Python library Pygame


//////////     Deutsch     //////////

* Einleitung
  
Entwicklung des Spiels "Conways Spiel des Lebens". Das Spiel 
ist ein zellularer Automat, der 1970 vom britischen Mathematiker John Horton Conway 
entworfen wurde. Das Projekt wurde von Dr. Alexander Stolpmann in Auftrag gegeben und 
soll in der Programmiersprache Python entwickelt werden.


* Funktionale Anforderungen

- Speicherung des Spielfeldes:
  Um die notwendigen Spielwerte zu speichern, werden Objekte erstellt, die die spezifischen
  Werte jeder Zelle speichern, diese Objekte werden in einem zweidimensionalen Array
  gespeichert und sind über einen Koordinatenindex zugänglich.

- Ränder und Nachbarfelder:
  Um die Spielregeln anwenden zu können, ist es notwendig, dass jede Zelle im Raster ihre
  Nachbarzellen identifizieren kann. Es wird eine Funktion erstellt, die die Nachbarzellen jeder
  Zelle im Spielbereich mit Hilfe des zweidimensionalen Array-Index identifizieren kann.

- Realisierung der Regeln:
  Das Programm muss nach den vorher festgelegten Regeln des Spiels des Lebens
  funktionieren. Dazu werden "If-Anweisungen" verwendet, die es dem Programm zusammen
  mit den Informationen aus den Nachbarzellen ermöglichen, zu wissen, ob eine Zelle leben
  oder sterben soll.


* Nichtfunktionale Anforderungen

- Spielgeschwindigkeit:
  Durch Ändern des Wertes der Fps-Variablen im Programm können Sie die Geschwindigkeit
  ändern, mit der die Bilder während der Spielzeit verarbeitet werden. der Wert 5 ist eine
  langsame Geschwindigkeit, 60 eine sehr schnelle.

- Schaltflächen für Benutzerinteraktion:
  Es gibt Schaltflächen, die es dem Benutzer ermöglichen, das Spiel zur gewünschten Zeit zu
  starten, zu unterbrechen oder zurückzusetzen.
  
- Benutzerfreundliche Schnittstelle:
  das Spielfenster hat ein Hintergrundbild, die Schaltflächen haben verschiedene Farben, und
  die Zellen haben Zufallsbilder, die dem Spiel mehr visuellen Reiz verleihen.


* Technische Anforderungen

Die folgenden Ressourcen werden für die Realisierung des Projekts verwendet:
- Ein Computer mit dem Windows 10 Betriebssystem
- Python 3.8.3
- Visual Studio Code-Entwicklungsumgebung
- Python-Bibliothek Pygame
