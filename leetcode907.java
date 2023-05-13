import java.util.Deque;
import java.util.LinkedList;

/**
 * leetcode907: 贡献值法与单调栈结合
 */

public class leetcode907 {
    static final int MAX_VALUE = 1000000007;
    public static void main(String[] args) {
        int[] arr = {11,81,94,43,3};

        int ans = sumSubarrayMins(arr);
        System.out.println(ans);


    }

    public static int sumSubarrayMins(int[] arr) {
        int[] rightFirst = new int[arr.length];
        int[] leftFirst = new int[arr.length];
        Deque<Integer> stack = new LinkedList<>();

        int findIndex;

        // 初始化默认值
        for (int i = 0; i < arr.length; i++) {
            leftFirst[i] = -1;
        }


        for (int i = 0 ; i < arr.length ; i++) {
            if (stack.isEmpty() ||
                    arr[stack.peek()] <= arr[i]) {
                stack.push(i);
            } else {
                while (!(stack.isEmpty()) && (arr[stack.peek()] > arr[i])) {
                    findIndex = stack.pop();
                    rightFirst[findIndex] = i;
                    leftFirst[findIndex] = stack.isEmpty() ? -1 : stack.peek();
                }
                stack.push(i);
            }
        }
        while (!stack.isEmpty()) {
            findIndex = stack.pop();
            rightFirst[findIndex] = arr.length;
            leftFirst[findIndex] = stack.isEmpty()? -1 : stack.peek();
        }

        long ans = 0;
        for (int i = 0; i < arr.length; i++) {
            ans = (ans + (long)(arr[i] * (i - leftFirst[i]) * (rightFirst[i] - i)));
        }

        while (ans >= (MAX_VALUE)) {
            ans -= MAX_VALUE;
        }

        return (int)ans;


    }

}



class MyStack {
    int maxSize;  // 栈的最大容量
    int[] stack; // 存放栈元素的容器
    int top = -1; // 栈顶位置索引

    public MyStack(int maxSize) {
        this.maxSize = maxSize;
        stack = new int[this.maxSize];
    }

    public boolean isEmpty() {
        if (top == -1) {
            return true;
        } else {return false;}
    }

    public boolean isFull() { // 用于判断栈是否满，防止溢出非法访问
        if (top == maxSize - 1) {return true;}
        else {return false;}
    }

    public void push(int Element) throws StackOverflowError { // 定义入栈操作
        stack[++top] = Element;
    }

    public int pop() throws StackOverflowError { // 定义出栈操作
        return stack[top--];
    }

    public int getTop() { // 返回栈顶元素
        return stack[top];
    }
}