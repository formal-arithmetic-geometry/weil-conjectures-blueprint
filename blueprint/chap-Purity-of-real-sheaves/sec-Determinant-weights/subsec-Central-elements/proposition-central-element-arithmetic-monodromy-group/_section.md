+++
id = "proposition-central-element-arithmetic-monodromy-group"
kind = "proposition"
title = "A central element of the arithmetic monodromy group"
order = 1141
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_isPositiveCentralPair", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.IsPositiveCentralPair.map"]
uses = ["definition-monodromy-groups", "lemma-normality-geometric-monodromy"]
+++
Let $V_1,\ldots,V_n$ be semisimple Weil representations and form the
monodromy groups $H\subseteq G$ of $V=\bigoplus_iV_i$, and let $s\in W(U_0)$
have degree one. There are an integer $N>0$ and $h\in H(\overline{\mathbf Q}_\ell)$ such
that

$$
z=h\,\rho(s)^N\in Z(G)(\overline{\mathbf Q}_\ell).
$$

The action of $z$ on each tensor construction on $V$ preserves every
$W(U_0)$-stable subquotient and is scalar on each simple subquotient.
