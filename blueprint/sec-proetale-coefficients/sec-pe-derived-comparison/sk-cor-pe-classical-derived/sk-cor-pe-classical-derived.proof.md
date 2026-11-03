+++
kind = "proof"
of = "sk-cor-pe-classical-derived"
uses = ["thm-weil-pbc-site-comparison", "sk-thm-pe-classical-sheaves", "sk-prop-sf-comparison"]
+++
For kernels and cokernels this follows from exactness and full faithfulness
of $\nu_X^*$. Given an extension
$0\to\nu_X^*F\to G\to\nu_X^*F'\to0$, we apply $\nu_{X,*}$. Since
$R^1\nu_{X,*}\nu_X^*F=0$ by Theorem [sk-prop-sf-comparison], the
result $0\to F\to\nu_{X,*}G\to F'\to0$ is exact, and the counit maps
its pullback to the original extension. This map is the identity on the
outer terms, so by the five lemma $G\simeq\nu_X^*\nu_{X,*}G$ is classical.

For the equivalence, the functor $\nu_X^*$ lands in classical complexes,
and $\nu_X^*$ is fully faithful on $D^+$ by
Theorem [sk-prop-sf-comparison], so it remains to show that the
counit $\nu_X^*R\nu_{X,*}K\to K$ is an isomorphism for $K$ in
$D^+_{\mathrm{class}}$. By (2.7), every classical
sheaf $\nu_X^*F$ is $\nu_{X,*}$-acyclic, so the hypercohomology spectral
sequence for $R\nu_{X,*}K$ degenerates and
$H^q(R\nu_{X,*}K)=\nu_{X,*}H^q(K)$. On $H^q$ the counit is therefore the
counit $\nu_X^*\nu_{X,*}H^q(K)\to H^q(K)$ for a classical sheaf, which is
an isomorphism by Theorem [sk-thm-pe-classical-sheaves]; see
[Stacks, Tag 09B1](https://stacks.math.columbia.edu/tag/09B1).
