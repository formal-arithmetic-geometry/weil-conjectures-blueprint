+++
id = "definition-completed-inverse-image--1"
kind = "definition"
title = "Completed inverse image (1)"
name_showing = false
order = 414001
aliases = ["bp-r125-1"]
lean = ["AlgebraicGeometry.Scheme.completedPullbackObject", "AlgebraicGeometry.Scheme.completedPullbackFunctor"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-extremally-disconnected-covers--3"]
+++
Let $g:Y'\to Y$ be a morphism. For $M\in D(Y_{\mathrm{pro}\acute{e}t},\mathcal O_E)$, the
*completed inverse image* is

$$
\hat g^*M
=R\varprojlim_n g^*(M\otimes^{\mathbf L}_{\mathcal O_{E,Y}}
(\mathcal O_E/\pi_E^n)_Y)
\in D(Y'_{\mathrm{pro}\acute{e}t},\mathcal O_E).
$$
