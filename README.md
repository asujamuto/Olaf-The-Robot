# Olaf The Robot 
### Budka, która może uratować życie i nie tylko


Olaf to oprogramowanie, które w przyszłości mogło by pojawić się w budce. 
Założenia projektu to:
- Zmniejszenie Bezdomności
- Rozmowa z mieszkańcami, w tym wsparcie samotnych lub smutnych
- System szybkiego zgłaszania problemów


Olaf to chatbot, który ma na celu zgłaszać problemy potrzebujących. Kiedy ktoś poprosi go o pomoc, podczas rozmowy z nim lub bezpośrednio przez maila, wysyłana jest wiadomość wpierw do administratora, administrator wysyła ją z kolei do kolejnych organów, które mogłyby udzielić profesjonalnej pomocy. Cały proces w przyszłości chciałbym zautomatyzować.

### Jak zainstalować Olafa?

Wchodząc w terminal możemy go pobrać z Git Huba
> komenda na stworzenie folderu
> komenda na pobranie z git-huba

Z terminala wchodzimy do folderu "chatbot"

Windows:
>cd .\chatbot\

Linux:
>cd ./chatbot/


Zbudujmy naszą aplikację:
> docker built -t olaf-chatbot .

Otwieramy aplikację:
> docker run -it --net=host olaf-chatbot

W wyszukiwarce wpisujemy: htttp://localhost:8000

To był ostatni krok. 

### Rzeczy, które można usprawnić:
- system rozmowy - Olaf niestety nie ma jeszcze wielu danych, ani nie był testowany na większej grupie ludzi. Bot zbiera dane z konwersacji, aby w przyszłości na ich podstawie, uczył się nieprzewidywalnie kreatywnych ludzkich sentencji

- reprezentacja ciekawych miejsc miasta - podczas rozmowy, olaf zapytany o ciekawe miejsca w mieście będzie wyszukiwał z internetu i wypisywał takie miejsca. Ma to na celu zachęcić turystów i mieszkańców do zapoznania się z miastem.

- automatyzacja procesu zgłaszania, znalezienie organizacji chętnych do współpracy



