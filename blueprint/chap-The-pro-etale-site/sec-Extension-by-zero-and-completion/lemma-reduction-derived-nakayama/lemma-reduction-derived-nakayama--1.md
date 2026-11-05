+++
id = "lemma-reduction-derived-nakayama--1"
kind = "lemma"
title = "Reduction and derived Nakayama (1)"
name_showing = false
order = 210001
aliases = ["bp-r062-1"]
lean = ["AlgebraicGeometry.ProEtale.DerivedNakayama.derived_nakayama_resolution"]
+++
Let $E/\mathbf Q_\ell$ be finite, let $X$ be a scheme, and let $n\geq1$.
For $K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$, put

$$
K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X.
$$

Then $K_n$ is the cone of $\pi_E^n:K\to K$. More precisely, if
$Q$ denotes localization from complexes to the derived category, there is
an isomorphism

$$
(Q(C))_n\simeq Q\bigl(\operatorname{Cone}(\pi_E^n:C\to C)\bigr)
$$

natural in the complex $C$. The coefficients are the continuous condensed
integer ring and its finite quotient, pulled back from the point to $X$.
