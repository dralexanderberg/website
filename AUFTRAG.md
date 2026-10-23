# Neue Website alexanderberg.ch

Auftrag und Ablauf, Fassung 4, Stand 23. Oktober 2026. Entschieden: eine Sprache (Englisch), ein „Work Diary“ in drei Stufen auf der Startseite, „Selected Texts“ zum Selbstarchivieren, eine eigene Seite zur Tagungsreihe „Wittgenstein & Hegel“ 2017–2024; alle Angaben aus der bisherigen englischen Fassung und der alten Tagungsseite. Teil A beschreibt die Schritte, Teil B ist der Auftrag für die Claude-Code-Sitzung, Teil C hält die getroffenen Entscheidungen fest. Der Anhang enthält die Inhalte.

# Teil A – Ablauf

## Erledigt (22. Oktober)

- Domain alexanderberg.ch bei Infomaniak registriert (ohne Zusatzoptionen); verlängert sich automatisch.

- E-Mail-Adresse alexander@alexanderberg.ch in der kostenlosen kSuite angelegt, auf Mac und iPhone eingerichtet, Empfang von außen getestet.

- GitHub-Konto „dralexanderberg“ (Anmeldung über iCloud-Adresse, neue Adresse zusätzlich hinterlegt).

- TXT-Eintrag \_github-pages-challenge-dralexanderberg bei Infomaniak gesetzt; Verifizierung bei GitHub läuft. Der Eintrag bleibt dauerhaft stehen.

- Offene Fragen geklärt (23. Oktober, s. Teil C); Porträtfoto liegt vor.

## Vor dem Start

1.  **Verifizierung abschließen** (falls noch offen): GitHub → Settings → Pages → bei alexanderberg.ch „Verify“.

2.  **Repository „website“ anlegen** (Public, mit README), falls noch nicht geschehen.

3.  **Porträtfoto hochladen.** Im Repository „Add file“ → „Upload files“, das Foto hineinziehen, als Ordner „images/“ angeben, die Datei portrait.jpg nennen, „Commit changes“.

4.  **Auftrag hochladen.** Die Datei AUFTRAG.md (die maschinenlesbare Fassung dieses Dokuments) auf dieselbe Weise ins Hauptverzeichnis des Repositorys laden.

5.  **Tagungs-PDFs sichern und hochladen.** Die acht PDFs aus der Liste „Tagungs-PDFs“ im Anhang auf den Mac laden (Terminal-Befehl oder einzeln anklicken und sichern). Dann im Repository „website“ auf „Add file“ → „Upload files“, alle PDFs hineinziehen und oben im Pfad den Ordner „files/conferences/“ angeben, unten „Commit changes“. So liegen sie für Claude Code bereit, auch wenn die alte Weebly-Seite einmal verschwindet.

## Bis 5. November: Website bauen lassen

1.  **Claude Code starten.** Auf claude.ai über das Symbol \</\> Claude Code öffnen, „Cloud“ wählen und GitHub verbinden. Bei der Frage nach dem Zugriff „Only select repositories“ → „website“ wählen. Dann als Auftrag schreiben: „Lies AUFTRAG.md in diesem Repository und setze Teil B um. Inhalte im Anhang, Tagungs-PDFs unter files/conferences/, Porträt unter images/portrait.jpg. Zeig mir zuerst Struktur und Startseite.“ Das verbraucht zuerst das Cloud-Guthaben.

2.  **Ergebnis prüfen.** Claude Code zeigt zuerst Struktur und Startseite, danach die ganze Website. Korrekturen in derselben Sitzung nennen.

## Danach: Veröffentlichen und Domain verbinden

1.  **GitHub Pages einschalten.** Im Repository Settings → Pages → „Deploy from a branch“, Branch „main“. Bei „Custom domain“ alexanderberg.ch eintragen und speichern.

2.  **Mini-Webseite von Infomaniak lösen.** Beim Kauf wurde automatisch eine kostenlose „Einfache Webseite 1“ (Starter-Hosting) angelegt; sie hält die Domain derzeit über einen A-Eintrag (128.65.195.180) besetzt. Im Manager unter Web & Domains → Websites die Domain von dieser Webseite trennen oder die Webseite löschen.

3.  **DNS bei Infomaniak umstellen** (DNS-Zone, „Vereinfachte Ansicht“): den alten A-Eintrag für alexanderberg.ch löschen; vier A-Einträge auf 185.199.108.153, 185.199.109.153, 185.199.110.153 und 185.199.111.153 setzen (Quelle leer lassen); einen CNAME-Eintrag mit Quelle „www“ auf dralexanderberg.github.io. Adressen vorher mit der GitHub-Anleitung „Managing a custom domain for your GitHub Pages site“ abgleichen. Die MX-Einträge (E-Mail) und den TXT-Eintrag für GitHub nicht anfassen.

4.  **HTTPS.** Nach einigen Stunden bei GitHub → Settings → Pages „Enforce HTTPS“ anhaken.

5.  **Hinweis auf den alten Seiten.** Oben auf der englischen und der deutschen Google-Seite „This site has moved to alexanderberg.ch“ mit Link; auf der Weebly-Tagungsseite (falls Zugang) „The documentation of the conference series is now at alexanderberg.ch/conferences“. Beide einige Monate stehen lassen.

# Teil B – Auftrag an Claude Code

Baue in diesem Repository die persönliche akademische Website von Alexander Berg, M.A., Ph.D., Philosoph (Feodor Lynen Research Fellow der Alexander von Humboldt-Stiftung an der Universität Zürich). Sie ersetzt seine bisherige Google-Sites-Seite und wird über GitHub Pages unter alexanderberg.ch veröffentlicht (GitHub-Benutzer dralexanderberg). Leser sind Fachkollegen, Herausgeber und Verlage, Veranstalter, Berufungs- und Habilitationskommissionen.

## Leitidee

Die Seite soll Leser einladen und ihnen gleich etwas Nützliches bieten, und sie soll den Verfasser als arbeitenden Wissenschaftler zeigen: woran er gerade arbeitet, was in Begutachtung oder im Druck ist, was zuletzt erschienen ist. Kollegen sollen sehen, dass es vorangeht und dass zugesagte Beiträge in guten Händen sind. Der Schwerpunkt liegt auf dem Aktuellen; das vollständige Verzeichnis steht dahinter. Nützliches Material bieten vor allem die „Selected Texts“ und die Dokumentation der Tagungsreihe „Wittgenstein & Hegel“, die er als Hauptorganisator getragen hat.

## Sprache und Ton

- Die ganze Website ist englisch; es gibt keine deutsche Fassung. Bibliographische Titel und Vortragstitel bleiben in der Originalsprache.

- Vorstellung und Work Diary in der ersten Person, sachlich und knapp.

## Seitenstruktur

- **Home:** Name, Porträt, kurze Vorstellung (Deutscher Idealismus und Wittgenstein, literarische Form der Philosophie); darunter das Work Diary; darunter zwei oder drei „Selected Texts“ und ein Hinweis auf die Tagungsreihe.

