let btn=document.getElementById("add")
btn.onclick=e=>{
    let r1=document.getElementById("task").value
    let r2=document.getElementById("duedate").value
        console.log(r1,r2)
        fetch('/h',
        {
            method:"post",
            body:JSON.stringify({"task_name":r1,"due_date":r2})
        }
    
    ).then(res=>res.json())
    .then(r=>{
        if (r.status==='ok'){
        }
        else{
            alert("someting went wrong")
        }
    })
    
}





function is_delete(a){
    console.log(a)
    fetch("m?task_id="+a,{
        method:"delete"
    }).then (res=> res.json())
    .then(r=>{
        if (r.status==="ok"){
            window.location.reload()
        }
        else{
            alert("error")
        }
    })
}


function mark_completed(a){
    console.log(a)
    fetch("put?task_id="+a,{
        method:"put"
    }).then (res=> res.json())
    .then(r=>{
        if(r.status==="ok"){  
            window.location.reload() 
        }
    })
}