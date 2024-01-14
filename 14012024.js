//! Problem Link : 

function repeatedRows(Matrix, M, N) {
    console.log(M,N)
    const hmap = {}
    const ans = []
    for (let r = 0; r < M; r++) {
        let temp_string = ''
        for (let c = 0; c < N; c++) {
            temp_string += Matrix[r][c]
        }
        if (temp_string in hmap) {
            ans.push(r)
        }
        else {
            hmap[temp_string] = 1
        }
    }
    return ans

}

const matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1]
]

console.log(repeatedRows(matrix, matrix.length, matrix[0].length))
