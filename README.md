# Website alexanderberg.ch – Anleitung zur Pflege

Diese Website wird von GitHub Pages aus den Dateien in diesem Repository erzeugt. Fast alles, was sich ändert, steht in einfachen Textdateien im Ordner **`_data/`**. Nach jeder Änderung baut GitHub die Seite selbst neu; nach **etwa ein bis zwei Minuten** ist sie online sichtbar.

## Wo steht was?

| Datei | Inhalt | erscheint auf |
|---|---|---|
| `_data/diary.yml` | Work Diary (In progress – Under review / in press – Recently published) | Startseite, Work Diary |
| `_data/publications.yml` | alle Publikationen, jede nur einmal; auch Rezensionen der Bücher | Publications, Work Diary, Conferences |
| `_data/talks.yml` | Vorträge | Talks |
| `_data/conferences.yml` | Tagungen: in Vorbereitung, die Reihe „Wittgenstein & Hegel“, weitere Tagungen und Workshops | Conferences |
| `_data/research.yml` | Texte der Forschungsseite (zwei Forschungsfelder, Habilitation) und die dort gezeigte Auswahl | Research |
| `_data/motto.yml` | Motto (Hegel, Wittgenstein und Schlegel) | Startseite |
| `_data/selected_texts.yml` | ausgewählte Texte zum Herunterladen (solange leer, ist die Rubrik unsichtbar) | Startseite, Selected Texts |
| `_data/memberships.yml` | Mitgliedschaften | About |
| `images/portrait.jpg` | Porträtfoto | Startseite |
| `files/conferences/` | PDFs der Tagungen | Conferences |
| `images/posters/` | Vorschaubilder der Tagungsplakate | Conferences |
| `texts/` | PDFs der „Selected Texts“ | Selected Texts |
| `berg-publications.bib` | BibTeX-Datei aller Publikationen, wird automatisch aus `publications.yml` erzeugt (siehe Abschnitt 7) | Publications (Download) |

Am Anfang jeder Datei in `_data/` steht eine **Vorlage** für einen neuen Eintrag (die Zeilen mit `#` sind Kommentare und erscheinen nicht auf der Seite).

## So bearbeitet man eine Datei (am Rechner und auf dem iPhone)

1. Auf **github.com** anmelden und das Repository **dralexanderberg/website** öffnen.
2. Den Ordner (z. B. `_data`) und dann die Datei (z. B. `diary.yml`) antippen.
3. Oben rechts auf das **Stift-Symbol** („Edit this file“) tippen. Auf dem iPhone ist es in Safari ebenfalls sichtbar; falls nicht, unten im Menü „Desktop-Website anfordern“ wählen.
4. Den Text ändern.
5. Oben rechts auf **„Commit changes…“** und im Fenster noch einmal auf **„Commit changes“** tippen.
6. Ein bis zwei Minuten warten, dann alexanderberg.ch neu laden.

**Drei Regeln für diese Dateien (YAML):**

- **Einrückung mit Leerzeichen**, nie mit Tabulator. Ein neuer Eintrag beginnt mit `- ` am Zeilenanfang; die Zeilen darunter sind mit zwei Leerzeichen eingerückt – genau wie bei den vorhandenen Einträgen.
- Enthält ein Text einen **Doppelpunkt mit Leerzeichen** (`: `) oder beginnt er mit einem Anführungszeichen, den ganzen Text in gerade Anführungszeichen setzen: `title: "Hegel: Eine Einführung"`.
- Am einfachsten ist es immer, einen **vorhandenen Eintrag zu kopieren** und abzuändern.

**Wenn etwas schiefgeht:** Im Repository oben auf **„Actions“** tippen. Ein rotes Kreuz zeigt, dass der letzte Bau fehlgeschlagen ist (meist ein Einrückungsfehler). Die alte Fassung der Seite bleibt online, bis der Fehler behoben ist. Über die Datei → „History“ sieht man jede frühere Fassung und kann sie zurückholen.

## 1. Einen Eintrag im Work Diary eine Stufe weiterschieben

Datei `_data/diary.yml` öffnen und beim betreffenden Eintrag zwei Zeilen ändern:

