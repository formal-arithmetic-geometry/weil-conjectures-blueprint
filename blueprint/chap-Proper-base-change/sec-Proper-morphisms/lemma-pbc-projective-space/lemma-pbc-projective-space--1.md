+++
id = "lemma-pbc-projective-space--1"
kind = "lemma"
title = "Products of projective lines"
name_showing = false
order = 395001
aliases = ["bp-r120-1"]
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_projectiveLinePowProj"]
uses = ["definition-torsion-pbc-property"]
+++
Let $\Lambda$ be a commutative ring that is torsion as an abelian group,
and suppose that $\mathrm{PBC}_\Lambda(\mathbf P^1_T\to T)$ holds for every
scheme $T$. For a scheme $S$, define the tower

$$
X_0=S,\qquad X_{n+1}=\mathbf P^1_{X_n},
$$

with $p_0=\mathrm{id}_S$ and $p_{n+1}$ the composite
$X_{n+1}\to X_n\xrightarrow{p_n}S$.
Then $\mathrm{PBC}_\Lambda(p_n)$ holds for every scheme $S$ and every
$n\geq0$.
