function sliceBack(sliceArr) {
    let arrLen = sliceArr.length;
    if (arrLen < 1) {
        return 0;
    } else {
        for (let i = 0; i >= arrLen; i++) {
            if (i == arrLen) {
                return sliceArr;
            }
            else if (sliceArr[i] == sliceArr[i + 1]) {
                continue;
            } else {
                return sliceArr.slice(0, i);
            }
        }
    }
}



function solution(A) {
    var listA = Array.from(A);
    if (listA.length < 1) {
        return 0;
    } 
    else if (listA.length == 1) {
        if (listA[0] == 1) {
            return 1; 
        } else {
            return 0;
        }
    } 

    listA.sort().reverse();
    
    while(listA.length < 1) {
        var sliceA = sliceBack(listA);
        var sliceALen = sliceA.length;
        if (sliceA[0] == sliceALen) {
            return sliceA[0];
        } else {
            listA = listA.slice(sliceALen);
        }
    }
    return 0;
}



