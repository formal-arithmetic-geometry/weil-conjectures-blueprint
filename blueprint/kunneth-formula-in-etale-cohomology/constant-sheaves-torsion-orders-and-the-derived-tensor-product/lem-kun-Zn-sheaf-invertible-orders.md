+++
id = "lem-kun-Zn-sheaf-invertible-orders"
kind = "lemma"
title = "Modules over $\\mathbf Z/n\\mathbf Z$ have invertible orders"
order = 6022
lean = ["AlgebraicGeometry.Etale.hasOrdersInvertible_of_zmod"]
uses = ["def-kun-torsion-invertible"]
+++
Let $K$ be a field and $n\in I_K$ an integer invertible in $K$
[def-kun-torsion-invertible]. For every scheme $T$ over $K$, every sheaf of
$\mathbf Z/n\mathbf Z$-modules on the small étale site of $T$ has orders
invertible in $K$.

## Proof

Let $F$ be a sheaf of $\mathbf Z/n\mathbf Z$-modules on $T_{\Et}$. The ring
$\mathbf Z/n\mathbf Z$ is annihilated by $n$, so multiplication by $n$ is
the zero endomorphism of $F$: every section of $F$, hence every element of
every geometric stalk, is killed by $n$. As $n\in I_K$, the condition
defining orders invertible in $K$ is satisfied.

Unresolved dependencies: def:weil-pbc-etale-site, def:weil-pbc-etale-sheaves
