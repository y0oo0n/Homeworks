/*
1. 프로퍼티 합 구하는 코드 작성하기
-> 아래 객체 속 모든 팀원의 월급을 합한 값을 구하고, 그 값을 변수 sum에 저장해주는 코드를 작성해보세요!
[Hint]
※ salaries가 비어있다면 sum에 0이 저장되어야 합니다.
※ 반복문을 사용해보세요.
※ 객체의 값을 참조하는 방법을 떠올려보세요! */

let salaries = {
  John: 100,
  Ann: 160,
  Pete: 130,
};


let sum = 0;
for (let key in salaries) {
  sum += salaries[key];
}

console.log(sum)
/*
  
  여기에 1번 문제의 정답 코드를 작성해보세요. 
  
  */

