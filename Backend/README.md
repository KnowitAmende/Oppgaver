![Knowit.png](../Knowit.png)
![Technology.png](../Technology.png)

# Oppgaver

Som en del av intervjuprosessen i Knowit benytter vi tekniske oppgaver. Disse oppgavene er ment som et hjelpemiddel for oss til å se hvordan våre kandidater tenker analytisk og angriper problemstillinger. Oppgavene er kun overordnet beskrevet slik at det er stor frihet i hvordan besvarelsen presenteres. Still gjerne forutsetninger der du føler for det.

Under intervjuet vil vi be deg presentere besvarelsen og forklare hva du har tenkt.

Eksempler på virkemidler i tillegg til tekst:

Flytdiagram

Kode

Skisser (f.eks i Visio)

Oppgave 3 leveres som kode og deles gjennom f.eks. github minst 24 timer før intervjuet.

Vi ser for oss at kandidater bruker ca. 3-5 timer på å ferdigstille oppgavene.

Selve intervjuet varer som regel rundt 1,5 time.

##

## Oppgave 1 – Bookingløsning

Din kunde, et padelsenter, ønsker seg en løsning for å kunne administrere reservasjoner av senterets baner.

Hvilke typer roller/personer ser du for deg trenger å bruke systemet og hvordan bruker rollene systemet?

Beskriv en løsning av systemet. Ta også med vurderinger rundt valg av plattform og teknologi.

Hvilke nye muligheter vil et slikt system gi for ledelsen av senteret?

## Oppgave 2 – Dårlig ytelse

Du jobber på et prosjekt der første versjon av et egenutviklet system er levert kunden. Applikasjonen består av en webklient som kjører på brukernes PC, tre webservere som er lastbalansert og en databaseserver.

I et møte med kunden får du vite at brukerne opplever applikasjonen som treg. Når du spør hva det er spesifikt som går tregt, får du til svar: Av og til går alt tregt, men noen ganger går det raskt.

Hvilke elementer mener du kan spille inn på ytelsen i slike systemer?

Hvordan vil du angripe dette problemet for å finne ut årsaken? Hvilke verktøy vil du bruke?

## Oppgave 3 – Integrasjonstjeneste

Kunden du jobber for ønsker at du skal utvikle en ny integrasjonstjeneste. Tjenesten skal tilgjengeliggjøre diverse _begreper_. Den skal erstatte en eldre eksisterende løsning og må derfor gi ut data på samme format. Tjenesten skal hente data fra en intern tjeneste som leverer data på et internt format.

### 3a

I denne oppgaven skal du sett opp en REST-applikasjon som integreres mot en intern tjeneste.


#### Oppsett av intern tjeneste
Vi bruker docker-compose for å sette opp tjenesten som du skal integrere mot.

Gjør følgende:

1. Installere docker-desktop eller manuelt installer det som trengs på din maskintype:
   https://www.docker.com/products/docker-desktop/
2. Kjør bash eller powershell filen build_and_run.
   (Denne bygger test api'et og så tar opp sql databasen og api'et)

Swagger dokumentasjonen for tjenesten kan hentes på http://localhost:8080/apidocs/.
For å hente ut alle begrep så kan man sende en POST-request til `localhost:8080/concepts`. Send med body `{ page: 1 }` for å hente neste side.

#### Utvikling av ny tjeneste

Lag en integrasjonstjeneste som tilbyr informasjon om _begreper_. Begrepene skal hentes fra den interne tjenesten og tilbys som angitt under.
Du kan selv velge teknologi og rammeverk, men gi gjerne en begrunnelse for valgene.

Tjenesten skal tilby følgende endepunkter:

`/begrep`  
Endepunkt som leverer en liste med alle begreper

`/begrep/{id}`  
Endepunkt som leverer ett begrep med angitt id.

Det forventes at endepunktene skal tilby begreper med følgende JSON-format:
```yaml
{
   "id": string,
   "subject": string,
   "prefLabel": string,
   "altLabel": string,
   "definition": { 
      "tekst": string,
      "lastUpdated": date 
   }
}
```

### 3b
Noen måneder etter produksjonssetting av løsningen du laget, kommer kunden med ønske om å oppgradere noen av konsumentene til tjenesten for å støtte flere språk. Det vil fortsatt være enkelte brukere som bruker JSON-formatet som var spesifisert i oppgave 3a. Du må lage støtte for nytt format som kan tilby flere språk på begrepene. 

Nytt format på begreper:
```yaml
{
   "id": string,
   "subject": { “nb”: string, “nn”: string, “en”: string },
   "prefLabel": { “nb”: string, “nn”: string, “en”: string },
   "altLabel": { “nb”: string, “nn”: string, “en”: string },
   "definition": {
      "tekst": { “nb”: string, “nn”: string, “en”: string },
      "lastUpdated": date
    }
}
```


<!--
## Oppgave 3b - DevOps

Ta utgangspunkt i applikasjonen som er bygget i oppgave 3.

### 1. Containerisering:

- Lag en Dockerfile for å containerisere den eksisterende integrasjonstjenesten.
- Sørg for at alle nødvendige avhengigheter er inkludert.

### 2. Orchestrering:

- Skriv en enkel Kubernetes-manifestfil for å deploye tjenesten.
- Inkluder en tjeneste for å eksponere tjenesten.

### 3. Overvåkning:

- Foreslå en metode for å implementere grunnleggende overvåkning av tjenesten i Kubernetes-miljøet.
- Beskriv kort hvilke nøkkelmetrikker du ville overvåket.
- Hvilke overvåkningsverktøy har du erfaring med? Hvordan ville du implementert overvåkning med disse verktøyene? Ta utgangspunkt i eventuelle skyplattformer du har erfaring med, eller beskriv hvordan du ville satt opp overvåkning med open source-verktøy.

### 4. CI/CD:

- Skissér et forslag til en enkel CI/CD-pipeline for denne applikasjonen.
- Forklar hvilke steg du ville inkludert i pipelinen.
- Hvilke CI/CD-verktøy har du brukt tidligere? Har du kjennskap til andre verktøy som kan brukes for å sette opp CI/CD?
- Hvordan ville du satt opp en CI/CD-pipeline hvis en kunde hadde krav om å sette opp alt on-prem? Beskriv trinnene og verktøyene du ville brukt i dette scenariet.
--!>
