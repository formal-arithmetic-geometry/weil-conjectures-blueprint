+++
id = "lem-wf-weil-fundamental-representation"
kind = "lemma"
title = "The Weil fundamental representation is a continuous representation"
lean = ["AlgebraicGeometry.Monodromy.DegreeDatum.lift", "AlgebraicGeometry.Monodromy.DegreeDatum.lift_apply_of_mem_ker", "AlgebraicGeometry.Monodromy.DegreeDatum.lift_degreeOneElement", "AlgebraicGeometry.Monodromy.DegreeDatum.continuous_lift"]
order = 3735
uses = ["def-tw-frobenius-action", "def-wf-fundamental-representation", "thm-lisse-qlbar-representations"]
+++
In the situation of [def-wf-fundamental-representation], the formula

$$
\rho(\gamma s^n):=\rho_{\mathrm{geom}}(\gamma)T_s^n
\qquad(\gamma\in\pi_1(X,\bar x),\ n\in\mathbf Z)
$$

defines a continuous group homomorphism
$\rho:W(X_0,\bar x)\to\operatorname{GL}(V)$ with
$\rho|_{\pi_1(X,\bar x)}=\rho_{\mathrm{geom}}$ and
$\rho(s)=T_s$.
