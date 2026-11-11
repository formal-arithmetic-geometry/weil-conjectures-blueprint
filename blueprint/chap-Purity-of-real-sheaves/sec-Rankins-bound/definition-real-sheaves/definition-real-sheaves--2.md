+++
id = "definition-real-sheaves--2"
kind = "lemma"
title = "Real sheaves (2)"
name_showing = false
order = 1156002
aliases = ["bp-r354-2"]
lean = ["AlgebraicGeometry.WeilGroup.IsReal.conj_sum_map_pow_localEigenvalues", "AlgebraicGeometry.WeilSheaf.IsReal.conj_map_trace_frobeniusEnd_pow"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-perfect-complexes-geometric-point--6", "definition-real-sheaves--1"]
+++
Let $\mathcal G$ be an $\iota$-real Weil sheaf on a scheme $X_0/\Fq$.
For every closed point $x$ and every integer $n\ge0$,

$$
\overline{\iota\operatorname{Tr}(\operatorname{Frob}_x^n\mid\mathcal G_{\bar x})}
=\iota\operatorname{Tr}(\operatorname{Frob}_x^n\mid\mathcal G_{\bar x}).
$$

In the representation formulation on a geometrically connected curve, let
$M_x$ be the multiset of complex local eigenvalues of an $\iota$-real
finite-dimensional Weil-group representation. Then for every $n\ge0$,

$$
\overline{\sum_{\alpha\in M_x}\alpha^n}
=\sum_{\alpha\in M_x}\alpha^n.
$$
