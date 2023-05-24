import java.util.HashMap;
import java.util.Set;

/**
 * leetcode242
 */


public class leetcode242 {
    public static void main(String[] args) {
        String s = "a";
        String t = "ab";
        isAnagram(s,t);


    }


    // 思路：构建两张hash表，记录每个字母的次数.15ms,42.8MB
    public static boolean isAnagram(String s,String t) {
        if (s.length() != t.length()) {return false;}
        HashMap<Character,Integer> hM1 = new HashMap<>();
        HashMap<Character,Integer> hM2 = new HashMap<>();

        char[] sList = s.toCharArray();
        char[] tList = t.toCharArray();

        for (char i : sList) {
            if (!(hM1.containsKey(i))) {
                    hM1.put(i,1);
            } else {
                hM1.put(i,(int)hM1.get(i) + 1);
            }
        }

        for (char j : tList) {
            if (!(hM2.containsKey(j))) {
                hM2.put(j,1);
            } else {
                hM2.put(j,(int)hM2.get(j) + 1);
            }
        }

        Set<Character> h1 = hM1.keySet();
        for (char i : h1) {
            int value1 = hM1.get(i);
            if (!(hM2.containsKey(i))) {return false;}
            int value2 = hM2.get(i);
            System.out.println(value1);
            System.out.println(value2);
            if (value1 != value2) {
                return false;
            }
        }
        return true;
    }


    // 28ms,40.9MB(5.25,97.52)
    public static boolean isAnagram2(String s,String t) {
        if (s.length() != t.length()) {return false;}

        HashMap<Character, Integer> hM = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if (!(hM.containsKey(s.charAt(i)))) {
                hM.put(s.charAt(i),1);
            } else {
                hM.put(s.charAt(i),(int)hM.get(s.charAt(i)) + 1);
            }

            if (!(hM.containsKey(t.charAt(i)))) {
                hM.put(t.charAt(i),-1);
            } else {
                hM.put(t.charAt(i),(int)hM.get(t.charAt(i)) - 1);
            }
        }

        Set<Character> letterSet = hM.keySet();

        for (char i : letterSet) {
            if (hM.get(i) != 0) {return false;}
        }

        return true;
    }

    // 4ms,40.6MB(40.7,99.72 %)
    public static boolean isAnagram3(String s,String t) {
        if (s.length() != t.length()) {return false;}

        int[] letterList = new int[26];

        for (int i = 0; i < s.length(); i++) {
            letterList[s.charAt(i) - 'a'] += 1;
            letterList[t.charAt(i) - 'a'] -= 1;
        }

        for (int i : letterList) {
            if (i != 0) {return false;}
        }

        return true;
    }
}

