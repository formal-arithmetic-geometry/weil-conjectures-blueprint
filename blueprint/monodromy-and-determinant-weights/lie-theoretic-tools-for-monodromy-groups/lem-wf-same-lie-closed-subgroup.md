+++
id = "lem-wf-same-lie-closed-subgroup"
kind = "lemma"
title = "Connected matrix groups and equal Lie algebras"
order = 4030
uses = ["def-wf-algebraic-components", "def-wf-lie-algebra-derivation"]
+++
Let $K$ be a connected closed matrix group over
$\overline{\mathbf Q}_\ell$. Then $K$ is irreducible. Moreover,
if $L\subseteq K$ is a closed algebraic subgroup and
$\operatorname{Lie}(L)=\operatorname{Lie}(K)$, then $L=K$.

## Proof

A reduced finite-type variety over the characteristic-zero field
$\overline{\mathbf Q}_\ell$ has a nonempty smooth locus by the
elementary Jacobian criterion. In an algebraic group, translation
carries a smooth point to the identity and then the identity to every
other point. Thus the reduced closed matrix groups $K$ and $L$
are smooth. In particular every local ring of $K$ is regular, hence
is an integral domain. If two distinct irreducible components of
$K$ met at a point $x$, the local ring $\mathcal O_{K,x}$ would
have at least two minimal prime ideals, one from each component, and
could not be a domain. Therefore the finitely many irreducible
components of $K$ are pairwise disjoint; each is consequently both
open and closed.

Let $K_1$ be the unique irreducible component containing the identity.
The image of the irreducible variety $K_1\times K_1$ under
multiplication is irreducible and contains the identity, so its closure
lies in the unique component $K_1$. Hence $K_1K_1\subseteq K_1$.
Inversion sends $K_1$ to an irreducible component containing the
identity, hence to $K_1$. Thus $K_1$ is a subgroup. Translation by
$g\in K$ sends $K_1$ onto the irreducible component containing
$g$. Since the components are open and closed, connectedness in
[def-wf-algebraic-components] forces $K=K_1$; thus $K$ is
irreducible.

Finally smoothness and the tangent-space definition in
[def-wf-lie-algebra-derivation] gives

$$
\dim K=\dim\operatorname{Lie}(K),\qquad
\dim L=\dim\operatorname{Lie}(L).
$$

Equality of Lie algebras gives $\dim L=\dim K$. A proper closed
subset of the irreducible variety $K$ has smaller dimension, so
$L=K$.
