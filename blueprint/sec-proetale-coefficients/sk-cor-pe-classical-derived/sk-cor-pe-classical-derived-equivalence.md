+++
id = "det-pe-classical-derived-equivalence"
kind = "lemma"
title = "The bounded-below classical equivalence"
uses = ["det-pe-classical-sheaves-modules", "sk-prop-sf-comparison", "thm-weil-pbc-site-comparison"]
+++
Let $X$ be a scheme and $\Lambda$ a discrete commutative ring for which the
bounded-below derived unit $L\xrightarrow{\sim}R\nu_{X,*}\nu_X^*L$ of
[sk-prop-sf-comparison] holds for $L\in D^+(X_{\Et},\Lambda)$.

1. $\nu_X^*$ maps $D^+(X_{\Et},\Lambda)$ into
   $D^+_{\mathrm{class}}(X_{\Proet},\Lambda)$, and $R\nu_{X,*}$ maps
   $D^+(X_{\Proet},\Lambda)$ into $D^+(X_{\Et},\Lambda)$.
2. For every $K\in D^+_{\mathrm{class}}(X_{\Proet},\Lambda)$ the counit
   $\nu_X^*R\nu_{X,*}K\to K$ is an isomorphism.

Hence $\nu_X^*$ and $R\nu_{X,*}$ are inverse equivalences between
$D^+(X_{\Et},\Lambda)$ and $D^+_{\mathrm{class}}(X_{\Proet},\Lambda)$.
