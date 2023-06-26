function destroyer(arr, ...vals) {
    return arr.filter(elt=>!vals.includes(elt))
  }

  destroyer([1, 2, 3, 1, 2, 3], 2, 3);