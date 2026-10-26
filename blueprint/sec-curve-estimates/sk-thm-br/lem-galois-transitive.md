+++
id = "lem-galois-transitive"
kind = "lemma"
title = "The action of $\\operatorname{Aut}(F)$ is transitive"
order = 1381
lean = ["CategoryTheory.PreGaloisCategory.FiberFunctor.isPretransitive_of_isConnected"]
uses = ["def-galois-category", "lem-galois-aut-profinite", "lem-galois-axioms", "lem-galois-object-exists"]
+++
Let $(\mathcal C,F)$ be a Galois category, $G=\operatorname{Aut}(F)$ and
$X$ connected. Then $G$ acts transitively on $F(X)$.
