import java.util.ArrayList;

import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.*;
import org.semanticweb.owlapi.vocab.OWL2Datatype;

import java.io.File;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class test_create{
    static OWLOntologyManager m = OWLManager.createOWLOntologyManager();
    static OWLDataFactory dataFactory = m.getOWLDataFactory();

    // The IRIs used here are taken from the OWL 2 Primer
    private static String base = "http://example.com/owl/families/";

    static OWLClass peopleClass = dataFactory.getOWLClass(IRI.create(base + "#people"));
    static OWLClass locationClass = dataFactory.getOWLClass(IRI.create(base + "#location"));
    static OWLClass companyClass = dataFactory.getOWLClass(IRI.create(base + "#company"));
    static OWLClass robotClass = dataFactory.getOWLClass(IRI.create(base + "#robot"));

    static OWLObjectProperty peoplerobot = dataFactory.getOWLObjectProperty(IRI.create(base + "#peoplerobot"));
    static OWLObjectProperty companyrobot = dataFactory.getOWLObjectProperty(IRI.create(base + "#companyrobot"));
    static OWLObjectProperty companylocation = dataFactory.getOWLObjectProperty(IRI.create(base + "#companylocation"));

    static OWLDataProperty CNname = dataFactory.getOWLDataProperty(IRI.create(base + "#cnname"));
    static OWLDataProperty ENname = dataFactory.getOWLDataProperty(IRI.create(base + "#enname"));
    static OWLDataProperty continent = dataFactory.getOWLDataProperty(IRI.create(base + "#continent"));
    static OWLDataProperty founded = dataFactory.getOWLDataProperty(IRI.create(base + "#founded"));
    static OWLDataProperty function = dataFactory.getOWLDataProperty(IRI.create(base + "#function"));

    static OWLDatatype stringDatatype = dataFactory.getOWLDatatype(OWL2Datatype.XSD_STRING.getIRI());
    static OWLDatatype doubleDatatype = dataFactory.getOWLDatatype(OWL2Datatype.XSD_DOUBLE.getIRI());
    public static Map<String,String> tem;

    public static String specialUnicode(String str){
        if (str.startsWith("\uFEFF")){
            str = str.replace("\uFEFF", "");
        }else if (str.endsWith("\uFEFF")){
            str = str.replace("\uFEFF","");
        }
        return str;
    }
    public static void solve(OWLOntologyManager m,OWLOntology ont,String filename) {
        ArrayList result = TestCsv.getList();
        Object List = null;
        List<String> keys = new ArrayList<String>();
        List<String> values = new ArrayList<String>();
        for (int i = 0; i < result.size(); i++) {
            String tmp = specialUnicode((String) result.get(i));
            if ((i & 1) != 1) {   //是偶数
                keys.add(tmp);
            } else {
                values.add((String) result.get(i));
            }
        }
        System.out.println(keys);
        System.out.println(values);

        Map<String, String> tem = listToMap(keys,values);
        System.out.println(tem);
        System.out.println(tem.get("CNname"));
        System.out.println(tem.get("continent"));
        System.out.println(tem.get("location"));

    }

    public static void create_node(OWLOntologyManager m, OWLOntology ont, String filename){
        System.out.println("done!");

    }

    public static<k,v>Map<k,v>listToMap(List<k>keys,List<v>values){
        return keys.stream().collect(Collectors.toMap(key->key,key->values.get(keys.indexOf(key))));
    }
    public static void main(String[] args) throws OWLOntologyCreationException, OWLOntologyStorageException{
        IRI ontologyIRI = IRI.create("http://example.com/owl/example/");
        OWLOntology ont = m.createOntology(ontologyIRI);
        String path = "/Users/yuhaomao/Desktop/AES-CN/ubuntu_maven/example";
        File file = new File(path);

        String[] filelist = file.list();
        for(String key : filelist){
            File readfile = new File(path + "/" + key);
            String[] flist = readfile.list();
//            for(String fname : flist){
//                solve(m, ont, readfile.getPath() + "/" + fname);
//            }
        }
        solve(m, ont, "/Users/yuhaomao/Desktop/AES-CN/ubuntu_maven/test.csv");
        create_node(m, ont, "file:/Users/yuhaomao/Desktop/AES-CN/ubuntu_maven/myh_robot.owl");
//        OWLNamedIndividual site = dataFactory.getOWLNamedIndividual(IRI.create(base + "#" + tem.get("CNname")));
//        OWLLiteral literal = dataFactory.getOWLLiteral(tem.get("continent"), stringDatatype);
//        // Create the property assertion and add it to the ontology
//        OWLAxiom ax = dataFactory.getOWLDataPropertyAssertionAxiom(CNname, site,literal);
//        m.addAxiom(ont, ax);
//
//        m.saveOntology(ont,IRI.create("file:/Users/yuhaomao/Desktop/AES-CN/ubuntu_maven/myh_robot.owl"));

        System.out.println("done!");

    }

}

//public class test_create {
//    public static void main(String[] args) {
//        ArrayList result = TestCsv.getList();
//        System.out.println(result);
//    }
//}