```yaml
- stage: review          # vorher: progress
  date: 2026-12-01       # Datum der Änderung, Form Jahr-Monat-Tag
```

Die Stufen heißen:

- `stage: progress` → „In progress“
- `stage: review` → „Under review / in press“
- `stage: published` → „Recently published“ (als `date` dann das Erscheinungsdatum)

Bei Bedarf auch die Zeile `status:` anpassen (z. B. `status: accepted, awaiting publication`) oder löschen.

Unter „Recently published“ zeigt die Startseite immer die **drei neuesten** Einträge; ältere wandern von selbst ins Archiv auf der Seite „Work Diary“. Die Zahl drei lässt sich in `_config.yml` bei `diary_recent_count` ändern.

**Neuer Eintrag:** die Vorlage am Dateianfang kopieren, unter die passende Überschrift setzen, das `# ` am Zeilenanfang entfernen und ausfüllen. Ist die Arbeit schon in `publications.yml` eingetragen, genügt `pub: kennung` statt `title:`; Titel und Link kommen dann von dort.

**Erscheint eine Arbeit:** in `publications.yml` beim Eintrag die Zeile `status: forthcoming` löschen, Datum, Seitenzahlen und Link (`url:`) ergänzen.

## 2. Einen neuen Vortrag eintragen

Datei `_data/talks.yml` öffnen. Direkt unter dem Kommentarblock (also **ganz oben**, da die neuesten zuerst stehen) einfügen:

```yaml
- title: Titel des Vortrags
  venue: Name der Tagung, Universität – Nov. 2026
  year: 2026
```

Optional: `url:` (Link zur Veranstaltung) und `video:` (Link zur Aufzeichnung, z. B. YouTube).

## 3. Eine neue Publikation eintragen

Datei `_data/publications.yml` öffnen. Den neuen Eintrag **oben in der passenden Gruppe** einfügen (Monographs, Edited volumes, Articles, Translations), z. B.:

```yaml
- id: kant-und-wittgenstein
  type: article
  title: Titel des Aufsatzes
  in: Titel des Bandes oder der Zeitschrift
  in_editors: Vorname Name & Vorname Name (eds.)
  publisher: Verlag, Ort
  date: 2027
  pages: 11–35
  url: https://doi.org/10.xxxx/xxxxx
```

- `id`: eine kurze, eindeutige Kennung in Kleinbuchstaben ohne Leerzeichen.
- `type`: `monograph`, `edited`, `article` oder `translation`.
- Noch nicht erschienen? Zeile `status: forthcoming` hinzufügen.
- Links nur auf Verlagsseite oder DOI, nicht auf Amazon.
- Rezension eines Buches: beim Buch unter `reviews:` einen Eintrag ergänzen (Beispiele bei „Wittgensteins Hegel“ und „Wittgenstein and Hegel“): `by:` Rezensent (Universität), `source:` Zeitschrift, Jahr, Seiten, optional `url:` (Link zur Rezension) und `quote:` (ein kurzes Zitat). Ist das Zitat nicht englisch, `lang: de` oder `lang: fr` und `translation:` mit der englischen Übersetzung dazuschreiben. Die Rezensionen erscheinen unter „Reviews and endorsements“ auf der Publications-Seite; beim Buch steht ein Link dorthin. Die PDFs der Rezensionen selbst nicht hochladen: Die Rechte liegen bei den Verlagen.
- Geht eine Rezension eines Sammelbandes eigens auf Dein Kapitel ein: beim Kapitel unter `discussed:` die Stelle eintragen (gleiche Felder wie bei `reviews:`, Beispiel bei „Identity in Difference“). Sie erscheint bei den Rezensionen des Bandes.
- Blurbs von der Rückseite eines Buches: beim Buch unter `endorsements:` mit `by:` und `quote:` (Beispiel bei „Wittgenstein and Classical German Philosophy“).
- Für die BibTeX-Datei sind außerdem `isbn:`, `doi:` und bei Zeitschriftenaufsätzen `journal:`, `volume:`, `issue:` nützlich (siehe Abschnitt 7).

## 4. Einen Text mit PDF unter „Selected Texts“ ergänzen

