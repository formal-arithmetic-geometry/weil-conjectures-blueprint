+++
kind = "proof"
of = "sk-prop-sp-trace-composition"
uses = ["sk-prop-sp-composition"]
+++
We expand both traces using (10.24). By naturality of $\gamma_f$,
we may move the map $\gamma_g(K):g^{*}K(e)[2e]\to g^!K$
past the map $\gamma_f$ of the first trace. The composite then consists of
the two maps $\gamma_f$ and $\gamma_g$, which together are $\gamma_{g\circ f}(K)$ by
Proposition [sk-prop-sp-composition], followed by

$$
Rg_!Rf_!f^!g^!K
\xrightarrow{\ Rg_!(\varepsilon_{f}(g^!K))\ }
Rg_!g^!K
\xrightarrow{\ \varepsilon_{g}(K)\ }K.
$$

This is the counit of the composite adjunction
$R(g\circ f)_!\dashv(g\circ f)^!$. Thus the composite is the map $\gamma_{g\circ f}(K)$
followed by its counit, that is,
$\operatorname{Tr}_{g\circ f}(K)$.
