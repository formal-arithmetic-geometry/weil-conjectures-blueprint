+++
id = "fin2-lem-constructibility-finite-etale-descent"
kind = "lemma"
title = "Descent of constructibility along finite étale surjections"
order = 5178
lean = ["AlgebraicGeometry.Etale.isConstructible_of_isConstructible_pullback_finiteEtale"]
uses = ["sbc-def-coefficient-conventions", "lem-fin-finite-morphism"]
+++
Let $\sigma:S'\to S$ be a finite étale surjective morphism with $S'$ and $S$
of finite type over $k$, and let $G$ be a $\Lambda$-sheaf on $S_{\Et}$. If
$\sigma^{-1}G$ is constructible, then so is $G$; and $\sigma^{-1}G=0$
implies $G=0$.

## Proof

Consider the unit $G\to\sigma_*\sigma^{-1}G$ of the adjunction: at a
geometric point $\bar s$ of $S$ the target stalk is, by the finite stalk
formula, the finite product of the stalks
$(\sigma^{-1}G)_{\bar s'}=G_{\bar s}$ over the geometric points $\bar s'$ of
the finite fibre $S'_{\bar s}$, and the unit is the diagonal: injective,
since $\sigma$ is surjective.

The morphism $\sigma$ is finite, so $\sigma_*$ is exact, and the
constructible $\sigma^{-1}G$ pushes forward to the constructible
$\sigma_*\sigma^{-1}G$ by [lem-fin-finite-morphism]. The sheaf $G$ is the
image of the unit, hence a submodule of a constructible sheaf, so
constructible by the weak-Serre closure.

For the zero clause, $\sigma^{-1}G=0$ gives $\sigma_*\sigma^{-1}G=0$, and
the injection $G\hookrightarrow\sigma_*\sigma^{-1}G$ gives $G=0$.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-inverse-image, def:weil-pbc-direct-image, def:weil-pbc-constructible-complexes, lem:weil-pbc-finite-stalk-formula, lem:weil-pbc-finite-direct-image-exact, lem:weil-pbc-constructible-serre
