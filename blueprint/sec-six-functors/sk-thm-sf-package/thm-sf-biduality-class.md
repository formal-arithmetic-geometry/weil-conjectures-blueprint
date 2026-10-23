+++
id = "thm-sf-biduality-class"
kind = "theorem"
title = "Verdier biduality on the coefficient class"
order = 3381
uses = ["lem-coef-integral-residue-tor", "lem-weil-verdier-preservation-strata", "thm-coef-integral-verdier", "thm-fix-general-biduality", "def-sf-setting", "sk-thm-pd-verdier-duality", "det-pd-biduality-coefficients", "sk-prop-scalar-six", "sk-lem-integral-models", "sk-thm-sfb-qlbar-two-colimit"]
+++
Let $X$ be separated of finite type over $\Fbar$, and let
$\Lambda=A_{E,n},\mathcal O_E,E$, or $\Qlb$.
regarded as a condensed ring, and use the categories
$\Dctf(X,\Lambda)\subseteq D(X_{\mathrm{pro\acute et}},\Lambda)$ of
[def-sf-setting]. Put
$\omega_{X,\Lambda}=Ra_X^!\Lambda$,
$D_{X,\Lambda}=R\mathcal Hom_\Lambda(-,\omega_{X,\Lambda})$.
Then $D_{X,\Lambda}$ is an exact contravariant anti-equivalence
of $D^b_{ctf}(X,\Lambda)$, and the evaluation-defined map

$$
K\longrightarrow D_{X,\Lambda}D_{X,\Lambda}K
$$

is a natural isomorphism ([sk-thm-pd-verdier-duality]). For
$\Lambda=\mathcal O_E,E,\Qlb$ this is the whole category
$\Dbc(X,\Lambda)$.

At finite coefficients, an input Tor interval $[a,b]$ gives
$[-b-2\dim X,-a]$ for its dual. For $K\in\Dbc(X,\mathcal O_E)$ the
reductions $K_n$ have Tor amplitude in one interval $[a,b]$, and the
reductions of $D_{X,\mathcal O_E}K$, which are the duals $D_{X,A_{E,n}}K_n$
([sk-prop-scalar-six]), have Tor amplitude in $[-b-2\dim X,-a]$. In
particular the finite or integral dualizing object has interval
$[-2\dim X,0]$.
