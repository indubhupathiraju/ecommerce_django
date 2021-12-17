

var updateBtns =  document.getElementsByClassName('update-cart')

console.log(updateBtns.length);
for(var i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
     var productId =  this.dataset.product
     var action= this.dataset.action
     console.log('productId:' , productId, 'action:', action)
     updateUserOrder(productId, action)
     })
    }


function updateUserOrder(productId, action){
    console.log('User logged in')
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) =>{
        console.log('i m in')
        console.log(response);
        //return window.location.href="../../prodview"
        //return response.json()
        })
    .then((data) =>{
    console.log('data:', data)
    // location.reload()
    });
}

var buyBtns =  document.getElementsByClassName('buy-now')
console.log(buyBtns.length);

for(var i=0; i < buyBtns.length; i++){
    buyBtns[i].addEventListener('click', function(){
     var productId =  this.dataset.product
     var action= this.dataset.action
     console.log('productId:' , productId, 'action:', action)
     Buynow(productId, action)
     })
    }

function Buynow(productId, action){
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
            },
            body:JSON.stringify({'productId': productId, 'action': action})

    })
    .then((response) =>{
        return window.location.href="../../checkout"
        })
    .then((data) =>{
    console.log('data:', data)
    })
}

var removebtn =  document.getElementsByClassName('remove-prod')

for(var i=0; i < removebtn.length; i++){
    removebtn[i].addEventListener('click', function(){
     var prodId =  this.dataset.product
     console.log('productId:' , prodId)
     RemoveProd(prodId)
     })
    }

function RemoveProd(productId, action){
    console.log('User logged in')
    var url = '/remove_prod/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
            },
            body:JSON.stringify({'productId': productId})

    })

    .then((response) =>{
        return response.json()
        })
    .then((data) =>{
    console.log('data:', data)
    location.reload()
    })
}

//saving address
        const btn = document.querySelector('#place-order');
        // handle click button
        btn.onclick = function () {
            const rbs = document.querySelectorAll('input[name="address"]');
            const pyts = document.querySelectorAll('input[name="paymentmode"]');
            let Value;
            for (const pyt of pyts) {
                if (pyt.checked) {
                    value = pyt.value;
                    break;
                }
            }

            let selectedValue;
            for (const rb of rbs) {
                if (rb.checked) {
                    selectedValue = rb.value;
                    break;
                }
            }
            SaveOrder(selectedValue,value)

        };

 function SaveOrder(selectedValue,value){
    var url = '/order_completed/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
            },
            body:JSON.stringify({'selectedValue': selectedValue, 'value':value})

    })

    .then((response) =>{
        return window.location.href="../../successful"
        })
    .then((data) =>{
    console.log('data:', data)
    })
}