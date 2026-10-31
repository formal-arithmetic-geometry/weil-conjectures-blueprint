+++
id = "def-wf-arithmetic-monodromy-extension"
kind = "definition"
title = "Arithmetic monodromy extension"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.frobeniusConj", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.frobeniusAction", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.ArithmeticMonodromyExtension", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.arithmeticMonodromyExtensionHom"]
order = 3941
uses = ["d-monodromy", "lem-wf-conjugation-geometric-monodromy"]
+++
Let $\rho$ be a represented degree datum ([d-monodromy]) with geometric
monodromy group $H$ and $F=\rho(s)$, and let $\alpha(h)=FhF^{-1}$ be
the automorphism of $H$ furnished by
[lem-wf-conjugation-geometric-monodromy]. Define the locally
finite-type group scheme

$$
G_{\mathrm{arith}}(\rho)=
\bigsqcup_{m\in\mathbf Z}H\times\{m\},
\qquad (h,m)(h',n)=(h\alpha^m(h'),m+n),
$$

a disjoint union of finite-type pieces, with *degree map*

$$
\deg_G:G_{\mathrm{arith}}(\rho)(k)
\longrightarrow\mathbf Z,\qquad (h,m)\longmapsto m.
$$

On $k$-points, $G_{\mathrm{arith}}(\rho)(k)=H(k)\rtimes_\alpha\mathbf Z$.
The map to matrices is $(h,m)\mapsto hF^m$. This map need not be
injective: the integer in the second coordinate is retained because it
records the degree even when two degree components have the same
matrix image, for instance when $F$ has finite order.
