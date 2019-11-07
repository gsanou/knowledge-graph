import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.formats.FunctionalSyntaxDocumentFormat;
import org.semanticweb.owlapi.model.*;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;


/////////////////////////////////////////////////////创建节点
//public class test
//{
//    public static void main(String[] args) {
//        OWLOntologyManager man = OWLManager.createOWLOntologyManager();
//        OWLOntology o;
//        try {
//            o = man.createOntology();
//            System.out.println(o);
//            } catch (OWLOntologyCreationException e) {
//            e.printStackTrace();
//            }
//        }
//}





/////////////////////////////////////////////////////读取文件 从本地
//public class test
//{
//    public static void main(String[] args) throws OWLOntologyCreationException
//    {
//        OWLOntologyManager man = OWLManager.createOWLOntologyManager();
//        File file = new File("/Users/yuhaomao/Desktop/AES-CN/ubuntu_maven/pizza.owl.xml");
//        OWLOntology o = man.loadOntologyFromOntologyDocument(file);
//        System.out.println(o);
//    }
//}

/////////////////////////////////////////////////////读取文件 从网上
//public class test
//{
//    public static void main(String[] args) throws OWLOntologyCreationException
//    {
//        OWLOntologyManager man = OWLManager.createOWLOntologyManager();
//        IRI pizzaontology = IRI.create("http://protege.stanford.edu/ontologies/pizza/pizza.owl");
//        OWLOntology o = man.loadOntology(pizzaontology);
//        System.out.println(o);
//    }
//}

/////////////////////////////////////////////////////保存文件
//public class test
////{
//    public static void main(String[] args) throws OWLOntologyCreationException, FileNotFoundException, OWLOntologyStorageException {
//        OWLOntologyManager man = OWLManager.createOWLOntologyManager();
//        File fileout = new File("/Users/yuhaomao/Desktop/pizza.func.owl");
//        IRI pizzaontology = IRI.create("http://protege.stanford.edu/ontologies/pizza/pizza.owl");
//        OWLOntology o = man.loadOntology(pizzaontology);
//        man.saveOntology(o, new FunctionalSyntaxDocumentFormat(),
//            new FileOutputStream(fileout));
//    }
//}
