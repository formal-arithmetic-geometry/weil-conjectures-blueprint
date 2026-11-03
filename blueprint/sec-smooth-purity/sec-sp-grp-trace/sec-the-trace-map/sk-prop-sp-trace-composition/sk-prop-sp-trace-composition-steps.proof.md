+++
kind = "proof"
of = "det-sp-trace-transitivity-steps"
+++
(1) $\operatorname{Tr}_f$ is natural in its argument ([det-sp-trace-basic]); apply
naturality to the morphism $\gamma_g(K):L\to g^!K$, noting that the source
functor is $Rf_!(f^*(-)(d)[2d])$.

(2) By definition $\operatorname{Tr}_g(K)=\varepsilon_g(K)\circ Rg_!\gamma_g(K)$, so
$\operatorname{Tr}_g(K)\circ Rg_!\operatorname{Tr}_f(L)=\varepsilon_g(K)\circ Rg_!(\gamma_g(K)\circ\operatorname{Tr}_f(L))$.
Insert (1) and expand $\operatorname{Tr}_f(g^!K)=\varepsilon_f(g^!K)\circ Rf_!\gamma_f(g^!K)$.

(3) By [det-sp-composition-factors], under $(g\circ f)^!\simeq f^!g^!$ the composite
$\gamma_f(g^!K)\circ f^*\gamma_g(K)(d)[2d]$ is $\gamma_{g\circ f}(K)$; by
[det-sp-composition-comparisons] (1) the counit of $R(g\circ f)_!\dashv(g\circ f)^!$
under these identifications is $\varepsilon_g(K)\circ Rg_!\varepsilon_f(g^!K)$.
Substituting gives $\varepsilon_{g\circ f}(K)\circ R(g\circ f)_!\gamma_{g\circ f}(K)$,
which is $\operatorname{Tr}_{g\circ f}(K)$ by definition.
