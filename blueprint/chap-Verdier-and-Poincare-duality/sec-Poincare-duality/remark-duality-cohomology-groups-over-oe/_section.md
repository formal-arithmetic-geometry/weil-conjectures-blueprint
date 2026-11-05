+++
id = "remark-duality-cohomology-groups-over-oe"
kind = "remark"
title = "Duality on cohomology groups over $\\mathcal O_E$ and finite rings"
order = 863
+++
Over $\mathcal O_E$, derived duality gives only the natural
universal coefficient exact sequence

$$
0\longrightarrow
\Ext^1_{\mathcal O_E}(H_c^{i+1}(X,K),\mathcal O_E)
\longrightarrow H^{2d-i}(X,K^\vee(d))
\longrightarrow
\Hom_{\mathcal O_E}(H_c^i(X,K),\mathcal O_E)
\longrightarrow0.
$$

It comes from applying derived Hom to a bounded finite free model of
$R\Gamma_c(X,K)$, since $\mathcal O_E$ has global dimension one.
The sequence need not split canonically, and because of its $\Ext^1$ term
the pairings on individual cohomology modules need not be perfect. For
example, on a point the perfect
complex $[\mathcal O_E\xrightarrow{\pi_E}\mathcal O_E]$ in degrees
$-1,0$ has $H^0=\mathcal O_E/\pi_E$, whereas its dual has
$H^0=0$ and $H^1=\mathcal O_E/\pi_E$. Derived evaluation
is an isomorphism, but the degree-zero pairing is not perfect.

Over a finite ring $A$ that is not injective as a module over
itself, derived Hom out of a
bounded complex of finite projective modules records all the
groups $\Ext^i_A(-,A)$ of the cohomology modules, and this information
may be lost in their ordinary duals. Moreover, the cohomology modules of a
complex in $D^b_{\mathrm{ctf}}(X,A)$ need not have finite Tor dimension, so the
derived pairing cannot be reduced to pairings of cohomology sheaves.
