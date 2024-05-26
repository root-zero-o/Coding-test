// 2024.5.26.
// https://school.programmers.co.kr/learn/courses/30/lessons/181916

function solution(a, b, c, d) {
    const arr = [a, b, c, d];
    const obj = {};
      
      for(let i = 0; i < 4; i++){
          let num = arr[i];
          obj[num] = typeof obj[num] === 'number' ? obj[num] + 1 : 1
      }
     
      const counts = [...Object.values(obj)] 
      const keys = [...Object.keys(obj).sort((a, b) => obj[b] - obj[a])].map(Number)
      const max = Math.max(...counts)
      
      let answer = 0;
      
      switch(max){
          case 4 :
              answer = 1111 * a;
              break;
          case 3 : 
              answer = (10 * keys[0] + keys[1]) ** 2;
              break;
          case 2 : 
              if(keys.length === 2){
                  answer = (keys[0] + keys[1]) * Math.abs(keys[0] - keys[1]);
                  break;
              } else if(keys.length === 3){
                  answer = keys[1] * keys[2];
                  break;
              }
          case 1 : 
              answer = Math.min(...keys);
              break;
      }
      
      return answer;
  }