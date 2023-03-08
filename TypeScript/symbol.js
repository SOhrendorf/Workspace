var _a;
var sym = Symbol("abc");
var sym2 = Symbol("abc");
//console.log(sym === sym2)
var object = (_a = {},
    _a[sym] = "Wert",
    _a[sym2] = "Wert2",
    _a);
console.log(object[sym]);
object[sym] = function () {
    return 'Whatever';
};
console.log(object[sym]());
