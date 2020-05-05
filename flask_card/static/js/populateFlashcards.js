//variables
const card = document.querySelector("#card");
const front = document.querySelector(".front");
const back = document.querySelector(".back");
const next = document.querySelector("#next");
const prev = document.querySelector("#prev");
const count = document.querySelector("#count");
const flashcardData = $('#my-data').data();
const questions = [];

let current = 0;
let turned = false;

// Populate flashcard data on load
load().then(populateNextCard)

// Promise base load function
function load() {
    return new Promise((resolve, reject) => {
        window.onload = () => {
            console.log(flashcardData.collection)
            flashcardData.collection.forEach((item) => {
                data = {
                    question: item.question,
                    answer: item.answer,
                    inputType: item.input_type
                };
                questions.push(data);
            })
            resolve();
        }
    })
}

function resetCard() {
    prev.disabled = false;
    next.disabled = false;
    card.classList.remove("turned");
}

function populateNextCard() {
    resetCard();
    const md = window.markdownit();
    const questionMd = md.render(questions[current].question);
    const answerMd = md.render(questions[current].answer);

    front.innerHTML = `<div class="container is-fluid has-text-centered">${questionMd}</div>`;
    if (questions[current].inputType === 'markdown') {
        back.innerHTML = `<div class="container is-fluid">${answerMd}</div>`;
    } else {
        back.innerHTML = `<div class="container is-fluid has-text-centered">${answerMd}</div>`;
    }
    count.innerHTML = `<p>${[current + 1]} / ${questions.length}</p>`;
    current++;
}

function getNextCard() {
    if (current < questions.length) {
        populateNextCard();
    } else {
        next.disabled = true;
    }
}

function getPrevCard() {
    if (current > 1) {
        resetCard();
        const md = window.markdownit();
        const questionMd = md.render(questions[current - 2].question);
        const answerMd = md.render(questions[current - 2].answer);

        front.innerHTML = `<div class="container is-fluid has-text-centered">${questionMd}</div>`;
        if (questions[current - 2].inputType === 'markdown') {
            back.innerHTML = `<div class="container is-fluid">${answerMd}</div>`;
        } else {
            back.innerHTML = `<div class="container is-fluid has-text-centered">${answerMd}</div>`;
        }
        count.innerHTML = `<p>${[current - 1]} / ${questions.length}</p>`;
        current--;
    } else {
        prev.disabled = true;
    }
}

function toggleTurn(e) {
    turned = !turned;
    if (turned) {
        this.classList.add("turned");
    } else {
        this.classList.remove("turned");
    }
}

// Listening to events from carousel buttons
card.addEventListener("click", toggleTurn);
next.addEventListener("click", getNextCard);
prev.addEventListener("click", getPrevCard);