- **Work Diary** (auf der Startseite, zusätzlich als eigene Seite mit Archiv): drei Stufen – „In progress“, „Under review / in press“, „Recently published“. Jeder Eintrag eine Zeile mit Datum der letzten Änderung. Auf der Startseite nur die aktuellen Einträge; Einträge unter „Recently published“, die älter als zwölf Monate sind, wandern automatisch ins Archiv. Keine Zieltermine für unfertige Arbeiten.

- **Selected Texts:** wenige ausgewählte Texte zum Lesen oder Herunterladen. Bei jedem steht die Fassung (Preprint, accepted manuscript oder Verlags-PDF), die Angabe der Druckfassung „Please cite the published version: …“ und gegebenenfalls ein Link zur frei zugänglichen Verlags- oder Tagungsfassung. Die Texte wählt der Verfasser erst, wenn die Website steht: Datei und Vorlage anlegen, die Rubrik aber ausblenden, solange selected_texts.yml leer ist.

- **Conference Series „Wittgenstein & Hegel“ (2017–2024)** unter /conferences/: kurze Einleitung zur Reihe (aus dem Anhang); dann je Tagung ein Abschnitt, neueste zuerst, mit Titel, Ort und Datum, Organisatoren, Keynotes bzw. Leitung, Förderern, Vortragsliste (aus dem Anhang oder aus dem jeweiligen Programm-PDF), Links zu Programm, Abstracts und Poster (PDFs im Repository unter /files/conferences/) und zu vorhandenen Aufzeichnungen (YouTube-Links, nicht eingebettet). Am Ende: die drei Bände, die aus der Reihe hervorgegangen sind. Mitorganisatoren stets nennen; Alexander Berg erscheint als Initiator und Hauptorganisator der Reihe.

- **Publications:** Monographs, Edited volumes, Articles, Translations, Online edition (Wittgenstein Nachlass, Bergen), Reviews of my books; jeweils umgekehrt chronologisch.

- **Talks** und **Conferences organized** (Überblick; die sechs Tagungen der Reihe verlinken auf /conferences/).

- **About:** Studium und Forschung, Sprachen, Mitgliedschaften.

- **Contact:** vorerst nur die E-Mail-Adresse alexander@alexanderberg.ch, keine Profil-Links (ORCID und weitere Profile ergänzt der Verfasser später); dazu Impressum (Name und E-Mail genügen für eine private Seite) und ein kurzer Datenschutzhinweis (Hosting bei GitHub, keine Cookies, kein Tracking; YouTube nur verlinkt).

## Gestaltung

- Ruhig, typographisch, wissenschaftlich: gut lesbare Serifenschrift (Palatino-ähnlich, lokal eingebunden), viel Weißraum, keine Animationen. Als Akzentfarbe das dunkle Nachtblau aus dem Hintergrund des Porträts, damit Foto und Seite zusammenpassen.

- Porträt: images/portrait.jpg (Querformat 1500 × 1000, dunkelblauer Hintergrund); für die Startseite passend zuschneiden (quadratisch oder hochkant, Gesicht mittig), in webtauglichen Größen ausliefern.

- Die drei Stufen des Work Diary klar unterscheidbar, aber unaufdringlich, etwa als drei Spalten am Rechner und untereinander auf dem Telefon. Auf der Tagungsseite die Vortragslisten aufklappbar, damit die Seite übersichtlich bleibt.

- Funktioniert auf dem Telefon ebenso gut wie am Rechner; Druckansicht ohne Navigation; barrierearm (Kontraste, Alternativtexte, Tastaturbedienung).

## Technik

- Jekyll, wie es GitHub Pages ohne eigenen Build-Schritt unterstützt. Alles Veränderliche steht in Datendateien unter \_data/ (YAML): diary.yml (Work Diary), publications.yml, talks.yml, conferences.yml (Reihe samt Vorträgen, PDFs und Videos), memberships.yml, selected_texts.yml. Jede Publikation steht nur einmal und wird auf allen Seiten daraus erzeugt.

- Tagungs-PDFs liegen bereits unter /files/conferences/ (vom Verfasser hochgeladen); falls nicht, Platzhalter setzen und melden. PDFs für „Selected Texts“ unter /texts/.

- Datei CNAME mit alexanderberg.ch anlegen.

- Keine externen Skripte, Schriften oder Tracker; keine Cookies; keine eingebetteten Videos.

- Für Suchmaschinen: aussagekräftige Seitentitel und Beschreibungen, sitemap.xml, strukturierte Daten (schema.org Person, vorerst ohne Profil-Links; Event für die Tagungen).

- Links auf Verlagsseiten oder DOIs statt auf Amazon-Suchergebnisse; Tracking-Parameter aus Links entfernen.

## Pflege

Lege eine README.md auf Deutsch an, die für einen Laien Schritt für Schritt erklärt, wie man im GitHub-Web-Editor (auch vom iPhone aus) einen Eintrag im Work Diary eine Stufe weiterschiebt, einen neuen Vortrag oder eine neue Publikation einträgt, einen Text mit PDF unter „Selected Texts“ ergänzt und das Porträt austauscht. Vorlagen für einen neuen Eintrag als Kommentar am Anfang jeder Datendatei.

## Inhalte und Arbeitsweise

- Die Inhalte stehen im Anhang, die Anfangseinträge des Work Diary und die Daten der Tagungsreihe ebenfalls. Nichts erfinden: Wo eine Angabe fehlt oder unklar ist, einen sichtbaren Platzhalter setzen und am Ende auflisten.

- Offensichtliche Tippfehler der alten Seiten sind im Anhang bereits berichtigt.

- Erst Seitenstruktur und einen Entwurf der Startseite zeigen, nach Zustimmung die ganze Website bauen, dann eine Vorschau geben und auf main committen.

- Das Repository ist öffentlich: AUFTRAG.md nach Fertigstellung aus dem Repository entfernen (nach Rückfrage).

# Teil C – Entscheidungen (geklärt am 23. Oktober)

1.  **Work Diary:** Die Einträge im Anhang sind auf dem aktuellen Stand. Hegel-Jahrbuch-Beitrag und Synthesis-Philosophica-Heft sind abgeschlossen und warten auf die Veröffentlichung.

2.  **Selected Texts:** werden ausgewählt, wenn die Website steht. Bis dahin bleibt die Rubrik ausgeblendet.

3.  **Kontakt:** vorerst nur die E-Mail-Adresse; ORCID und andere Profile folgen später.

4.  **Schreibweisen:** durchgehend „Denys Kaidalov“. Der Aufsatz in den Wittgenstein-Studien 11 heißt „Wittgenstein und die Begriffe des Psychischen bei Hegel“.

5.  **Noch offen, aber nicht eilig:** ob die Einleitung des De-Gruyter-Bandes von 2019 (intro.pdf) auf der Seite stehen darf (Verlagsvertrag); bis dahin nur Inhaltsverzeichnis und Link zum Verlag. Den Mitorganisatoren kurz mitteilen, dass die Dokumentation der Tagungsreihe künftig auf alexanderberg.ch weiterlebt.

# Anhang – Inhalte (englisch)

Übernommen aus der englischen Fassung von sites.google.com/view/alexander-berg und der Tagungsseite wittgensteinhegel2017.weebly.com, Stand 22. Oktober 2026.

