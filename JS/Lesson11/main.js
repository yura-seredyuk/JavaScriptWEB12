let big = document.querySelector('.big'),
    middle = document.querySelector('.middle'),
    small = document.querySelector('.small'),
    p = document.querySelector('p')
    table = document.querySelector('table')

// console.log(small.closest('div'))
// console.log(big.childNodes)
// console.log(big.hasChildNodes())
// console.log(big.nextSibling)
// console.log(big.nextElementSibling)
// console.log(big.parentElement)
// console.log(small.parentNode)

// console.log(middle.parentElement)
// console.log(middle.children)
// console.log(middle.firstChild)
// console.log(middle.firstElementChild)
// console.log(middle.lastChild)
// console.log(middle.lastElementChild)

// console.log(p.nextElementSibling)
// console.log(p.previousElementSibling)

console.log(table.rows)
console.log(table.caption)
console.log(table.tBodies)

console.log(table.rows[1].cells[0])
console.log(table.rows[1].rowIndex)
console.log(table.rows[1].cells[1].cellIndex)