// let next = document.querySelector('.next')
// let prev = document.querySelector('.prev')
// let items = document.querySelectorAll('.item')

// next.addEventListener('click', function(){
//     let firstItem = items[0]
//     firstItem.style.transform = 'translateX(100%)'
//     setTimeout(function(){
//         document.querySelector('.slide').appendChild(firstItem)
//         firstItem.style.transform = 'translateX(0)'
//     }, 500)
// })

// prev.addEventListener('click', function(){
//     let lastItem = items[items.length - 1]
//     lastItem.style.transform = 'translateX(-100%)'
//     setTimeout(function(){
//         document.querySelector('.slide').prepend(lastItem)
//         lastItem.style.transform = 'translateX(0)'
//     }, 500)
// })

//---------------------------------------------------//

// let next = document.querySelector('.next')
// let prev = document.querySelector('.prev')

// next.addEventListener('click', function(){
//     let items = document.querySelectorAll('.item')
//     document.querySelector('.slide').appendChild(items[0])
// })

// prev.addEventListener('click', function(){
//     let items = document.querySelectorAll('.item')
//     document.querySelector('.slide').prepend(items[items.length - 1]) // here the length of items = 6
// })

let next = document.querySelector('.next')
let prev = document.querySelector('.prev')
let items = document.querySelectorAll('.item')
let slideContainer = document.querySelector('.slide')
let intervalId = null
let currentIndex = 0

function nextSlide() {
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
intervalId = setInterval(nextSlide, 5000) // 3000ms = 3 seconds

// Optional: add event listeners for button clicks
next.addEventListener('click', function() {
  clearInterval(intervalId)
  nextSlide()
  intervalId = setInterval(nextSlide, 3000)
})

prev.addEventListener('click', function() {
  clearInterval(intervalId)
  prevSlide()
  intervalId = setInterval(nextSlide, 3000)
})