1. Das PDF hochladen: im Repository den Ordner **`texts`** öffnen → **„Add file“** → **„Upload files“** → PDF auswählen → **„Commit changes“**. Dateinamen ohne Leerzeichen und Umlaute, z. B. `berg-2019-identity-in-difference.pdf`.
2. Datei `_data/selected_texts.yml` öffnen und nach der Vorlage einen Eintrag anlegen:

```yaml
- pub: identity-in-difference
  file: /texts/berg-2019-identity-in-difference.pdf
  version: accepted manuscript
  cite: "Alexander Berg, Identity in Difference – Wittgenstein’s Hegel, in: Wittgenstein and Hegel – Reevaluation of Difference, ed. Jakub Mácha & Alexander Berg (De Gruyter 2019), 349–364."
  open_access: https://…
```

- `pub`: die Kennung (`id`) aus `publications.yml`.
- `version`: `preprint`, `accepted manuscript`, `author’s corrected version` oder `publisher's version` – bitte die Bedingungen des Verlags beachten.
- `open_access` nur, wenn es eine frei zugängliche Fassung beim Verlag gibt; sonst die Zeile weglassen.

Sobald der erste Eintrag da ist, erscheinen die Rubrik auf der Startseite (die ersten drei Texte) und der Menüpunkt „Selected Texts“ von selbst.

## 5. Das Porträt austauschen

1. Ordner **`images`** öffnen → **„Add file“** → **„Upload files“**.
2. Das neue Foto hochladen; es muss genau **`portrait.jpg`** heißen (die alte Datei wird ersetzt). Am besten ein Foto mit mindestens 800 Pixel Breite und unter 1 MB.
3. Datei **`_config.yml`** öffnen und die Zeile `portrait_crops: true` in `portrait_crops: false` ändern → „Commit changes“.

Die Seite schneidet das Foto dann selbst hochkant zu (Gesicht etwa in der Mitte, etwas oberhalb). Die Dateien `portrait-400.jpg`, `portrait-600.jpg` und `portrait-800.jpg` sind fertig zugeschnittene, kleinere Fassungen des jetzigen Fotos; sie werden mit `portrait_crops: false` nicht mehr benutzt und können bleiben.

## 6. Tagungen, Forschungsseite und Motto

- **Geplante Tagung konkretisieren:** In `_data/conferences.yml` unter `in_preparation:` beim Eintrag die Zeilen `dates:`, `place:` und `with:` ergänzen (Vorlage am Dateianfang). Nach der Tagung den Eintrag unter `further:` verschieben.
- **Weitere Tagung oder Workshop eintragen:** in `_data/conferences.yml` unter `further:` ganz oben, nach der Vorlage am Dateianfang.
- **Forschungsseite:** Texte und Auswahl stehen in `_data/research.yml`. Eine Publikation erscheint dort, wenn ihre Kennung (`id` aus `publications.yml`) in der Liste `publications:` steht. Ein Vortrag erscheint, wenn er in `talks.yml` eine Zeile `id:` hat und diese Kennung unter `talks:` steht.
- **Plakat einer Tagung der Reihe:** Vorschaubild (480 Pixel breit) in den Ordner `images/posters/`, das PDF in `files/conferences/`. In `_data/conferences.yml` beim Eintrag `poster:` mit dem Pfad des Bildes ergänzen, unter `files:` das PDF mit `label: Poster` und, wenn jemand anderes das Plakat gestaltet hat, unter `poster_by:` deren oder dessen Namen (erscheint unter dem Plakat); `poster_photo:` nennt bei Bedarf die Fotografin oder den Fotografen. Das geht auch bei einem Eintrag unter `further:`.
- **Buchcover:** Bild (440 Pixel breit) in den Ordner `images/covers/`, dann in `_data/publications.yml` beim Buch `cover:` mit dem Pfad und `cover_height:` mit der Höhe des Bildes in Pixeln ergänzen; `cover_credit:` nennt bei Bedarf, wer das Coverbild gemacht hat (erscheint neben dem Cover). Das Cover erscheint rechts neben dem Eintrag auf Publications, Research und Conferences (auf breiten Bildschirmen am rechten Rand neben der Liste); bei einem Kapitel ist es das Cover des Sammelbandes.
- **PDFs von Tagungen:** vor dem Hochladen prüfen, dass keine privaten Kontaktdaten darin stehen (E-Mail-Adressen, Telefonnummern, Anschriften). Im Abstract-Heft von Zagreb 2024 sind die E-Mail-Adressen deshalb entfernt.
- **ORCID-iD und PhilPeople:** stehen in `_config.yml` bei `orcid:` und `philpeople:` (der Profilname aus philpeople.org/profiles/…) und erscheinen auf der Contact-Seite, ORCID mit dem grünen iD-Symbol. Wird eine Zeile geleert, verschwindet der jeweilige Link.
- **Motto:** in `_data/motto.yml`, drei Zitate (Hegel, Wittgenstein, Schlegel). Auf breiten Bildschirmen stehen die ersten beiden nebeneinander und das dritte mittig darunter, auf dem Handy alle untereinander. Um weniger Zitate zu zeigen, einen Eintrag löschen (von „- text“ bis vor das nächste „- text“); ohne Einträge verschwindet das Motto.

