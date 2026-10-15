+++
kind = "proof"
of = "sk-prop-sp-trace-composition"
uses = ["sk-prop-sp-composition"]
+++
Expand both traces by their definition. By naturality of $\gamma_f$, the map
$\gamma_g(K):g^{*}K(e)[2e]\to g^!K$ can be moved past the purity map of the first
trace. The composite then consists of the two purity maps, which together are
$\gamma_{g\circ f}(K)$ by [sk-prop-sp-composition], followed by

$$
Rg_!Rf_!f^!g^!K
\xrightarrow{\ Rg_!(\varepsilon_{f}(g^!K))\ }
Rg_!g^!K
\xrightarrow{\ \varepsilon_{g}(K)\ }K.
$$

This is the counit of the composite adjunction $R(g\circ f)_!\dashv(g\circ f)^!$
between $\Dctf(X,\Lambda)$ and $\Dctf(Z,\Lambda)$, so the composite is purity for
$g\circ f$ followed by its counit, that is, $\operatorname{Tr}_{g\circ f}(K)$.
