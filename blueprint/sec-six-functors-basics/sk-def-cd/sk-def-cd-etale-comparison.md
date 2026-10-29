+++
id = "det-cd-etale-comparison"
kind = "lemma"
title = "Pro-étale and étale ℓ-cohomological dimensions agree"
order = 2231
uses = ["det-pe-classical-sheaves-modules", "sk-prop-sf-comparison", "prop-weil-pbc-comparison-direct-image", "def-sc-etale-torsion-cd"]
+++
Let $S$ be a qcqs scheme and $g\colon X\to Y$ a qcqs morphism. A sheaf of abelian
groups on a site is *$\ell$-power torsion* if each local section is killed by
some power of $\ell$.

1. A classical sheaf $F\cong\nu_S^*F_0$ on $S_{\Proet}$ is $\ell$-power torsion if
   and only if $F_0$ is.
2. $\operatorname{cd}_\ell(S)=\sup\{q:H^q(S_{\Et},F_0)\neq0$ for some
   $\ell$-power torsion sheaf $F_0$ on $S_{\Et}\}$.
3. $\operatorname{cd}_\ell(g)=\sup\{q:R^qg_{\Et,*}F_0\neq0$ for some
   $\ell$-power torsion sheaf $F_0$ on $X_{\Et}\}$.
4. If $\operatorname{cd}_{\rm tor}(S)\leq c$ in the sense of
   [def-sc-etale-torsion-cd], then $\operatorname{cd}_\ell(S)\leq c$.
