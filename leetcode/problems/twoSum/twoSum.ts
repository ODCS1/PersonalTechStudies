function twoSum(nums: number[], target: number): number[] {
    interface Values {
        [key: number]: number;
    }

    let values:Values = {};

    for(let i = 0; i < nums.length; i++) {
        let diff = target - nums[i];

        if (diff in values) {
            return [values[diff], i];
        }

        values[nums[i]] = i;
    }

    return [];
};