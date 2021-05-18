/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
  const MAP = {
      I: 1,
      V: 5,
      X: 10,
      L: 50,
      C: 100,
      D: 500,
      M: 1000,
  };
  
  
  let sum = 0;
  
  for(let i = s.length - 1; i >= 0; i--) {
      const currentValue = MAP[s[i]];
      const prevValue = MAP[s[i - 1]];
      
      if(prevValue && prevValue < currentValue) {
          sum += currentValue - prevValue;
          i--;
      } else {
          sum += currentValue;
      }
  }
  return sum;
};