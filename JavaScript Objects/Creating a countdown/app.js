function countdown(n){
  if(n < 1) {
    return []; 
  } else {
    const newArr = countdown(n - 1); 
    newArr.unshift(n); 
    return newArr; 
  } 
}     