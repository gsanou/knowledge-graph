import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class TestCsv {
    public static ArrayList<String> result_list = new ArrayList();

    public static ArrayList getList(){
        TestCsv test = new TestCsv();
        test.test();
//        System.out.print(result_list);
        return result_list;
    }

    public static void main(String[] args) {
        TestCsv test = new TestCsv();
        test.test();
    }


    public void test() {
        try {
            //先FileReader把文件读出来再bufferReader按行读  reader.readLine(); 没有标题用不着了
            BufferedReader file = new BufferedReader(new FileReader("/Users/yuhaomao/Desktop/AES-CN/ubuntu_maven/example/test.csv"));
            String record;
            while ((record = file.readLine()) != null) {
                String[] result = record.split(",");
                result_list.add(result[0]);
                result_list.add(result[1]);
//                System.out.print(result_list);
            }
        } catch (Exception e) {
            //在命令行打印异常信息在程序中出错的位置及原因。
            e.printStackTrace();
        }
//        return result_list;
    }
}