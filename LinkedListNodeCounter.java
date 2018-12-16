import java.util.*;
import java.lang.String;

class Node {
    int data;
    Node next;
    Node(int data) {
        this.data = data;
    }
}

class LinkedList {
    Node head;
    Node nodeB;
    Node nodeC;
    Node nodeD;
    Node nodeE;
    Node nodeF;
    public LinkedList() {
        head = new Node(4);
        nodeB = new Node(2);
        nodeC = new Node(3);
        nodeD = new Node(10);
        nodeE = new Node(2);
        nodeF = new Node(12);
        head.next = nodeB;
        nodeB.next = nodeC;
        nodeC.next = nodeD;
        nodeD.next = nodeE;
        nodeE.next = nodeF;
        nodeF.next = null;
    }
}

public class Main {
    static int countNodes(Node head) {
        int count = 1;
        Node current = head;
        while (current.next != null) {
            current = current.next;
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        LinkedList List = new LinkedList();
        System.out.println("This Linked List has: " + countNodes(List.head) + " Nodes!");
    }
}
