
window.onload = function(){
    let qty = document.getElementsByName('fdqty')
    let fdname = document.getElementsByName('fdname')
    let fdprice = document.getElementsByName('fdprice')
    let fdid = document.getElementsByName('fdid')
    let car_res = document.getElementById('car_res')
    let str = `` ; let str_res = ``
    // 偵測+-
    for(let i = 0 ;i < qty.length;i++){
        document.getElementsByName('plus')[i].onclick = function(){
            tmp = ''
            qty[i].value = parseInt(qty[i].value)+1
            console.log('chage')
            if (str.includes(fdname[i].innerText)){
                if (qty[i].value == '0' ){
                    document.getElementById(fdid[i].innerText).remove()
                }
                else{
                    document.getElementById(fdid[i].innerText).innerText = `${fdname[i].innerText} x ${qty[i].value} = ${parseInt(fdprice[i].innerText)*parseInt(qty[i].value)}`
                }
                
            }
            else{
                
                str += `<p id='${fdid[i].innerText}'> ${fdname[i].innerText} x ${qty[i].value} = ${parseInt(fdprice[i].innerText)*parseInt(qty[i].value)}</p>`
                str_res += `${fdname[i].innerText}x${qty[i].value}=${parseInt(fdprice[i].innerText)*parseInt(qty[i].value)}apple`
                document.getElementById('car').innerHTML = str
                car_res.value = str_res
                console.log(car_res.value)
            }

        }

        document.getElementsByName('minus')[i].onclick = function(){
            if(parseInt(qty[i].value) < 1){
                document.getElementById(fdid[i].innerText).remove()

            }
            else{
                qty[i].value = parseInt(qty[i].value)-1
                document.getElementById(fdid[i].innerText).innerText = `${fdname[i].innerText} x ${qty[i].value} = ${parseInt(fdprice[i].innerText)*parseInt(qty[i].value)}`
                console.log('chage')
                
            }
        }
    }

    document.getElementById('check').onclick = function(){
        car_res.value = document.getElementById('car').innerText
    }
    // 偵測變動
    for(let i = 0 ;i < qty.length;i++){
        qty[i].onchange = function(){
            console.log(123)
            

        }
        // if(qty[i].value != 0 ){
        // }
    }

    

}