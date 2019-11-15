import org.eclipse.rdf4j.model.vocabulary.OWL;
import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.formats.FunctionalSyntaxDocumentFormat;
import org.semanticweb.owlapi.model.*;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.util.OWLEntityRemover;

import javax.swing.plaf.basic.BasicInternalFrameTitlePane;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.Set;

import static junit.framework.Assert.assertTrue;


/////////////////////////////////////////////////////创建ontology
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
//{
//    public static void main(String[] args) throws OWLOntologyCreationException, FileNotFoundException, OWLOntologyStorageException {
//        OWLOntologyManager man = OWLManager.createOWLOntologyManager();
//        File fileout = new File("/Users/yuhaomao/Desktop/pizza.func.owl");
//        IRI pizzaontology = IRI.create("http://protege.stanford.edu/ontologies/pizza/pizza.owl");
//        OWLOntology o = man.loadOntology(pizzaontology);
//        man.saveOntology(o, new FunctionalSyntaxDocumentFormat(),
//            new FileOutputStream(fileout));
//    }
//}

/////////////////////////////////////////////////////Add Declaration Axiom
//public class test
//{
//    public static void main(String[] args) throws OWLOntologyCreationException, FileNotFoundException, OWLOntologyStorageException {
//        IRI IOR = IRI.create("http://owl.api");
//        OWLOntologyManager man = OWLManager.createOWLOntologyManager();
//        OWLOntology o = man.createOntology(IOR);
//        OWLDataFactory df = o.getOWLOntologyManager().getOWLDataFactory();
//        OWLClass person = df.getOWLClass(IOR);
//        OWLDeclarationAxiom da = df.getOWLDeclarationAxiom(person);
//        o.addAxiom(da);
//        System.out.println("qqqqqq");
//        System.out.println(o);
//    }
//}

/////////////////////////////////////////////////////添加两个individual 然后添加关系，保存到本地
//public class test
//{
//    public static void main(List<String> args) throws OWLOntologyCreationException, FileNotFoundException, OWLOntologyStorageException {
//        String individual1 = args.get(0);
//        String individual2 = args.get(1);
//        String relationship1 = args.get(2);
//        String class_individual = args.get(3);
//        OWLOntologyManager man = OWLManager.createOWLOntologyManager();
//        OWLDataFactory datafactory=man.getOWLDataFactory();
//        String base = "http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17";
//        File file = new File("/Users/yuhaomao/Desktop/new_robot.owl");
//        File fileout = new File("/Users/yuhaomao/Desktop/pizza.func.owl");
//        OWLOntology o = man.loadOntologyFromOntologyDocument(file);
////        System.out.println(o);
//        OWLIndividual indiv = datafactory.getOWLNamedIndividual(base + "护士助手");
//        System.out.println(indiv);
//        OWLIndividual xiaoming = datafactory.getOWLNamedIndividual(IRI.create(base + "#" + individual1));
//        OWLIndividual xiaoxiaoming = datafactory.getOWLNamedIndividual(IRI.create(base + "#"+ individual2));
//        OWLObjectProperty fuzi = datafactory.getOWLObjectProperty(IRI.create(base + "#" + relationship1));
//        OWLAxiom assertion = datafactory.getOWLObjectPropertyAssertionAxiom(fuzi,xiaoming,xiaoxiaoming);
//
//        OWLClass classname =datafactory.getOWLClass(IRI.create("http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17#"+ class_individual));
//        OWLAxiom addindividualclass = datafactory.getOWLClassAssertionAxiom(classname,xiaoming);
//        AddAxiom addAxiomchange1 = new AddAxiom(o, addindividualclass);
//        man.applyChange(addAxiomchange1);
//        AddAxiom addAxiomchange = new AddAxiom(o, assertion);
//        man.applyChange(addAxiomchange);
//        man.saveOntology(o, new FunctionalSyntaxDocumentFormat(),
//                new FileOutputStream(file));
//    }
//}

/////////////////////////////////////////////////////删除individuals
public class test
{
    public static void main(String[] args) throws OWLOntologyCreationException {
        OWLOntologyManager man = OWLManager.createOWLOntologyManager();
        OWLDataFactory datafactory=man.getOWLDataFactory();
        String base = "http://example.com/owl/families/";
        File file = new File("/Users/yuhaomao/Desktop/new_robot.owl");
        OWLOntology o = man.loadOntologyFromOntologyDocument(file);
        base = "http://www.semanticweb.org/yuhaomao/ontologies/2019/9/untitled-ontology-17#";
        OWLIndividual labID =  datafactory.getOWLNamedIndividual(base + "xiaoming");
        OWLObjectProperty property = datafactory.getOWLObjectProperty(base + "fuzi");
        OWLIndividual value = datafactory.getOWLNamedIndividual(base + "xiaoxiaoming");
//        OWLObjectPropertyAssertionAxiom assertion = datafactory.getOWLObjectPropertyAssertionAxiom(property,value,labID);
//        AddAxiom addAxiomchange = new AddAxiom(o, assertion);
//        man.applyChange(addAxiomchange);
        OWLObjectPropertyAssertionAxiom assertion = datafactory.getOWLObjectPropertyAssertionAxiom(property,value,labID);
        AddAxiom addAxiomchange = new AddAxiom(o, assertion);
        OWLEntityRemover remover = new OWLEntityRemover(o);
        value.accept(remover);
        man.applyChange(remover());
//        java.util.Set<OWLEntity> ref = assertion.accept(remover);
//        for (OWLEntity ent : ref){
//            System.out.println(ent);
//            ent.accept(remover);
//        }
//        man.applyChanges(remover.getChangers());
    }
}


