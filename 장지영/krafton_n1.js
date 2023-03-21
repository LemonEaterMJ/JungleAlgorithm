function solution(A) {
    var numDict = {};
    var keyList = new Array;

    var listA = Array.from(A).sort();

    let count = 1;
    for (let i = 0; i < listA.length; i++) {
        if (i == listA.length - 1) {
            if (listA[i] in numDict) {
                numDict[listA[i]] += 1;
            } else {
                numDict[listA[i]] = 1;
                keyList.push(listA[i]);
            }
        }
        else if (listA[i] == listA[i + 1]) {
            count += 1;
            continue;
        } else {
            numDict[listA[i]] = count;
            keyList.push(listA[i]);
        }
    }

    keyList.sort();
    for (var key in keyList) {
        if (key == numDict[key]) {
            return key;
        } 
    }
    return 0;
}