public class DynamicClassLoading {

    public static void main(String[] args){
        ClassLoader classLoader = DynamicClassLoading.class.getClassLoader();

        try {
            Class coin = classLoader.loadClass("Coin");
            System.out.println("coin.getName() = " + coin.getName());
            //System.out.println("coin.getValue() = " + coin.getValue());
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

}
