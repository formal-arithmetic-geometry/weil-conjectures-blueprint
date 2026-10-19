+++
id = "sk-rem-pd-integral-corrections"
kind = "remark"
title = "Integral corrections and finite rings"
order = 2749
tags = ["sketch"]
+++
Let $X$, $K$ and $K^\vee=\cHom_X(K,\Lambda_X)$ be as in
[sk-thm-sf-identification], with $X$ smooth and separated of pure dimension
$d$ over an algebraically closed field.

Over $\mathcal O_E$, derived duality yields the natural
universal-coefficient exact sequence

$$
0\longrightarrow
\Ext^1_{\mathcal O_E}(H_c^{i+1}(X,K),\mathcal O_E)
\longrightarrow H^{2d-i}(X,K^\vee(d))
\longrightarrow
\Hom_{\mathcal O_E}(H_c^i(X,K),\mathcal O_E)
\longrightarrow0.
$$

It follows by applying derived Hom to a bounded finite free model of
$R\Gamma_c(X,K)$, since $\mathcal O_E$ has global dimension one.
It need not split canonically, and its $\Ext^1$ term is what keeps
the pairings on individual cohomology modules from being perfect. For
example, on a point the perfect complex
$[\mathcal O_E\xrightarrow{\pi_E}\mathcal O_E]$ in degrees $-1,0$ has
$H^0=\mathcal O_E/\pi_E$, whereas its dual has $H^0=0$ and
$H^1=\mathcal O_E/\pi_E$. Derived evaluation is an isomorphism, but the
degree-zero pairing is not perfect.

Over a finite ring $A$ that is not regular, derived Hom out of a bounded
finite-projective representative records all the groups $\Ext^i_A(-,A)$ of
the cohomology modules, which their ordinary duals can lose. Moreover, the
cohomology modules of a complex in $\Dctf(X,A)$ need not have finite Tor
dimension, so the derived pairing cannot be reduced to pairings of cohomology
sheaves.
