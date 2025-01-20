// 121. Best Time to Buy and Sell Stock

// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

function maxProfit(prices: number[]): number {
    let h: number = prices[0];
    let l: number = prices[0];
    let result: number = h - l;

    for(let i = 0; i < prices.length; i++){
        if(prices[i] < l) {
            l = prices[i];
            h = prices[i];
        }else if (prices[i] > h){
            h = prices[i];
        }

        if ((h - l) > result) result = h - l;
    }

    return result;
};
