/* Part 2 */
console.log('PART 2')
for (tall=1; tall<21;tall++){
    console.log(tall)
}
/* Part 3 */
console.log('PART 3')

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for (i= 0;i <(numbers.length); i++){      /*Her har jeg brukt listenavn.lenght så selv om listen blir større så vil det ikke endre noe */
    if ((numbers[i]%3===0)&&(numbers[i]%5==0)){
        console.log("eplekake")
    }                                     /*Her blir % brukt for å skjekke om tallene er delige på 3 eller 5. && blir brukt som "and" i python */
    else if((numbers[i]%3===0)){
        console.log("eple")
    }
    else if((numbers[i]%5===0)){
        console.log("kake")
    }
    else{
        console.log(numbers[i])
    }
    
}
/* Part 4 */
var tittel=document.getElementById("title");
tittel.innerText="Hello JavaScript!"   /*her henter jeg IDen fra HTML filen (title) og bruker innertext for å endre headeren*/
/* Part 5 */
var viser_påSkjerm=document.getElementById("magic")
var synlig=document.getElementById("magic")
function changeDisplay() {
    viser_påSkjerm.style.display="none";
}

function changeVisibility() {
    synlig.style.visibility="hidden";
    viser_påSkjerm.style.display="block";
}

function reset() {
    synlig.style.visibility="visible";
    viser_påSkjerm.style.display="block";
}
/*Funksjonene ovenfor har blitt koblet sammen med de ulike knappene som er lagd i HTMLen*/
/* Part 6 */
const technologies = [
    'HTML5',
    'CSS3',
    'JavaScript',
    'Python',
    'Java',
    'AJAX',
    'JSON',
    'React',
    'Angular',
    'Bootstrap',
    'Node.js'
];
for(i=0;i<technologies.length;i++){
    var liste=document.createElement("LI");
    var addTekst=document.createTextNode(technologies[i]);
    liste.appendChild(addTekst);
    document.getElementById("tech").appendChild(liste);
}