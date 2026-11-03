+++
kind  = "proof"
of    = "lem-ag-equal-dimension-subgroup"
+++
By Cartier's theorem [lem-ag-cartier-reduced], $G$ and $J$ are reduced.
Since $G$ is connected, it equals its identity component, which is
irreducible by [lem-wf-algebraic-component-cosets].

The closed subset $J$ of the finite-type scheme $G$ has finitely many
irreducible components, and its dimension is the maximum of their
dimensions, so some irreducible component $J_1$ of $J$ has
$\dim J_1=\dim G$. Suppose $J_1\subsetneq G$. The dimension of $J_1$ is
the maximum of the dimensions of $J_1\cap U$ over a finite affine open
cover of $G$, so there is an affine open $U\subseteq G$ with
$\dim(J_1\cap U)=\dim J_1$. Being open in the irreducible reduced scheme
$G$, $U$ is an irreducible affine variety. If $J_1\cap U=U$, the closed
set $J_1$ would contain the dense open $U$ of $G$ and hence equal $G$;
so $J_1\cap U\subsetneq U$, and [lem-wf-affine-dimension-drop] gives
$\dim(J_1\cap U)\le\dim U-1\le\dim G-1$, a contradiction. Hence the
closed subset $J_1$ equals $G$, and $G=J_1\subseteq J\subseteq G$ as
sets. Since $J$ and $G$ are reduced closed subschemes of $G$ with the
same underlying set, $J=G$.

For the complement, the irreducible closed matrix group $G$ is closed in
the affine variety $\operatorname{GL}(V)$, hence an irreducible affine
variety, and the same argument with $U=G$ applies directly.
