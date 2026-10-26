+++
id = "det-prop-sfb-qlbar-colimit-x-invert-ell"
kind = "lemma"
title = "$E_X$ is $\\mathcal O_{E,X}$ with $\\ell$ inverted"
order = 1200
uses = ["def-sfb-integers-to-subfield", "def-sfb-integers-to-subfield-point", "det-def-sfb-condensed-ring", "det-def-sfb-pullback-from-point"]
+++
Let $E/\mathbf Q_\ell$ be finite and $X$ a scheme. Let $\cO_{E,X}[1/\ell]$ denote the colimit,
in sheaves of $\cO_{E,X}$-modules on $X_{\mathrm{proét}}$, of
$$
\cO_{E,X}\xrightarrow{\ \ell\ }\cO_{E,X}\xrightarrow{\ \ell\ }\cO_{E,X}\xrightarrow{\ \ell\ }\cdots,
$$
with its ring structure as the localization of $\cO_{E,X}$ at $\ell$. Then the map
$\varphi\colon\cO_{E,X}\to E_X$ of [def-sfb-integers-to-subfield], together with the maps
$\ell^{-m}\varphi$ on the $m$-th term, induces an isomorphism of sheaves of rings
$$
\cO_{E,X}[1/\ell]\xrightarrow{\ \sim\ }E_X .
$$
In particular $\ell$ acts invertibly on $E_X$, and $E_X$ is a flat $\cO_{E,X}$-module.
