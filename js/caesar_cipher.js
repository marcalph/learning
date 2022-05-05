function rot13(str) {
    let res = ''
    let start = 'A'
    let start_charcode = start.charCodeAt(0)
    for (let i=0; i<str.length; i++){
      if (str[i].match(/\W/)){
        res+=str[i]
      } else {
      res+= String.fromCharCode((str.charCodeAt(i)+13-start_charcode)%26+start_charcode)

      }
    }
    console.log(res)
    return res;
  }

  rot13("SERR PBQR PNZC");