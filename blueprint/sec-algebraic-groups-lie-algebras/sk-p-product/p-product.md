+++
id = "p-product"
kind = "theorem"
title = "The central--geometric product"
order = 2714
tags = ["latex:proposition"]
uses = ["d-monodromy", "lem-ag-central-radical-quotient", "lem-ag-closure-commutators", "lem-ag-closure-semisimple", "lem-ag-commuting-product-closed", "lem-ag-connected-group-central-radical", "lem-ag-lie-centre", "lem-wf-algebraic-component-cosets", "lem-wf-same-lie-closed-subgroup"]
+++
For a semisimple represented degree datum ([d-monodromy]), the
identity components and center satisfy

$$
G^\circ=Z(G^\circ)^\circ H^\circ.
$$

This applies to the Weil representation of a lisse Weil sheaf whose Weil
representation is semisimple.

## Proof

Use the defining representation of [d-monodromy]. By
[lem-ag-closure-semisimple], $V$ is a semisimple $G^\circ$-module; it is
faithful because $G^\circ\subseteq\operatorname{GL}(V)$. Set
$\mathfrak g=\operatorname{Lie}(G^\circ)$,
$\mathfrak h=\operatorname{Lie}(H^\circ)$ and $T=Z(G^\circ)^\circ$.
By [lem-ag-connected-group-central-radical], $\mathfrak g$ has central
radical, so [lem-ag-central-radical-quotient], [lem-ag-closure-commutators]
and [lem-ag-lie-centre] give

$$
\mathfrak g=Z(\mathfrak g)+[\mathfrak g,\mathfrak g]
           =Z(\mathfrak g)+\mathfrak h
           =\operatorname{Lie}(T)+\operatorname{Lie}(H^\circ).
$$

The group $H^\circ$ is connected and contains $1$, and $H\subseteq G$, so
$H^\circ\subseteq G^\circ$ ([lem-wf-algebraic-component-cosets]); the
central subgroup $T$ commutes with it. By
[lem-ag-commuting-product-closed], $K=TH^\circ$ is a connected closed
subgroup of $G^\circ$. Its Lie algebra is a subspace containing
$\operatorname{Lie}(T)$ and $\operatorname{Lie}(H^\circ)$, hence equals
$\mathfrak g$. Thus [lem-wf-same-lie-closed-subgroup] gives $K=G^\circ$.
