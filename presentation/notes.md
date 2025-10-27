# Präsentation 

## Motivation
Ziel: 
- Mit dieser Arbeit werde ich versuchen herauszufinden, wie didaktische Simulatoren in der Lehre, insbesondere in der Hochschullehre des Gebietes Rechnerarchitektur als Teilgebiet der Informatik, eingesetzt werden
- Anhand vieler Beispiele werde ich Trends in der Entwicklung und im Einsatz von Simulatoren aufzeigen und Best Practices ableiten

## Methodik
- Datenbanken
    - IEEE (Institute of Electrical and Electronics Engineers)
    - ACM (Association for Computing Machinery)

## Theoretische Grundlagen
- Simulator:
    1) Ausgangspunkt ist die Realität
    2) Wird die Realität vereinfacht, spricht man von einem Modell
    3) Führt man nun mit diesem Modell Experimente durch, so spricht man von einer Simulation
    4) Ein Simulator ist schließlich ein Werkzeug, das die Durchführung von Simulationen ermöglicht meist in Form einer Software

- Digitales Lernen:
    - Organisationsformen:
        - E-Learning: Als Oberbegriff für alle Formen des Lernens, die digitale Medien sowie Informations- und Kommunikationstechnologien zur Unter stützung oder Durchführung von Lehr- und Lernprozessen einsetzen 
        - M-Learning: Lernen mit mobilen Endgeräten wie Smartphones oder Tablets
        - Blended Learning: Kombination von Präsenzveranstaltungen und E-Learning
        - MOOCs: Massive Open Online Courses, die online angeboten werden und für eine große Anzahl von Teilnehmern zugänglich sind

    - Technologien:
        - Immersive Technologien: Virtuelle Realität (VR), Erweiterte Realität (AR) und Mixed Reality (MR)
        - Learning Analytics: Sammlung und Analyse von Daten über Lernende und deren Interaktionen mit digitalen Lernumgebungen zur Verbesserung des Lernprozesses
        - Virtual Labs: Virtuelle Labs sind computerbasierte, interaktive Umgebungen, die es ermöglichen, Aufgaben auszuführen, die normalerweise in einem physischen Labor stattfinden würden. Über entsprechende Benutzeroberflächen können Simulationen, Animationen und teilweise sogar die Fernsteuerung realer Laborhardware erfolgen

    - Gamification: Einsatz von spielerischen Elementen und Mechaniken in einem nicht-spielerischen Kontext, um die Motivation und das Engagement der Lernenden zu erhöhen
        - weitere Unterteilungen sind hier möglich

- Cognitive Theory of Multimedia Learning (CTML)
    - Lernpsychologische Theorien: Behaviorismus, Kognitivismus, Konstruktivismus
    - Annahmen der CTML:
        - Duale Kanäle: Menschen verfügen über zwei separate Kanäle zur Verarbeitung von Informationen – einen für visuelle/piktoriale Informationen und einen für auditive/verbale Informationen
        - Begrenzte Kapazität: Jeder Kanal hat eine begrenzte Kapazität
        - Aktive Verarbeitung: Lernen erfordert eine aktive Verarbeitung der Informationen durch den Lernenden, einschließlich der Auswahl, Organisation und Integration von Informationen

    - Einordnung:
        - Kognitivismus, da Prozess der aktiven Informationsaufnahme, -verarbeitung und -speicherung
        - Konstruktivismus, da Lernende aktiv Wissen konstruieren durch Integration neuer Informationen in bestehende Wissensstrukturen

## Chronologische Entwicklung didaktischer Simulatoren
- mechanische Lernmaschinen 
    - Agostino Remellis Leserad, das die parallele Nutzung mehrerer Bücher er-
möglichen sollte
    - Sidney Pressey im Jahr 1928 mit seiner „Maschine für Intelligenztests“. Sie arbeitete mit Multiple-Choice-Aufgaben, registrierte richtige Antworten und integrierte bereits Verstärkungsmechanismen
