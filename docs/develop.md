## Develop 


## Develop 1:

## Analyse en Prioritering
1. Onderzoeksvragen + hypotheses

1.1. Effectiviteit van het systeem

· Hoe effectief is het systeem in het detecteren en reageren op geluid?

· Het systeem reageert correct op relevante geluiden en vermindert het probleem waarvoor het ontworpen is.


1.2. Detectiedrempel (Decibel)

· Vanaf welk geluidsniveau moet het systeem reageren om vals alarm te vermijden?

· Een drempel boven het gemiddelde achtergrondgeluid zorgt ervoor dat het systeem enkel reageert op relevante geluiden.


1.3. Integratie van een speaker

· Verhoogt een geïntegreerde speaker de effectiviteit van het systeem?

· Een speaker zorgt voor een extra afschrikmiddel waardoor het systeem effectiever wordt.


1.4. Installatie / ophangen

· Is het haalbaar en praktisch om het systeem op te hangen?

· We vermoeden dat het systeem beter zal werken als het op een nachtkastje zal staan of op de grond. + het is makkelijker te instaleren.


1.5. Reactiesnelheid van het systeem

· Hoe snel moet het systeem reageren nadat een relevant geluid is gedetecteerd?

· Het systeem moet binnen enkele seconden reageren na detectie van een relevant geluid om effectief te zijn en de gewenste reactie uit te lokken


## Deconstructie

**storyboard**

Om een duidelijker beeld te krijgen in de visie van de werking van het systeem werd een nieuwe iteratie van een storyboard gemaakt. Dit werd getekend, rekening houdend met de inzchten die verkregen werden tijdens de feedback. Na overleg van de priotirtering werd dit [storyboard](/img/afbeelding_storyboard_develop_1.JPEG) getekend.

**Productarchitectuur (I/O)**

Om vroegtijdig een beeld te krijgen van naarmate de technische ideeën mogelijk waren, werd een raspberry pi zero 2 W aangekocht samen met een draagbare projector. Toen de verbinding met behulp van code slaagde, was het duidelijk dat er op deze manier verder gebouwd kon worden. De verschillende sensoren, actuatoren en datastromen  zijn in een [productarchitectuur](/img/productarchitectuur_develop_1.png) in kaart gebracht.

**User flows & Informatiearchitectuur**

* User flow 
Deze [user flow](/img/userflow_develop_1.jpg) is gebaseerd op de Hierarchical Task Analysis (HTA) met als hoofddoel “0. Het kind terug in slaap krijgen”. Wanneer het kind begint te huilen, detecteert de microfoon van het systeem het geluid en analyseert het of het effectief om huilen gaat. Indien dit het geval is, activeert het systeem automatisch de projector.

De projector projecteert rustgevende beelden op het plafond en kan tegelijk zachte, rustgevende deuntjes afspelen om het kind te kalmeren. Zodra het huilen stopt en het kind opnieuw rustig wordt, detecteert het systeem dit en dimt de projector geleidelijk. Daarna keert het systeem terug naar de monitoringmodus.

Deze flow toont hoe het systeem automatisch reageert op huilen en het kind helpt om opnieuw in slaap te vallen zonder tussenkomst van de ouders.


* Informatiearchitectuur

1. Information Ecology

Gebruikers:
· Ouders van kinderen die slaapregressie ervaren

· Vermoeide ouders die een snelle en eenvoudige interactie nodig hebben

· Het kind dat indirect met het systeem interacteert

Inhoud:
· Detectie van huilen

· Gevoeligheid van de microfoon

· Projector aan/uit

· Type projectie

· Animatie

· Rustgevende muziek

· Volume

· Timer

· Automatische activatie

· Slaapstatus van het kind

· Meldingen naar ouders

· Instellingen

Context:
· Gebruik tijdens de nacht

· Ouders hebben weinig aandacht of energie om met het systeem te interageren

· Minimale interactie is gewenst

· Het product reageert automatisch wanneer het kind huilt

2. Card Sorting Methode

Voor het bepalen van de informatiearchitectuur werd een open card sorting methode gebruikt. Deelnemers kregen kaarten met verschillende functies van het systeem en werden gevraagd deze in logische groepen te verdelen. Daarna gaven zij elke groep een naam. Deze methode helpt om de mentale modellen van gebruikers te begrijpen.

