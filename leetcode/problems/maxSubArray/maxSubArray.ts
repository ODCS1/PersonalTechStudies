// GIVEN AN INTEGER ARRAY NUMS, FIND THE SUBARRAY WITH THE LARGEST SUM, AND RETURN ITS SUM.

function maxSubArray(nums: number[]): number {
    let maxSum = nums[0];
    let currSum = nums[0];
    for (let i = 1; i < nums.length; i++){
        
        if (currSum < 0) {
            currSum = 0;
        }

        currSum += nums[i];

        if (currSum > maxSum) {
            maxSum = currSum;
        }
    }

    return maxSum;
}