## 7. Bibliographie-Datei (BibTeX)

Die Datei **`berg-publications.bib`** (online unter alexanderberg.ch/berg-publications.bib, verlinkt oben auf der Seite „Publications“) entsteht bei jedem Bau **automatisch aus `_data/publications.yml`**. Sie wird nie von Hand bearbeitet: Wer eine Publikation in der yml einträgt oder ändert, hat sie auch in der BibTeX-Datei. Geplante Titel (`status: planned`) und die Online-Edition fehlen darin, Titel mit `status: forthcoming` sind als solche markiert.

Diese Felder nutzt vor allem die BibTeX-Datei:

- `isbn:` – auf der Website nur bei Büchern ohne DOI sichtbar, in der BibTeX-Datei immer (bei Kapiteln die ISBN des Bandes).
- `doi:` – nur nötig, wenn `url:` nicht auf doi.org zeigt (z. B. beim Anthem-Kapitel, das auf die Verlagsseite verlinkt).
- `journal:`, `volume:`, `issue:` – bei Aufsätzen in Zeitschriften; dann erscheint der Eintrag in der BibTeX-Datei als Zeitschriftenaufsatz statt als Beitrag in einem Sammelband.
- `url_label:` – eigener Text für den Link, z. B. `Preview (PDF)` bei den Leseproben von Bautz. Solche Links kommen nicht in die BibTeX-Datei.

**Import in andere Dienste:**

- **Zotero:** Datei herunterladen, dann in Zotero „Datei → Importieren…“.
- **ORCID:** im Bereich „Works“ auf „+ Add“: Werke mit DOI am besten über „Add DOI“ (dann kommen die Daten direkt von Crossref), den Rest über „Import BibTeX“. ORCID zeigt vorher eine Liste, aus der man auswählt (forthcoming-Titel besser erst nach Erscheinen). Die Übersetzungen besser von Hand als „Translation“ anlegen.
- **PhilPapers:** zuerst unter „My works“ prüfen, was PhilPapers schon über den Namen zugeordnet hat, und Fremdes mit „not mine“ markieren; dann „Submit material → Upload a bibliography“ und die Datei hochladen. Vorhandene Einträge werden zugeordnet, nur fehlende neu angelegt.

## Technisches (nur zur Information)

- Jekyll über GitHub Pages, ohne eigenen Build-Schritt. Seitenlayout in `_layouts/` und `_includes/`, Gestaltung in `assets/css/main.css`.
- Schrift: P052 (URW, Palatino-ähnlich), lokal eingebunden unter `assets/fonts/` (Lizenz: `assets/fonts/LICENSE-URW.txt`; Quelle: github.com/ArtifexSoftware/urw-base35-fonts).
- Keine Cookies, kein Tracking, keine externen Skripte oder Schriften; Videos nur verlinkt.
- `CNAME` enthält die Domain alexanderberg.ch; `sitemap.xml` wird automatisch erzeugt.
- Lokale Vorschau (optional, am Rechner): `jekyll serve`, dann http://localhost:4000 öffnen.