## Person

- Alexander Berg, M.A., Ph.D.

- Feodor Lynen Research Fellow of the Alexander von Humboldt Foundation, University of Zurich; research project On the Literary Form of Philosophy.

- E-mail: alexander@alexanderberg.ch

## Work Diary – Anfangseinträge

### In progress

- Zur literarischen Form von Philosophie – Grundlinien eines Systems der Literatur (habilitation thesis, University of Zurich). The part on Hegel’s Phenomenology of Spirit is largely complete; I am now writing the part on the literary form of Wittgenstein’s Philosophical Investigations. A book that systematizes and integrates the different methods of literary-philosophical research to make them more productive for philosophical inquiry and problem-solving. It is grounded in the idea of a “system of literature” as a methodological foundation for understanding philosophical writings, and demonstrates the method on two exemplary works: Hegel’s Phenomenology of Spirit and Wittgenstein’s Philosophical Investigations.

- Up next: Die Liebe zum Wissen ablegen. Hegel und Wittgenstein als gegenläufige Weisheitskritiken – for the new series Weisheit und Weisheitskritik. Philosophische Erkundungen, ed. Moritz R. Pretzsch & Jan Kerkmann (Velbrück Wissenschaft).

- Planned: Wittgenstein and Hegel, Elements in the Philosophy of Ludwig Wittgenstein, ed. David G. Stern, Cambridge University Press (planned 2027). It will bring together what five conferences, two anthologies, one monograph and a series of articles and talks on Wittgenstein and Hegel have yielded, in a compact yet narratively accessible form. Series: https://www.cambridge.org/core/publications/elements/philosophy-of-ludwig-wittgenstein

### Under review / in press

- Goethe’s Influence on Hegel’s Phenomenology of Spirit – for Goethe and Philosophy, ed. Jan Kerkmann & Moritz Pretzsch (Springer, 2026); submitted, under review.

- Zur literarischen Form der Phänomenologie des Geistes – Methode und Bedeutung – Hegel-Jahrbuch 2024, ed. Brady Bowman, Myriam Gerhard & Jure Zovko (Duncker & Humblot); accepted, awaiting publication.

- Special issue Wittgenstein and Hegel on Normativity and Rationality, ed. Alexander Berg & Kenan Šljivo, Synthesis Philosophica 41/1, with my article Possibility and Probability – Wittgenstein in Russia, and the Curious Case of the Yellow Book; completed, awaiting publication. Presented at the XXXVI International Hegel Congress, Rome, Sept. 2026.

### Recently published

- Ludwig Wittgenstein and the Photography of Everyday Life, in: Wittgenstein and Popular Culture (Anthem Press), July 2026.

- Talk: Goethe’s Artistic Influence on the Phenomenology of Spirit, XXXVI International Hegel Congress, Rome, Sept. 2026.

- Book presentation: Wittgenstein and Hegel on Normativity and Rationality (Synthesis Philosophica special issue), XXXVI International Hegel Congress, Rome, Sept. 2026.

- Wittgenstein and Classical German Philosophy – Logic, Language, Life, ed. with Denys Kaidalov (De Gruyter 2025).

- Studien zur Transzendenz – Säkularisierungstheorie bei Charles Taylor und Falk Wagner (Bautz, April 2025).

## Monographs

- Wittgenstein and Hegel \[Elements in the Philosophy of Ludwig Wittgenstein, David G. Stern (ed.), Cambridge University Press 2027, planned\]

- Studien zur Transzendenz – Säkularisierungstheorie bei Charles Taylor und Falk Wagner \[Libri Nigri, Hans Rainer Sepp (ed.), Bautz 2025\] – ISBN 3689110300 (bisher Amazon-Link; Verlagsseite suchen)

- Wittgensteins Hegel, Wilhelm Fink Verlag, Paderborn \[2021, with the support of the VG Wort Science Promotion Fund\] – https://brill.com/display/title/54766

- Transzendenz bei Hegel und Heidegger \[Libri Virides, Hans Rainer Sepp (ed.), Bautz 2012\] – ISBN 3883097365 (bisher Amazon-Link; Verlagsseite suchen)

## Edited volumes

- Special Issue: Wittgenstein and Hegel on Normativity and Rationality, Alexander Berg & Kenan Šljivo (eds.), Synthesis Philosophica, vol. 41, no. 1 \[Filozofski Fakultet, Zagreb 2026, forthcoming\] – https://hrcak.srce.hr/en/synthesis-philosophica

- Wittgenstein and Classical German Philosophy – Logic, Language, Life, Alexander Berg & Denys Kaidalov (eds.), De Gruyter \[Berlin/New York 2025\] – https://www.degruyter.com/document/isbn/9783110698442/html

- Wittgenstein and Hegel – Reevaluation of Difference, Jakub Mácha & Alexander Berg (eds.), On Wittgenstein (5), James Conant, Wolfgang Kienzler, Stefan Majetschak, Volker Munz, Josef Rothhaupt, David Stern, Wilhelm Vossenkuhl (eds.) \[De Gruyter, Berlin/New York 2019\] – https://doi.org/10.1515/9783110572780

- Ambivalenzen des Heiligen, Alexander Berg, Friedrich Hausen, René Kaufmann, Beatrix Kersten, Martin Krebs, Anna Maria Martini (eds.), Journal für Religionsphilosophie (3), Arbeitsgemeinschaft Religionsphilosophie Dresden e. V. (ed.) \[Verlag Text & Dialog, Dresden 2014\]

## Reviews of my books

Wittgenstein and Hegel – Reevaluation of Difference (De Gruyter 2019):

- Stany Mazurkiewicz (Université de Liège), Bulletin de littérature hégélienne XXX, 2020, pp. 182–183.

- Guido Tana (University of Pavia), Verifiche XLIX (1–2), 2020, pp. 333–346.

- Diogo Ferrer (University of Coimbra), Wittgenstein-Studien 14 (1), 2023, pp. 277–283.

Wittgensteins Hegel (Fink 2021):

- Peter Eschweiler, Bibliographie zur Symbolik, Ikonographie und Mythologie 54/2021, pp. 22–23.

## Articles

- Goethe’s Influence on Hegel’s Phenomenology of Spirit, in: Goethe and Philosophy, Jan Kerkmann & Moritz Pretzsch (eds.) \[Springer, Berlin 2026\]

- Zur literarischen Form der Phänomenologie des Geistes – Methode und Bedeutung, in: Hegel-Jahrbuch 2024, Brady Bowman, Myriam Gerhard & Jure Zovko (eds.) \[Duncker & Humblot, Berlin 2026, forthcoming\]

- Possibility and Probability – Wittgenstein in Russia, and the Curious Case of the Yellow Book, in: Wittgenstein and Hegel on Normativity and Rationality, Alexander Berg & Kenan Šljivo (eds.), Synthesis Philosophica, vol. 41, no. 1 \[Filozofski Fakultet, Zagreb 2026, forthcoming\]

