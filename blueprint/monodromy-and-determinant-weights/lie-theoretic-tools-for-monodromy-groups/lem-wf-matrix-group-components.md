+++
id = "lem-wf-matrix-group-components"
kind = "lemma"
title = "Components of a closed matrix group"
order = 4031
uses = ["def-wf-algebraic-components", "lem-wf-same-lie-closed-subgroup"]
+++
Let $G\subseteq\operatorname{GL}(V)$ be a closed reduced matrix
group over $\overline{\mathbf Q}_\ell$. Its connected component
$G^\circ$ is irreducible, closed, open, and normal. The irreducible
and connected components of $G$ are exactly the disjoint cosets
$gG^\circ$ for $g\in G(\overline{\mathbf Q}_\ell)$; in particular
there are finitely many of them.

## Proof

The identity component and the finiteness of the connected-component
set are those of [def-wf-algebraic-components].
As in the proof of
[lem-wf-same-lie-closed-subgroup], translation carries a smooth
point of $G$ to the identity and then to every point. Thus $G$ is
smooth. Its local rings are regular domains, so two distinct
irreducible components cannot meet. Since there are finitely many
irreducible components, each is open and closed.

Let $C$ be the irreducible component containing the identity. It is
connected. Conversely, the connected component $G^\circ$ is a
connected subset containing the identity, hence lies in $C$;
therefore $G^\circ=C$. The first assertion of
[lem-wf-same-lie-closed-subgroup] also gives directly that this
connected matrix group is irreducible. Multiplication and inversion
send $C$ to irreducible components containing the identity, so
$CC\subseteq C$ and $C^{-1}=C$; hence $C=G^\circ$ is a subgroup.
Conjugation by any $g\in G$ preserves connectedness and fixes the
identity, so it preserves $G^\circ$; thus $G^\circ$ is normal.

Every irreducible component contains a closed point, and over the
algebraically closed field such a point is in
$G(\overline{\mathbf Q}_\ell)$. Translation by that point carries
$G^\circ$ onto the component containing the point. Hence all
components are the stated cosets. They are disjoint cosets and are
open and closed, so they are also exactly the connected components.
