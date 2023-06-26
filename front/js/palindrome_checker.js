function palindrome(str) {
    str = str.match(/[a-zA-Z0-9]/g).join('').toLowerCase()
    console.log(str)
    let left = 0
    let right = str.length-1
    while (left<=right){
      if (str[left]==str[right]){
        left++
        right--
      } else {
        return false
      }
    }
    return true;
  }

  palindrome("eye");