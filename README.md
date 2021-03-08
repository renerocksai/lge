# lge - Lua Game Exercises

# 1. First Challenges 

## 1.1 Lua Windows hello world

- Lua for Windows runterladen und installieren
- das Script soll einfach nur "hello world" auf die Console schreiben und fertig.
- Du wirst einen Editor brauchen (z.B. Notepad++ oder **Visual Studio Code**).
- Du wirst auf der Console (Windows Terminal oder was auch immer) arbeiten muessen, um Lua aufzurufen und Dein Script auszufuehren.
- Du kannst schauen, wie Du Visual Studio Code so einrichtest, dass Du Dein Script im eingebauten Terminal ausfuehren kannst.


## 1.2 Lua Game hello world

- irgendwas im Game durch ein einfaches Lua-Script anzeigen
- z.B. "hello, world"

Da ich (noch) keine Ahnung von dem Game und der Lua-Schnittstelle hab, kann ich hier keine Tipps geben.


# 2. Challenge #2 : Match-Making Basics 1
Lade dieses GitHub-Repository runter. Im Verzeichnis `data/` befindet sich `server1.csv`. Wir tun mal so, als waeren diese Daten vom Server gekommen.

Schau Dir das File an in Deinem Editor. Es beinhaltet einfache Fake-Daten von 20 fiktiven Usern und deren fiktive Punktezahlen.

Schreibe ein Lua-Script, das das File einliest und die beiden Spalten in umgekehrter Reihenfolge ausgibt. Also statt User, Punkte die Reihenfolge Punkte, User.

Bsp:

```
10000 : user234
234 : user4390
...
```

**Bonus-Punkte**, wenn es schoen formatiert ist, z.B.:

```
Points    | User
----------+------------
  759     | user234
 1000     | user4390
  312     | jhkgb890
78900     | jhfthsg5465
...

```


# 3. Challenge #3 : Match-Making Basics 2

# 3.1 Top-3
Die neue Aufgabe lautet nun: Schreibe ein Lua-Script, das:

- `data/server1.csv` einliest
- die 3 User mit den hoechsten Punktzahlen findet
- und diese aehnlich wie in #2 ausgibt, nur : 
  - **sortiert** nach absteigender Punktezahl
  - Spaltenreihenfolge User, Points

Bsp:

```
--------------------
Top-3:
--------------------
jhfthsg5465 : 78900
   user4390 :  1000
    user234 :   312
```


# 3.2 Top-n
Wie 3.1 - nur diesmal soll ueber einen Parameter steuerbar sein, wieviele Top-User man sehen moechte (also 3 fuer die Top-3 oder 5 fuer die Top-5, etc.).
