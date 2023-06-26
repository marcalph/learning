function diffArray(arr1, arr2) {
    return arr1.concat(arr2).filter(elt=>
     !arr1.includes(elt)||!arr2.includes(elt))
   }

   diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);