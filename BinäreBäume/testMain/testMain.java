public class testMain{

    public static void main(String[] args){
        BinTree oma1 = new BinTree<String>("J. Bouvier");
        BinTree opa1 = new BinTree<String>("C. Bouvier");
        BinTree mutter = new BinTree<String>(oma1, opa1, "Marge Simpson");
        BinTree oma2 = new BinTree<String>("M. Simpson");
        BinTree opa2 = new BinTree<String>("A. J. Simpson");
        BinTree vater = new BinTree<String>(oma2, opa2, "Homer Simpson");
        BinTree ich = new BinTree<String>(mutter, vater, "Lisa Simpson");
        ich.suche(ich, "M. Simpson");
    }
}