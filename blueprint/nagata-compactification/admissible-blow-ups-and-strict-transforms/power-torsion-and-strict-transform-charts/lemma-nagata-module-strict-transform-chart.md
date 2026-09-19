+++
id = "lemma-nagata-module-strict-transform-chart"
kind = "lemma"
title = "Affine formula for a module strict transform"
order = 333
uses = ["def-nagata-module-strict-transform", "def-nagata-power-torsion"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $A\to B$ be a ring map, let $I\subseteq A$ be an ideal, let $a\in I$,
and let $\mathcal F$ on $\operatorname{Spec}(B)$ correspond to the
$B$-module $M$. For the induced morphism
$\operatorname{Spec}(B)\to\operatorname{Spec}(A)$ and the blow-up of $I$,
on the $a$-chart the
strict transform corresponds to

$$
\frac{M\otimes_AA[I/a]}
{a\text{-power torsion}}.
$$

## Proof

Pullback of a quasi-coherent module on an affine morphism is tensor product.
Sections supported on the exceptional closed subset are exactly the elements
killed by a power of its local equation $a$.
