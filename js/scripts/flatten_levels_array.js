function steamrollArray(val,flatArr=[]) {
    val.forEach(item => {
      if (Array.isArray(item)) steamrollArray(item, flatArr);
      else flatArr.push(item);
    });
    return flatArr;
  }

  steamrollArray([1, [2], [3, [[4]]]]);