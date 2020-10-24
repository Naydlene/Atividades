function exibePar(n1,n2){
    var lista = []  
        while(n1<=n2){
            if(n1%2==0){
            lista.push(n1)
            }
        n1++    
        }
    return lista
    }

   console.log(exibePar(1,100))