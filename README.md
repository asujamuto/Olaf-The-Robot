# Olaf The Robot 
### Budka, która może uratować życie i nie tylko

![1](https://user-images.githubusercontent.com/67243090/196067579-960d1197-0994-4b64-ab6e-1114f5fc074e.png)


Olaf to oprogramowanie, które w przyszłości mogło by pojawić się w budce. 
Założenia projektu to:
- Zmniejszenie Bezdomności
- Rozmowa z mieszkańcami, w tym wsparcie samotnych lub smutnych
- System szybkiego zgłaszania problemów


Olaf to chatbot, który ma na celu zgłaszać problemy potrzebujących. Kiedy ktoś poprosi go o pomoc, podczas rozmowy z nim lub bezpośrednio przez maila, wysyłana jest wiadomość wpierw do administratora, administrator wysyła ją z kolei do kolejnych organów, które mogłyby udzielić profesjonalnej pomocy. Cały proces w przyszłości chciałbym zautomatyzować.

### Jak zainstalować Olafa?

Wchodzimy w terminal
Tworzymy folder:

> mkdir Olaf-The-Robot

Wchodzimy do folderu:

Windows:
> cd Olaf-The-Robot

Linux:
> cd Olaf-The-Robot

Wchodząc w terminal możemy pobrać pliki z Git Huba
> git clone https://github.com/asujamuto/Olaf-The-Robot.git -b master

Włączamy docker deamona.

Windows:
*W tym kroku należy włączyć windowsowego docker deamona. Niestety, program głównie jest przystosowany pod system Linux*

Linux:
>sudo systemctl start docker 

Linux:
Zbudujmy naszą aplikację:
> docker build -t olaf-chatbot .

Otwieramy aplikację:
> docker run -it --net=host olaf-chatbot

W wyszukiwarce wpisujemy: htttp://localhost:8000

To był ostatni krok.



### Folder (w tym opis drzewa katalogu)

Program złożony jest z głównych członów:
- Folder z Django **chatbotbackend**
- Folder z aplikacją Django **chatbotbackend/main**
	- **/templates/home.html** - główna strona aplikacji, na której wyświetla się chatbot
	- **/templates/email_form.html** - strona z formularzem do maila
	- **/static/** - jest tutaj plik css i js używany do wyświetlanych stron


- Plik **databases/cleaned_database.json** - plik, z danymi z których uczy się maszyna
- Folder **databases/scripts/** - folder, ze skryptami do konwersji danych z databases/csv/Small_talk_Intent.csv na polskie databases/cleaned_database.json
- Plik **training.py** - plik, w którym maszyna "uczy się"
- Folder **chatbot_model.model** - folder z zapisaną maszyną z training.py
- Plik **chatbotbackend/chatbot.py** - plik, w którym odbywa się chat


### Rzeczy, które można usprawnić:
- system rozmowy - Olaf niestety nie ma jeszcze wielu danych, ani nie był testowany na większej grupie ludzi. Bot zbiera dane z konwersacji, aby w przyszłości na ich podstawie, uczył się nieprzewidywalnie kreatywnych ludzkich sentencji

- reprezentacja ciekawych miejsc miasta - podczas rozmowy, olaf zapytany o ciekawe miejsca w mieście będzie wyszukiwał z internetu i wypisywał takie miejsca. Ma to na celu zachęcić turystów i mieszkańców do zapoznania się z miastem.

- automatyzacja procesu zgłaszania, znalezienie organizacji chętnych do współpracy



