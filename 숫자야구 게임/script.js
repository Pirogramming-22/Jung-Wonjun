//랜덤 세자리 숫자 생성
let digits = [];

let firstDigit;
firstDigit = Math.floor(Math.random() * 10);
digits.push(Math.floor(Math.random() * 10)); 

let secondDigit;
do {
    secondDigit = Math.floor(Math.random() * 10);
} while (secondDigit === digits[0]);
digits.push(secondDigit);

let thirdDigit;
do {
    thirdDigit = Math.floor(Math.random() * 10);
} while (thirdDigit === digits[0] || thirdDigit === digits[1]);
digits.push(thirdDigit);

console.log(digits);


// 정답체크 및 횟수관리
let remainChance = 9;
document.getElementById("attempts").innerText = remainChance;

function answerCheck(strike) {
    if (strike === 3) {
        document.getElementById("game-result-img").src = "./success.png";
        document.getElementsByClassName("submit-button")[0].disabled = true;
    }
    else {
        remainChance--;
        document.getElementById("attempts").innerText = remainChance;
        if (remainChance === 0) {
            document.getElementById("game-result-img").src = "./fail.png";
            document.getElementsByClassName("submit-button")[0].disabled = true;
        }
    }
    console.log(document.getElementById("attempts").innerText); //확인용도
    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";
}

// 초기화
let num1;
let num2;
let num3;

// 입력한 숫자를 확인하는 함수
function check_numbers() {
    num1 = document.getElementById("number1").value;
    num2 = document.getElementById("number2").value;
    num3 = document.getElementById("number3").value;
    if (num1 === "" || num2 === "" || num3 === "") {
        console.log("하나 이상의 input 값이 비어 있습니다!");
        document.getElementById("number1").value = "";
        document.getElementById("number2").value = "";
        document.getElementById("number3").value = "";
    }
    else {
        let inputNums = [num1, num2, num3];
        let strike = 0;
        let ball = 0;
        console.log(inputNums);
        for (let i = 0; i < 3; i++) {
            if (digits[i] == inputNums[i]) {
                console.log("strike증가!");
                strike++;
            }
            for (let j = 0; j < 3; j++) {
                if (digits[i] == inputNums[j] && i != j) {
                    console.log("ball증가!");
                    ball++;
                }
            }
        }
        // 결과 div 설정
        let resultDisplay = document.createElement('div');
        resultDisplay.classList.add('result-display');

        let checkResult = document.createElement('div');
        checkResult.classList.add('check-result');

        // 입력한 숫자
        let numSet = document.createElement('div');
        inputNums.forEach((num) => {
            let numDiv = document.createElement('div');
            numDiv.textContent = num;
            numDiv.classList.add('num-result');
            numSet.appendChild(numDiv);
        });

        // 구분선
        let centerDiv = document.createElement('div');
        centerDiv.textContent = ':';
        centerDiv.classList.add('num-result');

        // Strike, Ball, Out
        let strikeDiv = document.createElement('div');
        let ballDiv = document.createElement('div');
        let outDiv = document.createElement('div');
        let strikeNumDiv = document.createElement('div');
        let ballNumDiv = document.createElement('div');

        strikeDiv.textContent = 'S';
        ballDiv.textContent = 'B';
        outDiv.textContent = 'O';
        strikeNumDiv.textContent = strike;
        ballNumDiv.textContent = ball;

        strikeDiv.classList.add('num-result', 'strike');
        ballDiv.classList.add('num-result', 'ball');
        outDiv.classList.add('num-result', 'out');
        strikeNumDiv.classList.add('num-result');
        ballNumDiv.classList.add('num-result');

        
        let leftSide = document.createElement('div');
        leftSide.appendChild(numSet);

        let middleSide = document.createElement('div');
        middleSide.appendChild(centerDiv);

        let rightSide = document.createElement('div');
        if (strike == 0 && ball == 0) {
            rightSide.appendChild(outDiv);
        }
        else {
            rightSide.appendChild(strikeNumDiv);
            rightSide.appendChild(strikeDiv);
            rightSide.appendChild(ballNumDiv);
            rightSide.appendChild(ballDiv);
        }

        // 결과 출력
        checkResult.appendChild(leftSide);
        checkResult.appendChild(middleSide);
        checkResult.appendChild(rightSide);
    
        resultDisplay.appendChild(checkResult);

        let results = document.getElementById("results");
        if (results) {
            results.appendChild(resultDisplay);
        }

        answerCheck(strike, ball);
        console.log(strike, ball);
        console.log(checkResult);
        console.log(resultDisplay);
    }
}