+++
id = "proposition-sp-unique-adjoint--1"
kind = "proposition"
title = "Uniqueness of right adjoints"
order = 763001
aliases = ["bp-r230-1"]
lean = ["CategoryTheory.Adjunction.rightAdjointUniq", "CategoryTheory.Adjunction.rightAdjointUniq_hom_app_counit"]
+++
Let $\mathcal C$ and $\mathcal D$ be categories, let
$F:\mathcal C\to\mathcal D$ and $G,J:\mathcal D\to\mathcal C$ be functors,
and fix adjunctions $F\dashv G$ and $F\dashv J$ with counits
$\varepsilon^G$ and $\varepsilon^J$. There is a natural isomorphism
$\rho:G\xrightarrow{\sim}J$ such that, for every $K\in\mathcal D$,

$$
\varepsilon^J(K)\circ F(\rho(K))=\varepsilon^G(K).
$$

Its underlying natural transformation is uniquely determined by this equation.

In particular, let $\Lambda$ be an admissible coefficient ring and let $J$
be a right adjoint of
$Rf_!:D^b_{\mathrm{ctf}}(X,\Lambda)\to D^b_{\mathrm{ctf}}(Y,\Lambda)$ with
counit $\varepsilon^J$. Taking $F=Rf_!$ and $G=f^!$ with counit
$\varepsilon_f$, there is a unique natural isomorphism
$\rho:f^!\xrightarrow{\sim}J$ with
$\varepsilon^J(K)\circ Rf_!(\rho(K))=\varepsilon_f(K)$.
