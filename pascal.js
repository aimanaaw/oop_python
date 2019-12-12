const makeCounter = function(startValue) {
  value: () => {
    if (typeof(startValue) == int && startValue !== null) {
      return startValue;
    }
  };
  increment: () => {
    return this.value ++;
  };
  decrement: () => {
    return this.value --
  }
  }