- Ludwig Wittgenstein and the Photography of Everyday Life, in: Wittgenstein and Popular Culture, Bernhard Stricker & Martin Urschel (eds.), Anthem Studies in Wittgenstein, Konstantin Sandis (ed.) \[Anthem Press, London, July 2026\] – https://anthempress.com/wittgenstein-and-popular-culture-hb

- Wittgenstein’s ‘Übersichtliche Darstellung’ and Hegel’s ‘Speculative Philosophy’, in: Wittgenstein and Classical German Philosophy, Alexander Berg & Denys Kaidalov (eds.) \[De Gruyter, Oct. 2025\]

- Wittgenstein and Classical German Philosophy – or the Peculiar Nature of Philosophy, in: International Conference Wittgenstein and Hegel on Normativity and Rationality, Zagreb, 9–11 Sept. 2024, Hrvoje Jurić & Karlo Gardavski (eds.) \[Croatian Philosophical Society 2024\]

- The Method of Absolute Negativity and the Tractatus Logico-Philosophicus – Wittgenstein, William James and Hegel, in: 100 Years of Tractatus Logico-Philosophicus – 70 Years after Wittgenstein’s Death. A Critical Assessment. Contributions of the 44th International Wittgenstein Symposium, vol. XXIX, Esther Heinrich-Ramharter, Alois Pichler, Friedrich Stadler (eds.) \[Kirchberg a. W. 2023\] – https://symposium.alws.at/api/content/volume/2023.pdf

- Wittgenstein’s Photo Album as a Philosophical Experiment, in: Zeit der Unkultur – Ludwig Wittgenstein im Österreich der Zwischenkriegszeit, Károly Kókai (ed.) \[NoPress, Vienna 2022: 204–220\]

- Wittgensteins Übersichtliche Darstellung und Hegels Spekulative Philosophie, in: Wittgenstein and Platonism. Contributions of the 43rd International Wittgenstein Symposium, vol. XXVIII, Herbert Hrachovec & Jakub Mácha (eds.) \[Kirchberg a. W. 2022\]

- Wittgensteins philosophisches Photoalbum, in: Fotografische Differenz. Interkulturelle Theorien zum fotografischen Bild, Hans Rainer Sepp (ed.) \[Bautz 2022: 194–239\]

- Wittgenstein und die Begriffe des Psychischen bei Hegel, in: Special section Wittgenstein über das Psychische, Richard Raatzsch (ed.), Wittgenstein-Studien, vol. 11 \[Walter de Gruyter, Berlin/New York 2019: 137–168\] – https://doi.org/10.1515/witt-2020-0008

- Identity in Difference – Wittgenstein’s Hegel, in: Wittgenstein and Hegel – Reevaluation of Difference, Jakub Mácha & Alexander Berg (eds.) \[De Gruyter 2019: 349–364\]

- Wittgenstein, die Grundlagen der Mathematik, und Hegel, in: Philosophie der Logik und Mathematik. Beiträge zum 41. Internationalen Wittgenstein Symposium, vol. XXVI, Gabriele M. Mras, Paul Weingartner, Bernhard Ritter (eds.) \[Kirchberg a. W. 2018: 15 f.\]

- Vom Wissen zum Denken – Wittgensteins dialektische Methode am Beispiel der Seminarnotizen G. E. Moores, in: Contributions of the 40th International Wittgenstein Symposium, vol. XXV, Christoph Limbeck-Lilienau, Friedrich Stadler (eds.) \[Kirchberg a. W. 2017: 20 f.\] – https://www.alws.at/alws/wp-content/uploads/2020/03/papers-2017.pdf

- Ernste Spiele – eine kleine Erzählung von Wittgenstein bis Schiller und zurück, in: Ernste Spiele, Journal für Religionsphilosophie (5), Arbeitsgemeinschaft Religionsphilosophie Dresden e. V. (ed.) \[Verlag Text & Dialog, Dresden 2016: 57 f.\]

- Vom „pun“ zum Sprachspiel – Wittgenstein, Russell, Bradley, Hegel und der Streit um das concrete universal, in: Contributions of the 39th International Wittgenstein Symposium, vol. XXIV, Stefan Majetschak & Anja Weiberg (eds.) \[Kirchberg a. W. 2016: 20 f.\] – https://www.alws.at/alws/wp-content/uploads/2019/01/papers-2016.pdf

- Probleme in der historischen Wittgenstein-Forschung – Wunsch, Wirklichkeit und Russische Philosophie, in: Contributions of the 38th International Wittgenstein Symposium, vol. XXIII, Christian Kanzian, Josef Mitterer, Katharina Neges (eds.) \[Kirchberg a. W. 2015: 23 f.\] – https://www.alws.at/alws/wp-content/uploads/2018/06/papers-2015.pdf

- Grundlose Gewissheit und Absolutes Wissen – Wittgenstein und Hegel, in: Contributions of the 37th International Wittgenstein Symposium, vol. XXII, Sonja Rinofner-Kreidl, Harald A. Wiltsche (eds.) \[Kirchberg a. W. 2014: 24 f.\] – https://www.alws.at/alws/wp-content/uploads/2018/06/papers-2014.pdf

## Translations

- Christoph Demmerling, Hegel, the Pragmatic Turn, and the Later Wittgenstein, in: Wittgenstein and Classical German Philosophy, Alexander Berg & Denys Kaidalov (eds.) \[De Gruyter, Oct. 2025\]

- Thomas Rentsch, Three Key Hypotheses regarding Hegel and Wittgenstein, in: Wittgenstein and Hegel – Reevaluation of Difference, Jakub Mácha & Alexander Berg (eds.) \[De Gruyter 2019\] – https://doi.org/10.1515/9783110572780-006

## Online edition

Proofreading of the normalized transcription of Wittgenstein’s Nachlass, coded in XML, for: Wittgenstein, Ludwig: Interactive Dynamic Presentation (IDP) of Ludwig Wittgenstein’s philosophical Nachlass \[wittgensteinonline.no\], Wittgenstein Archives at the University of Bergen (WAB) under the direction of Alois Pichler, 2016–. Manuscripts:

- Ms-115: XI, Philosophische Bemerkungen

- Ms-139b \[so-called Lecture on Ethics\] (ÖNB, Cod.Ser.n.37.936)

- Ms-148 \[C4\], Ms-149 \[C5\], Ms-150 \[C6\], Ms-152 \[C8\]

- Ms-153a: Anmerkungen; Ms-153b; Ms-154; Ms-155; Ms-156a

- Ts-213 \[so-called Big Typescript\]

## Conferences and workshops organized

- Wittgenstein and Hegel on Normativity and Rationality, 9–11 Sept. 2024, University of Zagreb \[with Denys Kaidalov, Karlo Gardavski and Bruna Picas\] – http://wittgensteinhegel2017.weebly.com/zagreb-2024.html

- Reading Philosophy – On the Literary Forms of Philosophy, 12 April 2024, University of Zurich \[with Frauke Berndt\] – https://www.ds.uzh.ch/apps/\_files/uploads/agenda/1483.pdf

- Wittgenstein and Hegel on the Foundations of Logic, 11–13 Sept. 2023, University of Vienna \[with Denys Kaidalov, Daniel Kuran, Bruna Picas\] – http://wittgensteinhegel2017.weebly.com/vienna-2023.html

