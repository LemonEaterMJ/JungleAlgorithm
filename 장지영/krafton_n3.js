


function solution(A) {
    var listA = Array.from(A);
    if (listA.length < 2) {
        if (listA.length == 1) {
            return 1;
        } else {
            return 0;
        }
    }

    listA.sort();
    var flag = 1;
    var answer = 1;
    var maxNum = listA[-1];

    for (let i = 0; i <= listA.length - 1; i++) {
        if (listA[i] == maxNum) {
            answer += 1;
            break;
        } 
        else if (listA[i] == listA[i + 1]) {
            flag++;
            continue;
        } else {
            if (flag > 1) {
                answer += 2;
            } else {
                //flag == 1
                answer += 1;
            }
            flag = 1;
        }
    }
    return answer;
}