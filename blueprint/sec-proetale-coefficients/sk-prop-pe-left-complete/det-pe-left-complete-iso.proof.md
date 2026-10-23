+++
kind = "proof"
of = "det-pe-left-complete-iso"
+++
Write $P=\prod_n\tau_{\geq-n}K$ and let $\ell\colon K\to P$ have the truncation maps as
components. Since the truncation maps are compatible with the transitions,
$(1-T)\circ\ell=0$. Complete $1-T$ to a distinguished triangle
$L\xrightarrow{\iota}P\xrightarrow{1-T}P\to L[1]$; as $(1-T)\circ\ell=0$, the map $\ell$
factors as $\ell=\iota\circ u$ for some $u\colon K\to L$. Then $L$ is a homotopy limit
$R\varprojlim_n\tau_{\geq-n}K$, and it suffices to show that $u$ is an isomorphism, i.e. that
$H^q(u)$ is an isomorphism for every $q$; replacing $L$ by $K$ along $u$ then gives the
displayed triangle.

By [det-pe-milnor-sequence] there is a short exact sequence
$0\to R^1\varprojlim_nH^{q-1}(\tau_{\geq-n}K)\to H^q(L)\to
\varprojlim_nH^q(\tau_{\geq-n}K)\to0$, whose second map is induced by $\iota$ and the
projections. By [det-pe-left-complete-truncation-tower] (applied in degrees $q-1$ and $q$) the
first term vanishes, so $H^q(L)\to\varprojlim_nH^q(\tau_{\geq-n}K)$ is an isomorphism, and
the composite
$H^q(K)\xrightarrow{H^q(u)}H^q(L)\to\varprojlim_nH^q(\tau_{\geq-n}K)$, which is induced by the
truncation maps, is an isomorphism. Hence $H^q(u)$ is an isomorphism for every $q$.
