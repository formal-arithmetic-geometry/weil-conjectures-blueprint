+++
id = "sk-p-central"
kind = "section"
title = "A positive central representative"
order = 2717
uses = ["sk-d-central", "sk-d-monodromy", "sk-i-restriction", "sk-p-geometry", "sk-p-product"]
+++
*Proposition (sketch).*

Every semisimple represented degree datum
admits admissible choices; the displayed
construction gives a positive central pair $(N,z)$ for every such choice.

## Proof

The finite component group from [sk-p-geometry] supplies $m>0$ with
$F^m\in G^\circ$. The factorization is supplied by [sk-p-product],
so choose the data of [sk-d-central]. Since $G^\circ$ is normal, all
conjugates of $c$ lie in its abelian center. Replacing a coset
representative by $g_i u$, $u\in G^\circ$, leaves its factor unchanged;
the factors commute. Left multiplication permutes the component cosets,
so conjugation by any $g\in G$ fixes their product $z$.
By [sk-i-restriction], every commutator in $G$ lies in $H$.
Thus each $g_i c g_i^{-1}$ has the same $H$-coset as $c$, namely
$HF^m$, and multiplication yields $z\in HF^{mr}$.
There is at least the identity coset, so $r>0$ and $N=mr>0$.

Uses: [sk-d-central], [sk-d-monodromy], [sk-i-restriction], [sk-p-geometry], [sk-p-product]
