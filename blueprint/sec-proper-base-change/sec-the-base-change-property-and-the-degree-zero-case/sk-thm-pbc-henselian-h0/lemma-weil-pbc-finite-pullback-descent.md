+++
id = "lemma-weil-pbc-finite-pullback-descent"
kind = "lemma"
title = "Finite descent compatibility"
order = 1649
lean = ["AlgebraicGeometry.Etale.globalSectionsUpperStarMap_descent"]
uses = ["def-weil-pbc-finite-section-pullback", "lemma-weil-pbc-finite-pullback-composition"]
+++
Let $u:T'\to T$ be a morphism of schemes (in the applications finite
surjective) and $G$ an etale sheaf on $T$ (with values in $\mathcal A$ as in
[def-weil-pbc-finite-section-pullback]). Suppose $x'\in\Gamma(T',u^{-1}G)$ is
equipped with a descended section $x\in\Gamma(T,G)$, meaning $u^\sharp(x)=x'$
(more generally, $x$ and $x'$ may be morphisms from an arbitrary object $M$ of
$\mathcal A$ to the global sections). Then the same equality holds after
restriction to a closed fibre: for every commutative square $u\circ a=i\circ b$
as in [lemma-weil-pbc-finite-pullback-closed-fibre],

$$
a^\sharp(x')=\Gamma(\theta)\bigl(b^\sharp(i^\sharp(x))\bigr),
$$

with $\theta:b^{-1}i^{-1}G\cong a^{-1}u^{-1}G$ the square isomorphism.
