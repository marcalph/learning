function sumPrimes(num) {
    let prev = []
    let cursum = 0
    for (let i=2; i<= num; i++){
      if (!prev.some(elt=>i%elt==0)){
        cursum+=i
      }
      prev.push(i)
    }
    return cursum;
  }

  sumPrimes(10);