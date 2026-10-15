+++
kind = "proof"
of = "det-pe-wcb-cover"
+++
Let $\{\operatorname{Spec}B_i\}$ be the family of all affine opens of $U$. For each $i$,
let $B_i\to C_i$ be the strict w-local cover of [lem-weil-pbc-strict-w-cover] (faithfully
flat, ind-étale, w-strictly local), and $C_i\to D_i$ the faithfully flat ind-Zariski
algebra of [det-pe-wc-cover-second-stage], applied with a Stonean cover of
$\pi_0(\operatorname{Spec}C_i)$; then $D_i$ is w-contractible and $B_i\to D_i$ is
faithfully flat and ind-étale ([lem-weil-pbc-ind-etale-stability]).

The composite $\operatorname{Spec}D_i\to\operatorname{Spec}B_i\to U\to X$ is weakly étale
(ind-étale maps and open immersions are weakly étale, and weakly étale maps compose), so
$\operatorname{Spec}D_i$ is an object of $X_{\mathrm{proét}}$, and
$\operatorname{Spec}D_i\to U$ is a morphism there.

The family is a pro-étale covering [def-weil-pbc-proetale-covering]: let $W\subset U$ be an
affine open. Then $W$ itself is one of the $\operatorname{Spec}B_i$, and
$\operatorname{Spec}D_i$ is an affine open of $\operatorname{Spec}D_i\times_UW
=\operatorname{Spec}D_i$ whose image is all of $W$ by faithful flatness. So one index
suffices for each $W$.
