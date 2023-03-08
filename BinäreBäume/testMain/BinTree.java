public class BinTree<ContentType>{

    /* --------- Anfang der privaten inneren Klasse -------------- */
    private class Node{

        private Node left;
        private Node right;
     private ContentType value; 

     public Node (Node pLeft, Node pRight, ContentType pValue) {
            left = pLeft;
            right = pRight;
            value = pValue;
        }

        public ContentType getValue(){
            return value; 
         }

        public Node getLeft(){
            return left;
        }

        public Node getRight(){
            return right;
        }
    }
    /* ----------- Ende der privaten inneren Klasse -------------- */

    private Node root;

    //leeren Baum
    public BinTree(){
        root = null;
    }

    //Baum mit nur einer Wurzel
    public BinTree(ContentType v){
        root = new Node(null, null, v);
    }

    //Baum aus zwei gegeben Teilbäumen mit neuer Wurzel 
    public BinTree(BinTree left, BinTree right, ContentType v){
        root = new Node(left.root, right.root, v);
    }

    public ContentType getRoot(){
        if(root == null){
            System.err.println("ein leerer Baum hat keine Wurzel");
            return null;
        }else{
            return root.getValue();
        }
        
    }

    public BinTree getLeft(){
        if(root == null){
            System.err.println("Ein leere Baum hat keinen linken Teilbaum");
            return null;
        }else{
            BinTree l = new BinTree();
            l.root = root.getLeft();
            return l;
        }
    }

    public BinTree getRight(){
        if(root == null){
            System.err.println("Ein leere Baum hat keinen linken Teilbaum");
            return null;
        }else{
            BinTree r = new BinTree();
            r.root = root.getRight();
            return r;
        }
    }

    public boolean isEmpty(){
        return root == null;
    }

    public ContentType suche(BinTree b, ContentType value){
        if(b.getRoot() == value){
            return value;
        }

        BinTree btLeft = b.getLeft(); 
        if(btLeft.isEmpty() == false){
            suche(btLeft, value);
            return value;
        }

        BinTree btRight = b.getRight();
        if(btRight.isEmpty() == false){
            suche(btRight, value);
            return value;
        }
        return null;
    }
}

