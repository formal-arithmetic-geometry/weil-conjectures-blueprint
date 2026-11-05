+++
id = "det-prop-scalar-six-compact-support"
kind = "lemma"
title = "Coefficient comparison for compactly supported direct image"
order = 2819
uses = ["det-prop-scalar-six-direct-image", "det-prop-scalar-six-pullback", "sk-thm-existence"]
+++
Let $f\colon X\to Y$ be a morphism of standing schemes, $f=p\circ j$ a
compactification ($j$ an open immersion, $p$ proper), so that $Rf_!=Rp_*j_!$
([sk-thm-existence] (2)), and let $\Lambda\to\Lambda'$ be a listed coefficient map. For
$K\in\Dctf(X,\Lambda)$ the composite
$$
\gamma^!_{f,K}\colon(Rf_!K)_{\Lambda'}=(Rp_*j_!K)_{\Lambda'}\xrightarrow{\gamma_{p,j_!K}}Rp_*\bigl((j_!K)_{\Lambda'}\bigr)\simeq Rp_*j_!(K_{\Lambda'})=Rf_!(K_{\Lambda'})
$$
is an isomorphism in $\Dctf(Y,\Lambda')$. It does not depend on the
compactification and is compatible with the composition isomorphisms
$R(gf)_!\simeq Rg_!Rf_!$.
