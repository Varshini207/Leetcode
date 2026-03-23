class Solution {
    public String findDifferentBinaryString(String[] nums) {
        ArrayList<Integer> l=new ArrayList();
        for(int i=0;i<nums.length;i++){
            int n=Integer.parseInt(nums[i],2);
            l.add(n);
        }
        int s = nums.length;
        for(int i=0;i<Math.pow(2,s);i++){
            if(!l.contains(i)){
                String a=Integer.toBinaryString(i);
                while(a.length()<s){
                    a='0'+a;
                }
                return a;
            }
        }
        return "";
    }
}