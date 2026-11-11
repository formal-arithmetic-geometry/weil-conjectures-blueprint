+++
id = "definition-derived-adic-completeness--1"
kind = "definition"
title = "Derived adic completeness (1)"
name_showing = false
order = 208001
aliases = ["bp-r061-1"]
lean = ["AlgebraicGeometry.ProEtale.IsDerivedComplete"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1"]
+++
Let $E/\mathbf Q_\ell$ be finite, with uniformizer $\pi_E$, and let
$\mathcal O_{E,X}=p_X^*\underline{\mathcal O_E}$ and
$(\mathcal O_E/\pi_E^n)_X$ be the integral and finite coefficient
sheaves of Section [sec-Coefficient-rings]. A complex $K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ is
*derived complete* if its canonical map

$$
K\longrightarrow R\varprojlim_n
(K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^{n})_X)
$$

is an isomorphism.
