let next = document.querySelector('.next')
let prev = document.querySelector('.prev')
let items = document.querySelectorAll('.item')
let slideContainer = document.querySelector('.slide')
let intervalId = null
let currentIndex = 0

let time = 1500;


document.querySelector("#searchbutton").addEventListener('click', ()=>{
  console.log("hello");
  document.querySelector(".s01").classList.add('hiddenleft');

  for (let i=0; i<items.length; i++){
    if (i==currentIndex+1) continue;
    items[i].classList.add('hiddenleft');
  }

  console.log(document.querySelector("#search001").value);
  console.log(document.querySelector("#search002").value);
  // document.querySelectorAll(".item").forEach(elem =>{
  //   elem.classList.add("hiddenleft")
  // })

})

function nextSlide() {

  if ( document.querySelector(".s01").classList.contains("hiddenleft")){

    return;
  }

  let currentItem = items[currentIndex]
  slideContainer.appendChild(currentItem)
  currentIndex = (currentIndex + 1) % items.length
}

function prevSlide() {
  let currentItem = items[currentIndex]
  slideContainer.prepend(currentItem)
  currentIndex = (currentIndex - 1 + items.length) % items.length
}

// Set the initial interval
intervalId = setInterval(nextSlide, time) // 3000ms = 3 seconds

// Optional: add event listeners for button clicks
next.addEventListener('click', function() {
  clearInterval(intervalId)
  nextSlide()
  intervalId = setInterval(nextSlide, time)
})

prev.addEventListener('click', function() {
  clearInterval(intervalId)
  prevSlide()
  intervalId = setInterval(nextSlide, time)
})

