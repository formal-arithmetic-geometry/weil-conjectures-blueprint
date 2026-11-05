+++
id = "definition-derived-adic-completeness"
kind = "definition"
title = "Derived adic completeness"
order = 208
lean = ["AlgebraicGeometry.ProEtale.IsDerivedComplete", "AlgebraicGeometry.ProEtale.AdicCompletion.isDerivedComplete_iff"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-affines-form-basis"]
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
