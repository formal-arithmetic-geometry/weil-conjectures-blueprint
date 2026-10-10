+++
id = "p-product"
kind = "theorem"
title = "The central--geometric product"
order = 2523
tags = ["latex:proposition"]
uses = ["d-monodromy", "lem-ag-closure-commutators", "lem-ag-closure-semisimple", "lem-ag-faithful-semisimple-lie-central-radical", "lem-ag-homomorphism-image-closed", "lem-ag-lie-centre", "lem-ag-lie-stable-subspace", "lem-wf-algebraic-component-cosets", "lem-wf-same-lie-closed-subgroup"]
lean = ["AlgebraicGeometry.GeneralLinearGroup.surjective_mulCenterIdentityComponent", "AlgebraicGeometry.GeneralLinearGroup.exists_mul_eq_of_containsCommutators", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.surjective_mul_center_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_mem_center_mul_mem_geometricMonodromy_eq"]
+++
For a semisimple represented degree datum ([d-monodromy]) over an
algebraically closed field $k$ of characteristic zero, the
identity components and center satisfy

$$
G^\circ=Z(G^\circ)^\circ H^\circ:
$$

the multiplication morphism $Z(G^\circ)^\circ\times_k H^\circ\to G^\circ$
is surjective, and every $g\in G^\circ(k)$ is a product $g=ch$ with
$c\in Z(G^\circ)^\circ(k)$ and $h\in H^\circ(k)$. More generally, the
same holds for closed subgroup schemes $H\subseteq G$ of
$\operatorname{GL}_n$ over such a $k$ such that $H$ contains the
commutators of $G$ and $k^n$ is a semisimple representation of
$G^\circ(k)$.

This applies to the Weil representation of a lisse Weil sheaf whose Weil
representation is semisimple.

## Proof

Throughout, $k$ is algebraically closed of characteristic zero; this is
used through Cartier's theorem (reducedness, and
[lem-wf-same-lie-closed-subgroup]) and through the group–Lie comparison
[lem-ag-lie-stable-subspace], [lem-ag-lie-centre].

*Reduction to the general version.* For a semisimple represented degree
datum ([d-monodromy]), $H\subseteq G$ are closed subgroup schemes of
$\operatorname{GL}_n$, $H$ contains the commutators of $G$ by
[lem-ag-closure-commutators], and $V=k^n$ is a semisimple
$G^\circ(k)$-module by [lem-ag-closure-semisimple]. So it suffices to
treat closed subgroup schemes $H\subseteq G$ of $\operatorname{GL}_n$
such that $H$ contains the commutators of $G$ and $V$ is a semisimple
$G^\circ(k)$-module: $V=\bigoplus_iM_i$ with each $M_i$ a simple
$G^\circ$-module. In characteristic zero these group schemes are reduced
(Cartier), so they are matrix groups.

*The Lie algebra.* Set
$\mathfrak g=\operatorname{Lie}(G^\circ)\subseteq\operatorname{End}(V)$,
$\mathfrak h=\operatorname{Lie}(H^\circ)$ and $T=Z(G^\circ)^\circ$.
Apply [lem-ag-lie-stable-subspace] to the connected group $G^\circ$ and
its inclusion $r:G^\circ\to\operatorname{GL}(V)$, whose differential is
the inclusion $dr:\mathfrak g\subseteq\operatorname{End}(V)$: a subspace
of $V$ is $G^\circ$-stable if and only if it is $\mathfrak g$-stable.
Hence each $M_i$ is $\mathfrak g$-stable, and its $\mathfrak g$-stable
subspaces are exactly its $G^\circ$-stable subspaces, so $M_i$ has no
$\mathfrak g$-stable subspaces other than $0$ and $M_i$. Thus the Lie
representation $\mathfrak g\subseteq\operatorname{End}(V)$ is semisimple,
and it is faithful because it is an inclusion. By
[lem-ag-faithful-semisimple-lie-central-radical],
$\mathfrak g=Z(\mathfrak g)+[\mathfrak g,\mathfrak g]$. Since $H$
contains the commutators of $G$, the Lie-inclusion step of
[lem-ag-closure-commutators], which uses only this property of the pair,
gives $[\mathfrak g,\mathfrak g]\subseteq\mathfrak h$, and
[lem-ag-lie-centre] gives $Z(\mathfrak g)=\operatorname{Lie}(T)$. (These
lemmas, and [lem-ag-lie-stable-subspace], [lem-wf-same-lie-closed-subgroup],
are written over $\overline{\mathbf Q}_\ell$; their proofs use only that
the field is algebraically closed of characteristic zero.) Hence

$$
\mathfrak g=Z(\mathfrak g)+[\mathfrak g,\mathfrak g]
           =Z(\mathfrak g)+\mathfrak h
           =\operatorname{Lie}(T)+\operatorname{Lie}(H^\circ).
$$

Here the middle equality holds because
$[\mathfrak g,\mathfrak g]\subseteq\mathfrak h\subseteq\mathfrak g$.

*The product.* The group $H^\circ$ is connected and contains $1$, and
$H\subseteq G$, so $H^\circ\subseteq G^\circ$
([lem-wf-algebraic-component-cosets]); the central subgroup $T$ of
$G^\circ$ commutes with it. The product $T\times H^\circ$, embedded
block-diagonally in $\operatorname{GL}(V\oplus V)$, is a closed matrix
group, and the multiplication map

$$
\mu:T\times H^\circ\to G^\circ,\qquad(t,h)\mapsto th,
$$

is a morphism of varieties and, since $T$ is central, a group
homomorphism: $tht'h'=tt'hh'$. By [lem-ag-homomorphism-image-closed] its
image $K=TH^\circ$ is a closed subgroup of $G^\circ$. It is connected:
$T$ and $H^\circ$ are connected and contain $1$, so both lie in the
identity component $K^\circ$ ([lem-wf-algebraic-component-cosets]),
and hence $K=TH^\circ\subseteq K^\circ$. Its Lie algebra is a subspace
containing $\operatorname{Lie}(T)$ and $\operatorname{Lie}(H^\circ)$,
hence equals $\mathfrak g$. Thus [lem-wf-same-lie-closed-subgroup]
gives $K=G^\circ$. On $k$-points this says that every $g\in G^\circ(k)$ is
a product $g=ch$ with $c\in T(k)$ and $h\in H^\circ(k)$. Since $k$ is
algebraically closed, the $k$-points of $G^\circ$ are its closed points
and are dense, and the closed image of $\mu$ contains them all; so the
multiplication morphism $T\times_kH^\circ\to G^\circ$ is surjective.
