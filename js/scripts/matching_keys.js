function whatIsInAName(collection, source) {
    const arr = [];
    // Only change code below this line
      let keys = Object.keys(source)
      return collection.filter(obj => keys.every(key => obj.hasOwnProperty(key) &&
                              obj[key] === source[key]))

    // Only change code above this line
    return arr;
  }

  whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" });