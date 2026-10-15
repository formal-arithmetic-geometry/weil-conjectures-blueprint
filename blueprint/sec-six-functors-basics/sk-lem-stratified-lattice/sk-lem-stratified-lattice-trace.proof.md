+++
kind  = "proof"
of    = "det-lem-stratified-lattice-trace"
+++
*Local computation.* All assertions are local on $S$ for the pro-étale topology. Since $p$ is
finite étale, after an étale (hence pro-étale) cover of $S$ it splits: $V=\coprod_{k=1}^dS$.
Then $p_*p^*L=L^{\oplus d}$ and $\Tr$ is the sum map $L^{\oplus d}\to L$; $p_*M_0=M_1\oplus\dots\oplus M_d$
with $M_k\subseteq L$ lattices; so $L_0=M_1+\dots+M_d$.

Refine further so that $L\cong E_S^r$. By [det-lem-stratified-lattice-scheme] (1), each $M_k$
corresponds to a locally constant function to the discrete set of lattices in $E^r$; after a
common refinement of the cover by open and closed pieces, every $M_k$ is the constant sheaf of
a lattice $\Lambda_k\subseteq E^r$. Then $L_0$ is the constant sheaf of
$\Lambda_1+\dots+\Lambda_d$, a finitely generated torsion-free, hence free, $\cO_E$-module
containing $\Lambda_1$, which spans $E^r$; so it is a lattice of rank $r$. Hence locally
$L_0\cong\cO_{E}^r\otimes\cO_{E,S}$ is free and $L_0[1/\ell]=E^r_S=L$. Since the image of a map of
sheaves is formed locally, these local descriptions glue: $L_0$ is lisse over $\cO_{E,S}$ and
$L_0[1/\ell]=L$ (inverting $\ell$ is exact and commutes with restriction).

*Stratification.* Let $p\colon V\to X$ be quasi-compact, separated, étale and surjective, $X$
Noetherian. By \stacks{07RY} and \stacks{07RZ} (generic finiteness of a quasi-finite separated
morphism, applied with Noetherian induction), there is a finite stratification of $X$ by
locally closed subschemes $S$ such that $p_S\colon V\times_XS\to S$ is finite; it is étale and
surjective by base change. On each stratum apply the first part to $L|_S$, the finite étale
$p_S$ and $M_0|_{V\times_XS}$. The trace of the finite étale $p_S$ (locally the sum over the
sheets) is a morphism of $E_S$-modules $p_{S*}p_S^*L\to L$.