- Wittgenstein and Classical German Philosophy: Self-consciousness and Self-reference, 21–23 Sept. 2022, University of Barcelona \[with Denys Kaidalov, Jakub Mácha, Bruna Picas, Ricard Sapena, Thomas Spiegel\] – http://wittgensteinhegel2017.weebly.com/self-consciousness-and-self-reference.html

- Wittgenstein and Classical German Philosophy, 1–3 Sept. 2021, University of Warsaw \[with Denys Kaidalov\] – http://wittgensteinhegel2017.weebly.com/wittgenstein-and-classical-german-philosophy.html

- Hegel and Wittgenstein – Negativity and Language, 11–13 June 2019, Charles University Prague \[with Vojtěch Kolman\] – http://wittgensteinhegel2017.weebly.com/negativity-and-language.html

- Wittgenstein und Hegel – Neubewertung einer Differenz, 28–30 June 2017, TU Dresden \[with Jakub Mácha, Louisa Herzfeld, Alexander Romahn and Marco Kleber\] – http://wittgensteinhegel2017.weebly.com/

- Georg Friedrich Wilhelm Hegel: Rationalität und christlicher Glaube, 18 Nov. 2016, Kathedralforum Dresden \[with Arbeitsgemeinschaft Religionsphilosophie Dresden e. V.\]

- The Night of Philosophy in Prague – Images, Sciences and Politics, 16–17 June 2016, Charles University Prague \[with Ondřej Švec, Benjamin Kaiser and the Institut français de Prague\] – https://philonight.hypotheses.org/

## Conference Series „Wittgenstein & Hegel“ 2017–2024

Quelle: die bisherige Tagungsseite wittgensteinhegel2017.weebly.com, Stand 22. Oktober 2026. Die Einleitung bitte knapp auf Englisch nach folgenden Punkten formulieren:

- Ausgangspunkt ist Wittgensteins Bemerkung zu Drury (in: Rush Rhees, ed., Recollections of Wittgenstein): “Hegel seems to me to be always wanting to say that things which look different are really the same. Whereas my interest is in showing that things which look the same are really different.”

- Diese Differenz ist selten eigens untersucht worden, obwohl sie heute besonders aufschlussreich ist; die Spaltung in analytische und kontinentale Philosophie gilt als überholt, Überschneidungen zeigen sich etwa in Philosophie des Geistes, Logik und Wissenschaftsphilosophie. Ziel: dass Hegel-Studien das Verständnis Wittgensteins vertiefen und umgekehrt.

- Themenfelder: Wittgensteinsche Motive bei Hegel; Hegelsche Motive bei Wittgenstein; Wittgensteins Hegel-Rezeption; die Rolle von Neuhegelianismus und britischem Idealismus für die Entstehung der analytischen Philosophie; die Differenz der Ansätze im Blick auf die analytisch-kontinentale Spaltung.

- Sechs Tagungen 2017–2024 (Dresden, Prag, Warschau, Barcelona, Wien, Zagreb), daraus drei Sammelbände (De Gruyter 2019, De Gruyter 2025, Synthesis Philosophica 2026).

### Tagungs-PDFs (vor dem Start herunterladen und unter files/conferences/ hochladen)

- Zagreb 2024 – Programm und Abstracts: https://wittgensteinhegel2017.weebly.com/uploads/1/0/1/4/101459898/programme.abstracts_wh_zagreb_2024.pdf

- Zagreb 2024 – Poster: https://wittgensteinhegel2017.weebly.com/uploads/1/0/1/4/101459898/poster_wh_zagreb_2024.pdf

- Wien 2023 – Programm: https://wittgensteinhegel2017.weebly.com/uploads/1/0/1/4/101459898/2023_08_program_for_vienna_8.pdf

- Wien 2023 – Abstracts: https://wittgensteinhegel2017.weebly.com/uploads/1/0/1/4/101459898/2023_08\_\_abstracts_vienna_4.pdf

- Barcelona 2022 – Programm und Abstracts: https://wittgensteinhegel2017.weebly.com/uploads/1/0/1/4/101459898/2022_09_abstracts_wittgenstein_and_classical_german_philosophy.pdf

- Barcelona 2022 – Poster: https://wittgensteinhegel2017.weebly.com/uploads/1/0/1/4/101459898/conference_wittgenstein_and_the_german_philosophical_tradition_self-consciousness_and_self-reference-def.pdf

- Band 2019 – Inhaltsverzeichnis: https://wittgensteinhegel2017.weebly.com/uploads/1/0/1/4/101459898/toc.pdf

- Band 2019 – Einleitung (nur nach Prüfung der Rechte, s. Teil C): https://wittgensteinhegel2017.weebly.com/uploads/1/0/1/4/101459898/intro.pdf

### Zagreb 2024 – Wittgenstein and Hegel on Normativity and Rationality

- 9–11 Sept. 2024, University of Zagreb. Organizers: Alexander Berg (Konstanz), Karlo Gardavski (Zagreb), Denys Kaidalov (Charles University Prague), Bruna Picas (Barcelona).

- Keynotes: Hans-Johann Glock (Zurich), Elena Ficara (Paderborn).

- Supported by the Croatian Philosophical Society, the Department of Philosophy of the University of Zagreb and the Faculty of Philosophy of the University of Sarajevo.

- Talks: aus dem Programm-PDF. Resulting volume: Synthesis Philosophica 41/1 (2026, forthcoming).

### Vienna 2023 – Wittgenstein and Hegel on the Foundations of Logic

- 11–13 Sept. 2023, University of Vienna. Organizers: Alexander Berg (Zurich), Denys Kaidalov (Prague), Daniel Kuran (Vienna), Bruna Picas (Barcelona). Partners: Vojtěch Kolman (Prague), Michał Dobrzański (Warsaw), Kurt Appel (Vienna).

- Funded by CENTRAL Workshops (CENTRAL network).

- Keynotes und Talks: aus Programm- und Abstract-PDF.

### Barcelona 2022 – Wittgenstein and Classical German Philosophy: Self-consciousness and Self-reference

- 21–23 Sept. 2022, University of Barcelona, Faculty of Philosophy. Organizers: Alexander Berg (Zurich), Denys Kaidalov (Prague), Jakub Mácha (Brno), Bruna Picas, Ricard Sapena, Adrià Montalbán Figueroa (Barcelona), Thomas Spiegel (Potsdam).

- Keynotes: Román Cuartango (Barcelona), Hans-Johann Glock (Zurich), Luca Illetterati (Padua), Edgar Maraguat (Valencia), Sebastian Rödl (Leipzig).

- Supported by the Spanish research council (project PGC2018-093363-B-I00), Hegel en perspectiva (Valencia), Forschungskolleg Analytic German Idealism (Leipzig), German Philosophy Lab (Warsaw).

- Talks: aus dem Programm-PDF.

### Warsaw 2021 – Wittgenstein and Classical German Philosophy

