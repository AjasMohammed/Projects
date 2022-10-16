var equation = ""
function btn_clk(val){
    document.getElementById("display").value+=val;
    equation+=document.getElementById("display").value
}

function btn_clr(){
    document.getElementById("display").value=""
    sum = "s"
}
function eqls(){
    // var val = document.getElementById("display").value
    // console.group(val)
    try{
        var res = eval(equation)
        document.getElementById("display").value=res
    }
    
    catch{
        document.getElementById("display").value="Syntax Error"
    }
}
function calc(val){
    equation+=val
    // console.log(equation)
    document.getElementById("display").value = ""
    
    
}