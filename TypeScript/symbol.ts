var sym:symbol = Symbol("abc")
var sym2:symbol = Symbol("abc")
//console.log(sym === sym2)

let object = {
    [sym]: "Wert",
    [sym2]: "Wert2"
}
console.log(object[sym])
object[sym] = function (){
    return 'Whatever'
}
console.log(object[sym]())