1–3 Sept. 2021, University of Warsaw. Organizers: Alexander Berg (Zurich), Denys Kaidalov (Warsaw). Led by Pirmin Stekeler-Weithofer (Leipzig), Hans-Johann Glock (Zurich), Richard Raatzsch (Oestrich-Winkel), Jakub Mácha (Brno). Resulting volume: Wittgenstein and Classical German Philosophy (De Gruyter 2025). Talks:

- Denys Kaidalov (Warsaw): The Two Faces of Contradiction

- Pirmin Stekeler-Weithofer (Leipzig): Hegelian Semantics. From Wittgenstein’s Pure Konstatierungen to Dialectically Comprehended Utterances

- Christina Weiss (Darmstadt): Hegel’s Shine and Wittgenstein’s Function

- Guillaume Decauwert (Grenoble): Philosophical Clarity, Negation and Ineffability. A Dialogue between Wittgenstein and Schopenhauer

- Hans-Johann Glock (Zurich): The Whole Truth about Truth: Kant and Wittgenstein vs. Hegel

- Bruna Picas (Barcelona): Hegel and Wittgenstein on Philosophical Concepts, between Determination and Blurriness

- Karl-Friedrich Kiesow (Hannover): Wittgenstein, Longfellow – and Goethe

- Jakub Mácha (Brno): Hegel and Wittgenstein on God at the Beginning of the World

- Alexander Berg (Zurich): Wittgenstein’s Synoptic View and Hegel’s Speculative Philosophy

- Josefina Anna Formanová (Prague): The Failure of Philosophy. Language and Cognition between Hegel and Wittgenstein

- Elena Romano (Padua): Paradoxical Normativity. Wittgenstein and Kant on Following a Rule

- Richard Raatzsch (Oestrich-Winkel): Sameness and Difference

- Aloisia Moser (Linz): Acts of Thinking in Kant and Wittgenstein

- Silvia Locatelli (Padua): Following a Rule Blindly – Hegel and Wittgenstein on the Immediacy of Habit

- Thomas Spiegel (Potsdam): Rule-Following and Objective Spirit. Wittgenstein and Classical German Philosophy

- Herbert Hrachovec (Vienna): Exceptional Cases. Wittgensteinian Remarks on post-Kantian Emergency Law

- Valentina Balestracci (Pisa): Wittgenstein and Kant’s Influence through Hertz: the Boundaries of Language

- Jordi Fairhurst (Balearic Islands): Ethics is Transcendental (TLP 6.421)

- David Palme (Erfurt/Graz): Between Theory and Practice: Was Wittgenstein a Partial Idealist?

- Jan Podacker (Duisburg-Essen): Rules as the Pragmatic Core of Concepts in Kant and Wittgenstein

- Maya Halperin (Tel Aviv): “A man’s style is a picture of him”: Wittgenstein and Hamann

- Andrei-Valentin Bacrau: Naturalism and Noncognitivism in Wittgenstein and Nietzsche

- Eric Sancho Adamson (Barcelona): Wittgenstein, Mendelssohn, Kant, Dedekind and Wittgenstein. On How it is Possible to Learn Mathematics

### Prague 2019 – Hegel and Wittgenstein: Negativity and Language

11–13 June 2019, Charles University Prague (Campus Hybernská). Organizers: Alexander Berg, Vojtěch Kolman. Led by Kenneth R. Westphal (Istanbul) and Pirmin Stekeler-Weithofer (Leipzig). Funded by the European Regional Development Fund, project “Creativity and Adaptability as Conditions of the Success of Europe in an Interrelated World” (CZ.02.1.01/0.0/0.0/16_019/0000734). Talks:

- Jakub Mácha: Introduction to the volume Wittgenstein and Hegel – Reevaluation of Difference

- Pirmin Stekeler-Weithofer: Teaching Differences vs. Negation of Negation. Wittgenstein and Hegel on Two Aspects of Meaning

- Simon Skempton: Saying the Showing of the Absolute

- Josefina Anna Formanová: When History Remains Silent: Collective Trauma as Dialectical Negativity of Social Rituals

- Guido Tana: Rules, Recognition and Community: a Hegelian Proposal for a Wittgensteinian Paradox

- Andrej S. Peter: Relativism and Negativism – Talking about Following a Rule as a Reflexionsbestimmung

- Kenneth R. Westphal: Kant, Hegel & the Historicity of Pure Reason

- Denys Kaidalov: Hegel on Private Language

- Saori Makino: Our Way of Deciding the Use of a Word: Wittgenstein, Hegel, and Philosophical Method

- Vojtěch Kolman: Talking is Lying: On One Suspicious Metaphor

- Marco Kleber: Rethinking Logical Form: Wittgenstein, Hegel, and the Problem of Logical Antinomy

- David Palme: Critique with Wittgenstein. From the sub specie aeterni to the Entanglement in our Rules

- Alexander Berg: Hegel and Wittgenstein – Idea and Text

- James Fielding: The Spectre of Conservatism: The Ambiguous Political Legacy of Wittgenstein and Hegel

- Bruna Picas: Blurring the Differences between Hegel and Wittgenstein: a Response to Robert Brandom

- Martin Palauneck: Sophistic Education, Rhetoric and Negative Force

- Gabriele Tomasi: Wittgenstein and Hegel on the Artistic Gaze

- Kathrin Menden: Aspect Seeing and the Hegelian Notion – Examining the Rabbit-Duck Illusion through Hegel’s Science of Logic

- Christina Weiss: Schematizing Saying and Showing

### Dresden 2017 – Wittgenstein und Hegel: Neubewertung einer Differenz / Reevaluation of Difference

28–30 June 2017, TU Dresden. Organizers: Alexander Berg (Dresden & Prague), Jakub Mácha (Brno), Louisa Frintert/Herzfeld (Dresden), Marco Kleber (Dresden), Alexander Romahn (Leipzig). Keynotes: Thomas Rentsch (Dresden), Pirmin Stekeler-Weithofer (Leipzig), Hans-Johann Glock (Zurich). Funded by the Graduate Academy of TU Dresden (Excellence Initiative). Resulting volume: Wittgenstein and Hegel – Reevaluation of Difference (De Gruyter 2019). Talks with recordings:

- Thomas Rentsch (Dresden): Hegel und Wittgenstein, drei systematische Thesen

- Pirmin Stekeler-Weithofer (Leipzig): Das metaphysische Weltbild der Analytischen Philosophie. Kritik atomarer Monaden und Pixel bei Hegel und dem späteren Wittgenstein – https://youtu.be/FPDV7McgmsE

- Bruno Haas (Dresden): Vom Unsinn und seinen Produkten – https://youtu.be/0Yw5yCqvh5Y

- Herbert Hrachovec (Vienna): Maßstab und Regel. Ein Berührungspunkt zwischen Hegel und Wittgenstein

- Aloisia Moser (Linz): Hegel’s Speculative Method and Wittgenstein’s Projection Method – https://youtu.be/uZ5AGkv1n38

- Ingolf Max (Leipzig): Hegel and Wittgenstein on Contradiction – https://youtu.be/661MvlaCH_o

- Karl-Friedrich Kiesow (Hannover): Perspectivism in Hegel and Wittgenstein – https://youtu.be/qyHsblP-VVY

