+++
id = "det-prop-scalar-six-exceptional"
kind = "lemma"
title = "Coefficient comparison for exceptional inverse image"
order = 2820
uses = ["det-prop-scalar-six-compact-support", "det-prop-scalar-six-direct-image", "sk-thm-existence", "sk-lem-formal-closed-support", "sk-prop-geo-p1-adjunction", "sk-prop-diagonal-tower"]
+++
Let $f\colon X\to Y$ be a morphism of standing schemes, $\Lambda\to\Lambda'$ a listed
coefficient map, and $f^!$ the right adjoint of $Rf_!$ on $\Loc(\Dctf(-,\Lambda))$
and on $\Loc(\Dctf(-,\Lambda'))$ ([sk-thm-existence]). For $K\in\Dctf(Y,\Lambda)$ let
$$
\beta_{f,K}\colon(f^!K)_{\Lambda'}\longrightarrow f^!(K_{\Lambda'})
$$
be the transpose under $Rf_!\dashv f^!$ over $\Lambda'$ of
$$
Rf_!\bigl((f^!K)_{\Lambda'}\bigr)\xrightarrow{(\gamma^!_{f,f^!K})^{-1}}(Rf_!f^!K)_{\Lambda'}\xrightarrow{(\epsilon_K)_{\Lambda'}}K_{\Lambda'}
$$
(with $\gamma^!$ the isomorphism of [det-prop-scalar-six-compact-support]). Then
$\beta_{f,K}$ is an isomorphism in $\Dctf(X,\Lambda')$, and the $\beta$ are compatible
with composition, $\beta_{gf,K}=f^!(\beta_{g,K})\circ\beta_{f,g^!K}$ under $(gf)^!=f^!g^!$,
and with restriction to open subschemes; for an open immersion, $\beta$ is the
pullback identification.
