+++
kind = "proof"
of = "det-pe-left-complete-iso"
+++
In degree $q$ the fibre is $(\prod_n\tau_{\geq-n}K)^q\oplus(\prod_n\tau_{\geq-n}K)^{q-1}$
with differential $(x,y)\mapsto(dx,(1-T)x-dy)$. Since the quotient maps are compatible with
the transitions, $(1-T)((\bar k_n)_n)=(\bar k_n-t_n(\bar k_{n+1}))_n=0$, so $\iota$ is a map
of complexes; composed with the projection to $\prod_n\tau_{\geq-n}K$ it is the family of
quotient maps.

By [det-pe-milnor-sequence] there is a short exact sequence
$0\to R^1\varprojlim_nH^{q-1}(\tau_{\geq-n}K)\to H^q(R\varprojlim_n\tau_{\geq-n}K)\to
\varprojlim_nH^q(\tau_{\geq-n}K)\to0$, whose second map is induced by the projection to
the product. By [det-pe-left-complete-truncation-tower] (applied in degrees $q-1$ and $q$)
the first term vanishes and the composite
$H^q(K)\xrightarrow{H^q\iota}H^q(R\varprojlim_n\tau_{\geq-n}K)\to
\varprojlim_nH^q(\tau_{\geq-n}K)$, which is induced by the quotient maps, is an
isomorphism. Hence $H^q\iota$ is an isomorphism for every $q$.