- Rico Gutschmidt (Chicago): Unabschließbarkeit und unglückliches Bewusstsein. Transformationen bei Wittgenstein und Hegel – https://youtu.be/bt7aHQRiTuE

- David Kolb (Bates College): The Diamond Net: Metaphysics, Grammar, Ontologies – https://youtu.be/TB28v5NNoy4

- Hans-Johann Glock (Zurich): Suggesting Differences: Wittgenstein’s ‘Undogmatic Procedure’ vs. Hegel’s Dialectic – https://youtu.be/xrhnvfFolfo

- Gaetano Chiurazzi (Turin): Hegel’s Discussion of Kant’s Second Antinomy and its Anti-analytical Implications – https://youtu.be/bUkzAM1Oo8Y

- Ermylos Plevrakis (Heidelberg): „Die Eine logische Konstante“: Ein Vergleich zwischen Wittgensteins Logisch-philosophischer Abhandlung und Hegels Wissenschaft der Logik – https://youtu.be/DBCfI1JkBI4

- Guillaume Lejeune (Leipzig/Liège): Internal Relations: Wittgenstein’s Tractatus from the Point of View of Bradley’s Philosophy – https://youtu.be/-lDEWZHA2qY

- Vojtěch Kolman (Prague): Master, Slave and Wittgenstein: the Dialectic of Rule-following – https://youtu.be/UNx2Zl5D2Hs

- Josefina Anna Formanová (Prague): Social Structure of Cognition in the Philosophy of Hegel and Wittgenstein – https://youtu.be/UmL9Vdpat1E

- Valentin Pluder (Siegen): Regelbefolgung und institutioneller Kontext – https://youtu.be/aMNhTlHt8jE

- Valentina Balestracci (Pisa): Hegel and Wittgenstein: Examples of a Comparison – https://youtu.be/rRDQ6kCvags

- Oriane Petteni (Liège): Differences between Hegel’s and Wittgenstein’s Philosophical Approaches as they Relate to the Analytic-Continental Split – https://youtu.be/YjFDdfAWjVY

- Lorenzo Cammi (Leipzig/Verona): Hegel and Wittgenstein on the Notion of Wirklichkeit – https://youtu.be/7_HtYyrJi1s

- Elena Ficara (Paderborn): Truth and Incompatibility – https://youtu.be/x0xAxEkJrng

- Davide Dalla Rosa (Padua): Gestalten des Geistes as Lebensformen. On Terry Pinkard’s Notion of ‘Form of Life’ between Hegel and Wittgenstein – https://youtu.be/Pq5Rmha8F0c

- Jonathan Shaheen (Uppsala): Hegel and Wittgenstein on Recognition and Social Constitution

- Marco Kleber (Dresden): Das Unsagbare als Widerspruch zwischen Hegel und Wittgenstein – https://youtu.be/LqhhuhsQBUs

- Alexander Romahn (Leipzig): Die Unterschätzung von Hegels Philosophie durch die analytische Tradition – Eine mögliche Erklärung im Hinblick auf McTaggart und Russell – https://youtu.be/vPZjAQpoRV4

- Louisa Frintert/Herzfeld (Dresden): Der Widerspruch als Einführung in die Sprache – Hegels Logik des Seins im Dialog mit Wittgenstein – https://youtu.be/03F9zArrHD4

- Alexander Berg (Dresden/Prague): Wittgensteins Hegel – vom Wortspiel zum Sprachspiel – https://youtu.be/GqSvvLgsv20

- Jakub Mácha (Brno): Individuality, Particularity and Universality in Hegel and Wittgenstein – https://youtu.be/cj0Lh9ZYMdE

### Volumes from the series

- Wittgenstein and Hegel – Reevaluation of Difference, Jakub Mácha & Alexander Berg (eds.), De Gruyter 2019 – https://doi.org/10.1515/9783110572780

- Wittgenstein and Classical German Philosophy – Logic, Language, Life, Alexander Berg & Denys Kaidalov (eds.), De Gruyter 2025 – https://www.degruyter.com/document/isbn/9783110698442/html

- Wittgenstein and Hegel on Normativity and Rationality, Alexander Berg & Kenan Šljivo (eds.), Synthesis Philosophica 41/1, 2026 (forthcoming)

## Talks

- Goethe’s Artistic Influence on the Phenomenology of Spirit \[XXXVI International Hegel Congress, Rome III – Sept. 2026\]

- Book presentation: Wittgenstein and Hegel on Normativity and Rationality, special issue of Synthesis Philosophica \[XXXVI International Hegel Congress, Rome – Sept. 2026\]

- Wittgenstein Introduces Frege to Soviet Russia: Possibility, Probability, and the Curious Case of the Yellow Book \[SSHAP Congress, University of Jena – July 2025\]

- On the Literary Form of the Phenomenology of Spirit – Method and Meaning \[University of Turin – May 2025\]

- Die Bedeutung der literarischen Form des Herr-Knecht-Kapitels als Schlüssel für Anerkennung und Freiheit \[XXXV International Hegel Congress, University of Tbilisi – Oct. 2024\]

- Introduction to Wittgenstein and Classical German Philosophy – Book Presentation \[University of Zagreb – Sept. 2024 / Charles University Prague – Dec. 2024 / University of Bergen – Sept. 2025\]

- Traduttore, Traditore: On the Translations of the Works of Ludwig Wittgenstein \[round table with René J. Campis, Jesús Padilla Gálvez, Luca Oliva, Eduardo Bermúdez Barrera; XXV World Congress of Philosophy, Rome – Aug. 2024\] – https://wcprome2024.com/round-tables/

- Methods for a Literary History of Philosophy \[XXV World Congress of Philosophy, Rome – Aug. 2024 / XXVI German Congress of Philosophy, Münster – Sept. 2024\]

- Methoden für eine Literaturgeschichte der Philosophie \[University of Zurich – April 2024\] – https://www.ds.uzh.ch/apps/\_files/uploads/agenda/1483.pdf

- Grundzüge einer Literaturgeschichte der Philosophie \[University of Konstanz – Dec. 2023\]

- Ludwig Wittgenstein and the Photography of Everyday Life \[8th Annual Conference of the Kulturwissenschaftliche Gesellschaft, Saarland University – Sept. 2023\] – https://kwg-ev.org/populaere-kulturen-2023/

- The Method of Absolute Negativity as a Foundation of Logic in Wittgenstein and Hegel \[University of Vienna – Sept. 2023\] – http://wittgensteinhegel2017.weebly.com/vienna-2023.html

- The Method of Absolute Negativity and the Tractatus Logico-Philosophicus – Wittgenstein, William James and Hegel \[Wittgenstein Symposium, Kirchberg – Aug. 2023\]

- ‘Saying and Showing’ as Literary Form and Philosophical Content of the Tractatus \[eikones Forum, University of Basel – Oct. 2022\]

- Three Types of the Self in Wittgenstein and Hegel \[University of Barcelona – Sept. 2022\]

- The Art of Philosophy – On the Significance of Literary Form in Hegel’s Phenomenology of Spirit \[34th International Hegel Congress, Zadar – Sept. 2022\]

