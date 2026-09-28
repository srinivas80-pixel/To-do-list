
let t=document.getElementById('username')
let b=document.getElementById('userid')
let g=document.getElementById('values')
function add(){
    f1=parseFloat(t.value)
   f2=parseFloat(b.value)
    console.log(f1+f2)
    g.value=f1+f2}
let btn = document.getElementById('my-btn')
btn.onclick=add


