## Develop 


## Develop 1:

## Analyse en Prioritering



## Deconstructie

**storyboard**

Om een duidelijker beeld te krijgen in de visie van de werking van het systeem werd een nieuwe iteratie van een storyboard gemaakt. Dit werd getekend, rekening houdend met de inzchten die verkregen werden tijdens de feedback. Na overleg van de priotirtering werd dit [storyboard](/img/afbeelding_storyboard_develop_1.JPEG) getekend.

**Productarchitectuur (I/O)**

Om vroegtijdig een beeld te krijgen van naarmate de technische ideeën mogelijk waren, werd een raspberry pi zero 2 W aangekocht samen met een draagbare projector. Toen de verbinding met behulp van code slaagde, was het duidelijk dat er op deze manier verder gebouwd kon worden. De verschillende sensoren, actuatoren en datastromen  zijn in een [productarchitecuur](/img/productarchitectuur_develop_1.png) in kaart gebracht.

**User flows & Informatiearchitectuur**

**MVP-definitie**

In deze fase werd duidelijk dat de prioriteiten voor een deel anders liggen dan voordien. De focus van dit product lag in het begin van de fases vooral op het dilemma dat hing over het installatiesysteem (ophanging of neerzetten). In deze fase lag dit eerder achterwege. Nu de projector aangekocht is, kan meer gefocust worden op aspecten zoals activatie, geluid detectie en het beperken van mogelijke nadelen. 
Als minimal viabel productfuncties besluiten we op basis hiervan dat:

* Wake detection: activatie als drempelwaarde overschreden wordt.

* Activatie van systeem: Python programma draait automatisch na opstarten, zonder manuele interactie.

* Onderdrukking van bijkomende ruis:  Het bijkomen lawaai van de ingebouwde ventilatie in de projector is geen storende factor.

***Een systeem dat automatisch geluid detecteert bij een slapend kind en een rustgevende projectie toont om het kind weer tot rust te brengen.***

## Divergentie & Ontwerpkeuzes


## Build & Test