- Computerbasierte Instruktionen
    - PLATO (Programmed Logic for Automatic Teaching Operations) in den 1960er Jahren an der University of Illinois entwickelt
- Web 2.0
    - Moodle 
    - Wikipedia
    - neue Formen des informellen, selbstregulierten Lernens und erweiterten auch die Einsatzmöglichkeiten von Simulatoren in kollaborativen Kontexten
- MOOC & M-Learning
    - Online Kurse we von edX, Coursera, Udacity
    - Mobile Apps wie Duolingo
- Microlearning & Gamification
    - Plattformen Anki 
    - Lerninhalte in kleine, leicht verdauliche Einheiten aufgeteilt
- Immersive Technologien & Virtual Labs
    - Virtuelle Realität (VR) und Erweiterte Realität (AR)

## Chronologische Entwicklung Rechnerarchitektur
- Mikroprozessor
    - alle zentralen Funktionseinheiten eines Computers auf einem Chip
    - es dominierten erst CISC Architekturen wie IBM System/360 Ender der 1970er Jahre
- RISC und ILP
    - RISC als Weiterentwicklung: CDC 6000
    - ILP (Instruction Level Parallelism) als Konzept zur Leistungssteigerung durch parallele Ausführung von Befehlen
- Mehrkernprozessoren
    - Integration mehrerer Prozessorkerne auf einem einzigen Chip
    - Ermöglicht parallele Verarbeitung und verbessert die Gesamtleistung
- Rechenzentren und Cloud Computing
    - Verlagerung von Rechenleistung und Speicher in entfernte Rechenzentren
    - Ermöglicht flexible Ressourcennutzung und Skalierbarkeit
- KI, RISC, GPUs
    - Spezialisierte Architekturen für KI-Anwendungen
    - Nutzung von GPUs (Graphics Processing Units) für parallele Verarbeitung und beschleunigte Berechnungen
    - ARM computerbasierte Architekturen für mobile und eingebettete Systeme wie Apple M5

## Ergebnisse
- Thema
    - Prozessoren und Architekturen (49%) --> RISC, Mikroprozessoren, etc.
    - GPU und AI Entwicklung (15%), jedoch alle Veröffentlichungen nach 2020

    - Prozessoren und Architekturen (40%) --> RISC, CISC
    - GPU (4%) aus den Jahren 2007 und 2011 --> noch nicht angekommen
- Gamification
    - obwohl relevant und Motivation steigernd
    - lediglich 4%
- Abstraktionslevel
    - Brücke zur CTML --> kleine Lerneinheiten
    - didaktisch reduzierte Simulatoren dominieren in dem Feld "Prozessoren und Architekturen"
- Zugriff
    - abhänigig vom Thema
    - diverse Zugriffsarten
    - k.A. = manchmal nicht beschrieben, wie der Zugriff erfolgt
- Preis:
    - überwiegend kostenlos
    - k.A. bei Literraturrecherche
    - Einsatz von FPGA bspw. als kostenpflichtig beschrieben 
- Dokumentation
    - Brücke zur CTML --> Eine Dokumentation unterstützt das Kernprinzip Active Processing, da Lernende neue Informationen mit vorhandenem Wissen verknüpfen und erweitern können 
- OS
    - nur Simulatoren
    - alle gängigen Betriebssysteme
    - oder unabhängig durch Webanwendungen

## Best Practices, Trends und Diskussion
- Ausweitung des Suchumfeldes: --> STEM: Science, Technology, Engineering und Mathematics
- OER: Open Educational Resources --> bezogen auf den Preis
- Rahmenbedingungen --> Anpassung von Lehrkonzepten
- Validierung durch Begleitstudien

- Reflexion:
    - Bekanntheit: Manuell bei Simulatoren (Github-Sternen, Google Suchergebnisse) 
    - Unterteilung des Aspekts "Gamification"
    
