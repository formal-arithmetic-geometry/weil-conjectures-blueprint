+++
id = "proposition-properties-trace--4"
kind = "proposition"
title = "Termwise trace"
order = 895005
aliases = ["bp-r270-4"]
lean = ["CochainComplex.trace_f_zero", "DerivedCategory.trace_Qh_map_quotient_map"]
uses = ["definition-categorical-trace"]
+++
Let $\mathcal C$ be a preadditive braided monoidal category with a zero
object and tensor product additive in each variable. Assume that the
graded tensor products and their iterated associativity comparisons
exist, and that tensoring preserves zero objects. Let $P^\bullet$ vanish
outside $[a,b]$, with each $P^i$ admitting a right dual. Give $P^\bullet$
its termwise right dual and use the Koszul braiding. For a chain
endomorphism $v^\bullet$, the degree-zero component of its trace,
identified with an endomorphism of $\mathbf 1_{\mathcal C}$, is

$$
\operatorname{tr}(v^\bullet)^0
=\sum_{i=a}^b(-1)^i\operatorname{tr}(v^i\mid P^i).
$$

For passage to the derived category, let $\mathcal C$ be Grothendieck
abelian and monoidal closed, with functorial flat resolutions and a
derived category. Write $H$ for the quotient from complexes to the
homotopy category and $Q_h$ for its localization to $D(\mathcal C)$.
Assume that the braiding of $D(\mathcal C)$ is compatible with the
Koszul braiding through the lax monoidal structure of $Q_h$ on K-flat
objects. If $Q_hH(P^\bullet)$ is equipped with any right dual, then

$$
\operatorname{tr}(Q_hH(v^\bullet))
=\epsilon^{-1}\circ Q_hH(\operatorname{tr}(v^\bullet))\circ\epsilon,
$$

where $\epsilon:\mathbf 1_{D(\mathcal C)}\xrightarrow{\sim}
Q_h(\mathbf 1_{K(\mathcal C)})$ is the unit isomorphism.
