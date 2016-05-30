#!/usr/bin/env jython
# -*- coding: utf-8 -*-

# import edu.stanford.nlp.simple.*;

from edu.stanford.nlp.simple import Document

#
# public class SimpleCoreNLPDemo {
#     public static void main(String[] args) {
#         // Create a document. No computation is done yet.
#         Document doc = new Document("add your text here! It can contain multiple sentences.");

doc = Document("Here is a sentence. And another one.")

print("\n\n\nErgebnis:\n\n")

#         for (Sentence sent : doc.sentences()) {  // Will iterate over two sentences
for sent in doc.sentences():
    print(sent)
    print("Second word in this sentence: " + sent.word(1))
    print("Second lemma in this sentence: " + sent.lemma(1))
    print("Parse: " + sent.parse().toString())

#             // We're only asking for words -- no need to load any models yet
#             System.out.println("The second word of the sentence '" + sent + "'is " + sent.word(1));
#             // When we ask for the lemma, it will load and run the part of speech tagger
#             System.out.println("The third lemma of the sentence '" + sent + "' is " + sent.lemma(2));
#             // When we ask for the parse, it will load and run the parser
#             System.out.println("The parse of the sentence '" + sent + "' is " + sent.parse());
#             // ...
#         }
#     }
# }
