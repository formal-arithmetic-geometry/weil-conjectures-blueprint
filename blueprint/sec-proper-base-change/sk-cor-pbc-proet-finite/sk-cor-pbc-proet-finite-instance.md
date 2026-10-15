+++
id = "det-pbc-proet-finite-instance"
kind = "lemma"
title = "Finite coefficients satisfy the torsion hypothesis"
uses = ["thm-weil-pbc-finite-level-proetale", "def-weil-pbc-etale-origin-witness", "thm-weil-pbc-site-comparison"]
+++
Let $A$ be a finite commutative ring, of additive order $N=|A|$, let $T$ be a
scheme, and let $K\in D^+_{\mathrm{class}}(T_{\mathrm{proét}},A)$, that is,
$K\simeq\nu_T^*L$ for some $L\in D^+(T_{\Et},A)$ (an étale-origin witness
[def-weil-pbc-etale-origin-witness]). Then:

1. every cohomology sheaf of $K$ and of $L$ is killed by $N$; in particular
   their underlying abelian cohomology sheaves are torsion;
2. for $p:X\to Y$ proper and $K$ on $X$, the exchange map
   $g^*Rp_*K\to Rp'_*g'^*K$ is an isomorphism in
   $D^+(Y'_{\mathrm{proét}},A)$, and it is the exchange map of
   [thm-weil-pbc-finite-level-proetale] for the witness $(L,\alpha)$.
