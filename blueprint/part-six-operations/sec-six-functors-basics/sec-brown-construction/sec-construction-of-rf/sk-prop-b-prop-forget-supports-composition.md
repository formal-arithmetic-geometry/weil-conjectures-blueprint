+++
id = "sk-prop-b-prop-forget-supports-composition"
kind = "proposition"
title = "Forgetting supports and composition"
order = 303
uses = ["sk-thm-sf-comp-composition"]
tags = ["sketch"]
+++
There is a natural map $\eta_f:Rf_!\to Rf_*$ on
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$. For a compactification $f=pj$ it is

$$
Rp_*j_!\longrightarrow Rp_*Rj_*=Rf_*,
$$

where $j_!\to Rj_*$ is adjoint to the inverse of the counit
$j^*Rj_*\xrightarrow{\sim}\mathrm{id}$. It is independent of the
compactification, and the square

$$
\begin{CD}
Rg_!Rf_! @>{c^!_{g,f}}>> R(gf)_!\\
@V{Rg_*(\eta_f)\,\circ\,(\eta_g Rf_!)}VV @VV{\eta_{gf}}V\\
Rg_*Rf_* @>{c^*_{g,f}}>> R(gf)_*
\end{CD}
$$

commutes. Here $c^!_{g,f}$ is the composition map of
Proposition [sk-thm-sf-comp-composition], and $c^*_{g,f}$ is the
composition map for ordinary direct images. If $f$ is proper, $\eta_f$
is an isomorphism; under these isomorphisms the two composition maps
agree whenever $f$ and $g$ are proper.