| Informatie-item               | Detectie | Projector | Geluid | Automatisch systeem | Instellingen |
|-------------------------------|----------|-----------|--------|---------------------|--------------|
| Microfoon detecteert huilen  | ✓        |           |        |                     |              |
| Huilanalyse                  | ✓        |           |        |                     |              |
| Projector starten            |          | ✓         |        |                     |              |
| Projectie kiezen             |          | ✓         |        |                     |              |
| Helderheid                   |          | ✓         |        |                     |              |
| Rustgevende muziek           |          |           | ✓      |                     |              |
| Volume                       |          |           | ✓      |                     |              |
| White noise                  |          |           | ✓      |                     |              |
| Automatische activatie       |          |           |        | ✓                   |              |
| Timer                        |          |           |        | ✓                   |              |
| Nachtmodus                   |          |           |        | ✓                   |              |
| Microfoon gevoeligheid       |          |           |        |                     | ✓            |
| Meldingen naar ouders        |          |           |        |                     | ✓            |



4. Diagram – Informatiearchitectuur (boomstructuur)

## 4. Diagram – Informatiearchitectuur (boomstructuur)

```
Slaapprojector Systeem
│
├── Detectie
│   ├── Microfoon detecteert huilen
│   ├── Huilanalyse
│   └── Slaapstatus van het kind
│
├── Projector
│   ├── Projector aan/uit
│   ├── Type projectie
│   ├── Animatie
│   └── Helderheid
│
├── Geluid
│   ├── Rustgevende deuntjes
│   ├── Muziek kiezen
│   ├── White noise
│   └── Volume
│
├── Automatische reactie
│   ├── Activatie bij huilen
│   ├── Timer
│   └── Nachtmodus
│
└── Instellingen
    ├── Gevoeligheid microfoon
    ├── Meldingen naar ouders
    └── Systeeminstellingen
```


**MVP-definitie**

In deze fase werd duidelijk dat de prioriteiten voor een deel anders liggen dan voordien. De focus van dit product lag in het begin van de fases vooral op het dilemma dat hing over het installatiesysteem (ophanging of neerzetten). In deze fase lag dit eerder achterwege. Nu de projector aangekocht is, kan meer gefocust worden op aspecten zoals activatie, geluid detectie en het beperken van mogelijke nadelen. 
Als minimal viabel productfuncties besluiten we op basis hiervan dat:

* Wake detection: activatie als drempelwaarde overschreden wordt.

* Activatie van systeem: Python programma draait automatisch na opstarten, zonder manuele interactie.

* Onderdrukking van bijkomende ruis:  Het bijkomend lawaai van de ingebouwde ventilatie in de projector is geen storende factor.

***Een systeem dat automatisch geluid detecteert bij een slapend kind en een rustgevende projectie toont om het kind weer tot rust te brengen.***

## Divergentie & Ontwerpkeuzes

* Morfologische Matrix:
## Morfologische Matrix – Slaapprojector systeem

| Functie / Probleem          | Oplossing 1            | Oplossing 2                 | Oplossing 3                         | Oplossing 4                         |
|-----------------------------|------------------------|-----------------------------|-------------------------------------|-------------------------------------|
| Detectie van huilen / wakker zijn | Microfoon              | Bewegingssensor             | Combinatie geluid + beweging        |                                     |
| Activatie systeem           | Automatisch bij huilen | Bij beweging van het kind   | Handmatig via app                   | Constant aan                        |
| Visuele geruststelling      | Sterrenprojectie       | Dierenanimaties             | Rustgevende kleuren                 | Bewegende wolken                    |
| Auditieve geruststelling    | Rustgevende deuntjes   | White noise                 | Hartslaggeluid                      | Natuurgeluiden                      |
| Intensiteit aanpassen       | Vast niveau            | Automatisch aanpassen       | Manueel instellen via de app        | Adaptief op basis van huilvolume    |
| Stoppen van projectie       | Timer                  | Wanneer huilen stopt        | Ouder via app                       | Geleidelijke dimmen                 |
| Feedback naar ouders        | Geen feedback          | Meldingen via app           | Geluidsmelding                      | Slaaprapport                        |


* Toelichting:

Om verschillende oplossingsmogelijkheden te verkennen werd een morfologische matrix opgesteld. Deze methode helpt om voor elke functionele uitdaging meerdere mogelijke oplossingen te genereren en te combineren. Hierdoor kan men systematisch verschillende ontwerpvarianten onderzoeken.

Voor het slaapprojectorconcept werden onder andere oplossingen onderzocht voor de detectie van huilen, de activatie van het systeem, visuele en auditieve geruststelling en het automatisch stoppen van het systeem. Door verschillende oplossingen uit de matrix te combineren kunnen meerdere conceptvarianten worden ontwikkeld.

## Build & Test