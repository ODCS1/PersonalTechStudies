package praticando.p016;


public class Ex09 {
    private static int findMajorityElement(int[] nums) {
        int count = 0;
        Integer candidate = null;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
                count = 1;
            } else if (candidate == num) {
                count++;
            } else {
                count--;
            }
        }

        count = 0;
        for (int num : nums) {
            if (num == candidate) {
                count++;
            }
        }

        if (count > nums.length / 2) {
            return candidate;
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {2, 2, 3, 4, 2, 2, 5};
        int majorityElement = findMajorityElement(arr);
        if (majorityElement != -1) {
            System.out.println("O elemento majoritário é: " + majorityElement);
        } else {
            System.out.println("Não há elemento majoritário no array.");
        }
    }
}