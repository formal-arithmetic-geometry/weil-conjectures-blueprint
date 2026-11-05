+++
id = "proposition-sp-unique-adjoint--1"
kind = "proposition"
title = "Uniqueness of right adjoints"
name_showing = false
order = 762001
aliases = ["bp-r230-1"]
lean = ["CategoryTheory.Adjunction.rightAdjointUniq", "CategoryTheory.Adjunction.rightAdjointUniq_hom_app_counit"]
uses = []
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
