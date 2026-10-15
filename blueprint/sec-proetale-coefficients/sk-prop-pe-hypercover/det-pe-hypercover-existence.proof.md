+++
kind = "proof"
of = "det-pe-hypercover-existence"
+++
*1.* $\operatorname{Spec}D=\bigsqcup_j\operatorname{Spec}D_j$ is a finite disjoint union of
clopen pieces. Its closed points are the union of those of the pieces, hence closed; every
point specializes only inside its piece, hence to exactly one closed point; and the local
rings at closed points are those of the $D_j$, strictly henselian. Its space of components
is the finite disjoint union of the $\pi_0(\operatorname{Spec}D_j)$; the closure of an open
subset is computed piecewise, so extremal disconnectedness is preserved.

*2.* By [det-pe-wcb-cover], $V$ has a covering by maps
$\operatorname{Spec}D_i\to\operatorname{Spec}B_i\subset V$ with $\operatorname{Spec}B_i$
ranging over all affine opens and $B_i\to D_i$ faithfully flat. As $V$ is quasi-compact,
finitely many affine opens $\operatorname{Spec}B_1,\dots,\operatorname{Spec}B_k$ cover
$V$. Put $D=D_1\times\dots\times D_k$, w-contractible by 1. The map
$\operatorname{Spec}D\to V$ is weakly étale, and $\{\operatorname{Spec}D\to V\}$ is a
pro-étale covering: for an affine open $W\subset V$ the sets $W\cap\operatorname{Spec}B_j$
are covered by finitely many opens that are standard in both $W$ and
$\operatorname{Spec}B_j$ (a standard fact on affine opens of a scheme), and the preimage in $\operatorname{Spec}D_j$
of such a standard open $D(h)$ is the affine $\operatorname{Spec}(D_j)_h$, surjecting
onto $D(h)$.

*3.* Fibre products of quasi-compact, quasi-separated objects over the quasi-separated $U$
are quasi-compact and quasi-separated, and so are equalizers ($A\times_{B\times_UB}B$ for
two maps $A\rightrightarrows B$, the diagonal of $B/U$ being quasi-compact). Hence finite
limits over $U$ of quasi-compact, quasi-separated objects (which exist in
$X_{\mathrm{proét}}$ by part 1 of [det-pe-topos-functoriality-site]) are quasi-compact and
quasi-separated. Build $W_\bullet$ by induction on the simplicial degree, using the split
construction: let $N_0\to U$ be a covering as in 2 and $W_0=N_0$. Given the $r$-truncated
simplicial object $W_{\leq r}$ with all terms of the required form, let
$M_{r+1}=(\operatorname{cosk}_rW_{\leq r})_{r+1}$, a finite limit of the $W_i$, $i\leq r$,
over $U$; it is quasi-compact and quasi-separated, so 2 gives a covering
$N_{r+1}=\operatorname{Spec}D'\to M_{r+1}$ with $D'$ w-contractible. Put

$$
W_{r+1}=N_{r+1}\sqcup\bigsqcup_{\sigma\colon[r+1]\twoheadrightarrow[k],\ k\leq r}N_k ,
$$

with degeneracies and faces defined as in the standard construction of split
hypercoverings (Stacks, Tag 09A1, and the general construction of hypercoverings in
Stacks, Chapter Hypercoverings). The map $W_{r+1}\to M_{r+1}$ restricts on $N_{r+1}$ to a
covering, hence is a covering. Finally $W_{r+1}$ is a finite disjoint union of spectra of
w-contractible rings, hence the spectrum of a w-contractible ring by 1, and it is weakly
contractible by [det-pe-weak-contractible-equivalences].
