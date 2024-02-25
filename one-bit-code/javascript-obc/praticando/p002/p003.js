

function bubbleSort (array) {
    let arr = array.slice()
    const n = arr.length
    for (let i = 0; i < n -1; i++) {
        for (let j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                let aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
            }
        }
    }

    return arr
}


array = [4, 6, 3, 8, 2]
print(`O array original: ${array} \nArray ordenado: ${bubbleSort(array)}`)