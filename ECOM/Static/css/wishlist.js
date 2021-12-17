var updateBtns =  document.getElementsByClassName('update-wishlist')

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
        var url = '/update_wishlist/'
    
        fetch(url, {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken,
                },
                body:JSON.stringify({'productId': productId, 'action': action})
    
        })
    
        .then((response) =>{
            return response.json()
            })
        .then((data) =>{
        console.log('data:', data)
        location.reload()
        })
    }


    var removebtn =  document.getElementsByClassName('remove-prod-wishlist')

for(var i=0; i < removebtn.length; i++){
    removebtn[i].addEventListener('click', function(){
     var prodId =  this.dataset.product
     console.log('productId:' , prodId)
     RemoveProd(prodId)
     })
    }

function RemoveProd(productId, action){
    console.log('User logged in')
    var url = '/remove_wishlist/'

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