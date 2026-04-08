class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        Map<Character, Integer> char_bucket = new HashMap<>();

        for (char c : s.toCharArray()) {
            int current_frequency = char_bucket.getOrDefault(c, 0);
            char_bucket.put(c, current_frequency+1);
        }

         for (char c : t.toCharArray()) {
            int current_frequency = char_bucket.getOrDefault(c, 0);
            char_bucket.put(c, current_frequency-1);
        }

        for (Map.Entry<Character, Integer> entry : char_bucket.entrySet()) {
            Character key = entry.getKey();
            int current_frequency = char_bucket.getOrDefault(key, 0);
            if (current_frequency < 0) return false;
        }

        return true;
    }
}