- Wittgensteins Übersichtliche Darstellung und Hegels Spekulative Philosophie \[Wittgenstein Symposium, Kirchberg – Aug. 2022\]

- On Intertextuality in Hegel’s Phenomenology of Spirit \[Charles University Prague – June 2022\]

- Book presentation: Wittgensteins Hegel \[University of Bergen / University of Helsinki – June 2022\]

- Der Blick des Philosophen – Wittgenstein und die Photographie als Kulturtechnik in den 1920er und 30er Jahren \[Workshop Die Zeit der Unkultur. Ludwig Wittgenstein im Österreich der Zwischenkriegszeit, University of Vienna – Oct. 2021\]

- Eine philosophische Literaturgeschichte als Brücke zwischen Idee und Text – Konstellation, Intertextualität, Literarizität \[XXV Congress of the German Society for Philosophy, section Metaphilosophy & Methodology – Sept. 2021\]

- Wittgenstein’s Synoptic View and Hegel’s Speculative Philosophy \[University of Warsaw – Sept. 2021 / University of Zagreb – Dec. 2021 / University of Venice – Sept. 2022\]

- Live Talk, Burgtheater Vienna: On the traces of Ludwig Wittgenstein, on the occasion of the premiere of ALLES, WAS DER FALL IST, with ensemble member Philipp Hauß (as Ludwig Wittgenstein) and dramaturge Andreas Karlaganis; moderated by Anne Aschenbrenner \[June 2021\]

- Hegels Phänomenologie des Geistes in einer Literaturgeschichte der Philosophie \[33rd International Hegel Congress, Warsaw, panel Contexts and Discussions: Classical German Philosophy – June 2021\]

- Identity in Difference – Wittgenstein’s Hegel \[Workshop Ludwig Wittgenstein and German Philosophy, University of Zurich – Nov. 2020\]

- Philosophy in Captivity – Respondent to Alfred Nordmann \[Wittgenstein’s Philosophy in Times of Crisis, online – June 2020\] – Video: https://youtu.be/hv0JRR4U7kA

- Wittgenstein’s ‘Übersichtliche Darstellung’ and Hegel’s System \[Tokyo Metropolitan University – April 2020, postponed\]

- Identity in Difference – Wittgenstein’s Hegel \[Kyoto University – April 2020, postponed\]

- The Role of Leo Tolstoy for Wittgenstein’s Tractatus \[Jagiellonian University Kraków – Nov. 2019\]

- Hegel and Wittgenstein – Idea and Text \[Charles University Prague – June 2019\]

- Ernste Spiele – Wittgenstein und Schiller \[Victoria University of Wellington – Nov. 2018\]

- The Influence of William James’ Varieties of Religious Experience on Wittgenstein’s Pictorial Thinking \[SoPheRE Congress, Prague – Nov. 2018\]

- Psyche, Seele, Geist – Wittgenstein und Hegel \[5th Wittgenstein Forum of the International Ludwig Wittgenstein Society – Oct. 2018\]

- Wittgenstein, die Grundlagen der Mathematik, und Hegel \[Wittgenstein Symposium, Kirchberg – Aug. 2018\]

- Wittgenstein and Photography – The Early Picture Theory and the Late Photo Album \[Masaryk University Brno – Nov. 2017\]

- Hegel’s “Good Nose” – the Law of Contradiction in Wittgenstein and Hegel \[DGPhil Congress, Berlin – Sept. 2017\]

- Vom Wissen zum Denken – Wittgensteins dialektische Methode am Beispiel der Seminarnotizen G. E. Moores \[Wittgenstein Symposium, Kirchberg – Aug. 2017\]

- Wittgensteins Hegel – vom Wortspiel zum Sprachspiel \[Conference Wittgenstein and Hegel, TU Dresden – June 2017\] – Video: https://youtu.be/GqSvvLgsv20

- Wittgenstein und Fotografie – von Bildtheorie bis Fotoalbum \[Charles University Prague – April 2017\]

- Serious Games – Wittgenstein and Schiller \[Masaryk University Brno – Nov. 2016\]

- Vom „pun“ zum Sprachspiel – Wittgenstein, Russell, Bradley, Hegel und der Streit um das concrete universal \[Charles University Prague – May 2016 / Wittgenstein Symposium, Kirchberg – Aug. 2016\]

- Traces of Speculative Philosophy in Wittgenstein’s Thinking \[University of Chicago – Feb. 2016 / University of Peradeniya – March 2016\]

- Spuren der spekulativen Philosophie in Wittgensteins Denken \[TU Dresden – Oct. 2015 / University of Leipzig – Feb. 2016\]

- Probleme in der historischen Wittgenstein-Forschung – Wunsch, Wirklichkeit und Russische Philosophie \[Wittgenstein Symposium, Kirchberg – Aug. 2015 / Charles University Prague – Oct. 2015\]

- What Wittgenstein Thought of Hegel’s Philosophy \[University of Bergen – May 2015\]

- Farben – Flüssige Zeit \[Laudatio for Weg ins Grüne – Lucia Fischer, painting & drawing, Berlin – Oct. 2014\]

- Absolutes Wissen und Grundlose Gewissheit – Hegel und Wittgenstein \[Charles University Prague – April 2014 / TU Berlin – May 2014\]

- Heideggers System \[5th Meßkirch Heidegger Conference Freiheit und Geschick, Meßkirch – May 2014\]

- Hegels Transzendenz \[I Congreso Germano-Latinoamericano sobre la Filosofía de Hegel, Buenos Aires – May 2014\]

- Absolutes Wissen und grundlose Gewissheit \[Werkstatt Philosophie, TU Dresden – Dec. 2013\]

- Philosophie des Nichts \[Werkstatt Philosophie, TU Dresden – June 2012\]

- Philosophie des Nichts \[Symposium nichts-in-Pieschen, Dresden – June 2012\]

- Implikationen zu einer Theorie der Säkularisation bei Charles Taylor \[Werkstatt Philosophie, TU Dresden – April 2010\]

## About

- Research Fellow of the Alexander von Humboldt Foundation with a research project On the Literary Form of Philosophy.

- Research stays at the University of Zurich, the University of Konstanz, the Wittgenstein Archives at the University of Bergen, the Wren Library of Trinity College Cambridge, the University of Chicago and Charles University Prague.

- Studies of philosophy, art history and psychology at TU Dresden, the Sorbonne (Paris) and the University of Florence.

- Languages – fluent: German, English, Italian, French; basic: Latin, Czech, Norwegian, Russian.

### Memberships

- Arbeitsgemeinschaft Religionsphilosophie Dresden e. V.

- Austrian Ludwig Wittgenstein Society (ALWS)

- British Wittgenstein Society (BWS)

- Deutsche Gesellschaft für Philosophie

- German Humboldt Network e. V.

- Internationale Hegel-Gesellschaft

- Internationale Ludwig Wittgenstein Gesellschaft (ILWG)

- Italien-Zentrum der Technischen Universität Dresden

- Society for the Study of the History of Analytical Philosophy (SSHAP)

- The Central-European Institute of Philosophy (Charles University, Prague)

- Young Network for Wittgensteinian Philosophy
