+++
id = "thm-galois-abstract-equivalence"
kind = "theorem"
title = "The abstract equivalence theorem"
order = 1382
lean = ["CategoryTheory.PreGaloisCategory.functorToContAction", "CategoryTheory.PreGaloisCategory.functorToAction_full", "CategoryTheory.PreGaloisCategory.exists_lift_of_continuous"]
uses = ["def-galois-category", "lem-galois-action-continuous", "lem-galois-aut-profinite", "lem-galois-axioms", "lem-galois-object-exists", "lem-galois-transitive"]
+++
Let $(\mathcal C,F)$ be a Galois category and
$G=\operatorname{Aut}(F)$. Then $\mathcal C\to \text{finite-}G\text{-}\mathbf{Sets}$, $X\mapsto F(X)$ with the induced
$G$-action, is an equivalence of categories.
