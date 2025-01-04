// DOM 요소 선택
const watchTime = document.getElementById('watch_time');
const startButton = document.getElementById('start');
const stopButton = document.getElementById('stop');
const resetButton = document.getElementById('reset');
const recordList = document.getElementById('recording_list');
const allCheckButton = document.getElementById('all_check_button');
const trashButton = document.getElementById('trash_button');

let timer;
let isRunning = false;
let time = 0;
let timeDisplay = '00:00';
let allCheck = false;

// 시간 업데이트 함수
function updateTimeDisplay() {
    const seconds = Math.floor(time / 100);
    const centiseconds = time % 100;
    timeDisplay = `${String(seconds).padStart(2, '0')}:${String(centiseconds).padStart(2, '0')}`;
    watchTime.textContent = timeDisplay;
}

// 스톱워치 시작
function startWatch() {
    isRunning = true;
    timer = setInterval(() => {
        time++;
        updateTimeDisplay();
    }, 10); // 0.01초(10ms)마다 실행
}

// 스톱워치 멈추기
function stopWatch() {
    clearInterval(timer);
    isRunning = false;
    addRecord();
}

// 스톱워치 초기화
function resetWatch() {
    clearInterval(timer);
    isRunning = false;
    time = 0;
    updateTimeDisplay();
}

// 기록을 화면에 추가하는 함수
function addRecord() {
    const recordItem = document.createElement("li");
    const checkButton = document.getElementById('all_check_button').cloneNode(true);
    checkButton.id = 'check_button';
    checkButton.classList.add("check_button")
    const checkImage = checkButton.querySelector('svg');
    checkImage.id = 'check_image'
    checkImage.classList.add("check_image")

    const recordTime = document.createElement("h3")

    recordTime.textContent = timeDisplay;

    recordItem.append(checkButton);
    recordItem.append(recordTime);

    recordList.appendChild(recordItem);
}

// 전체 선택 버튼 상태 업데이트 함수
function updateAllCheckButtonState() {
    const records = recordList.querySelectorAll('li');  // 모든 기록 항목 (li)
    const checkedRecords = recordList.querySelectorAll('.checked');  // 체크된 항목들
    console.log(records.length);
    console.log(checkedRecords.length/2);

    if (records.length === checkedRecords.length/2 && records.length > 0) {
        allCheckButton.classList.add('checked');
        allCheckButton.querySelector('svg').style.display = "block";
        console.log("전체 선택 상태");
    } else {
        allCheckButton.classList.remove('checked');
        allCheckButton.querySelector('svg').style.display = "none";
        console.log("전체 선택 해제 상태");
    }
}

// 전체선택버튼
allCheckButton.addEventListener('click', () => {
    const records = recordList.querySelectorAll('li');
    console.log("전체선택버튼 눌림");
    if (!allCheckButton.classList.contains('checked')) {
        records.forEach(record => {
            const checkButton = record.querySelector('.check_button'); 
            if (!checkButton.classList.contains('checked')) {
                checkButton.classList.add('checked');
                record.classList.add('checked');
                checkButton.querySelector('svg').style.display = 'block';
            }
        });
    } else {
        records.forEach(record => {
            const checkButton = record.querySelector('.check_button');
            if (checkButton.classList.contains('checked')) {
                checkButton.classList.remove('checked');
                record.classList.remove('checked');
                checkButton.querySelector('svg').style.display = 'none';
            }
        });
    }

    updateAllCheckButtonState();
});


// 이벤트 리스너
// start 버튼
startButton.addEventListener('click', () => {
    if (!isRunning) {
        startWatch();
    }
});

// stop버튼
stopButton.addEventListener('click', () => {
    if (isRunning) {
    stopWatch();
    }
});

// reset버튼
resetButton.addEventListener('click', resetWatch);

// 선택버튼
recordList.addEventListener("click", (event) => {
    console.log("클릭함");
    if (event.target && (event.target.matches(".check_button") || event.target.matches(".check_image"))) {
        const checkButton = event.target.closest(".check_button");
        const recordItem = checkButton.closest('li');

        if (checkButton.classList.contains("checked")) {
            checkButton.classList.remove("checked");
            recordItem.classList.remove("checked");
            checkButton.querySelector('svg').style.display = 'none';
            console.log("체크된 상태 제거");
        } else {
            checkButton.classList.add("checked");
            recordItem.classList.add("checked");
            console.log("체크 안된 상태 추가");
            checkButton.querySelector('svg').style.display = 'block';
        }

        updateAllCheckButtonState();
    }
});

// 휴지통버튼
trashButton.addEventListener('click', () => {
    const checkedRecords = recordList.querySelectorAll('.checked');
    checkedRecords.forEach(record => {
        record.remove();
    });

    updateAllCheckButtonState();
});