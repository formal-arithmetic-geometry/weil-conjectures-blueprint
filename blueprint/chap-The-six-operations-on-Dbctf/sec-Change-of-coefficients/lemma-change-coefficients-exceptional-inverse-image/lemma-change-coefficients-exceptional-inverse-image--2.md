+++
id = "lemma-change-coefficients-exceptional-inverse-image--2"
kind = "lemma"
title = "Exceptional inverse image: reduction modulo powers of $\\ell$"
order = 640004
aliases = ["bp-r195-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.etaleReductionUpperShriekIso"]
uses = ["theorem-exceptional-inverse-image", "definition-sp-scalar-extension", "proposition-comparison-etale-derived-category"]
+++
Let $E\subset\overline{\mathbf Q}_\ell$ be finite over $\mathbf Q_\ell$ and
$n\geq 0$. For $Z=X,Y$, let
$$
\operatorname{red}_Z:\Dbc(Z,\mathcal O_E)\longrightarrow
D(Z_{\acute{e}t},\mathcal O_E/\ell^n)
$$
be derived reduction modulo $\ell^n$, followed by the comparison with the
small étale site, namely $R\nu_{Z,*}$ after identifying finite condensed
coefficients with finite coefficient sheaves. There is a canonical natural
isomorphism
$$
\operatorname{red}_X(f^!_{\mathcal O_E}K)
\xrightarrow{\ \sim\ }
f^!_{\acute{e}t,\mathcal O_E/\ell^n}(\operatorname{red}_Y K),
\qquad K\in\Dbc(Y,\mathcal O_E).
$$
It is the adjoint transpose of the inverse of the compactly supported
comparison for the chosen compactification of $f$.
