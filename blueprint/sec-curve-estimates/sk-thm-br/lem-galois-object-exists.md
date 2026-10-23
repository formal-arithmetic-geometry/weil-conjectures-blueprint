+++
id = "lem-galois-object-exists"
kind = "lemma"
title = "Galois objects dominate connected objects"
order = 1405
lean = ["CategoryTheory.PreGaloisCategory.exists_hom_from_galois_of_connected"]
uses = ["def-galois-category", "lem-galois-axioms"]
+++
Let $(\mathcal C,F)$ be a Galois category and $X$ a connected object.
Then there is a Galois object $Z$ and a morphism $Z\to X$. (The
construction: the symmetric group acts on the $n$-fold fibre power
$X^n$, and one takes a connected component whose fibre consists of tuples
of pairwise distinct elements.)
