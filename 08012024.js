//! Problem Link : https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

class Solution {

    search(pat, txt) {
        //create a temp suffix prefix array 
        // a a b a a b a a
        // 0 1 0 1 2 3 4 5
        const p = pat.length;
        const N = txt.length
        const suf_puf = Array(p).fill(0);

        suf_puf[0] = 0
        let i = 1;
        let j = 0;

        while (i < p) {
            const v1 = pat[i];
            const v2 = pat[j];
            if (v1 == v2) {
                suf_puf[i] = j + 1
                i += 1
                j += 1
            }
            else {
                if (j != 0) {
                    j = suf_puf[j - 1]
                }
                else {
                    suf_puf[j] = 0
                    i += 1
                }
            }
        }

        i = 0;
        j = 0;
        let answer = [];
        while ((N - i) >= (p - j)) {
            const mt = txt[i];
            const pt = pat[j];

            if (mt == pt) {
                i += 1;
                j += 1;
            }
            if (j == p) {
                answer.push(i - j + 1)
                j = suf_puf[j - 1]
            }
            else if (i < N & (mt != pt)) {
                if (j != 0) j = suf_puf[j - 1]
                else i += 1
            }
        }
        return (answer.length == 0 ? [-1] : answer)
    }
}
function kmp(pat, txt) {
    //create a temp suffix prefix array 
    // a a b a a b a a
    // 0 1 0 1 2 3 4 5
    const p = pat.length
    const suf_puf = Array(p).fill(0);

    suf_puf[0] = 0
    let i = 1;
    let j = 0;

    while (i < p) {
        const v1 = pat[i];
        const v2 = pat[j];
        if (v1 == v2) {
            suf_puf[i] = j + 1
            i += 1
            j += 1
        }
        else {
            if (j != 0) {
                j = suf_puf[j - 1]
            }
            else {
                suf_puf[j] = 0
                i += 1
            }
        }
    }

    i = 0;
    j = 0;
    let count = 0;
    let answer = [];
    while (i < txt.length) {
        const mt = txt[i];
        const pt = pat[j];

        if (mt == pt) {
            i += 1;
            j += 1;
            count += 1
            console.log(count)
        }

        else {
            if (j != 0) j = suf_puf[j - 1]
            else i += 1
        }
        if (count == p) {
            console.log("h")
            answer.push(i - count + 1)
            count = 0
        }
    }
    return (answer.length == 0 ? -1 : answer)
}

console.log(kmp("n", "cxggbw"))

