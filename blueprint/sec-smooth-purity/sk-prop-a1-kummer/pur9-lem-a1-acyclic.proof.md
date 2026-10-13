+++
kind = "proof"
of = "pur9-lem-a1-acyclic"
uses = ["pur9-input-stalk-formula", "pur9-lem-curve-a1", "pur9-lem-fibre-reduction"]
+++
By Input “Forgetting finite coefficient actions in direct images” (`pur7710-input-cohomology-coefficients`, see [sk-thm-sf-comp-composition]), it suffices to prove the statement for the underlying abelian sheaves; the twist sheaf is constant with value the finite $\ell$-group $P(m)$. Geometric stalks are conservative on $Y_{\Et}$, so it suffices to check the map on cohomology stalks at every geometric point $\bar y$. By Input [pur9-input-stalk-formula], $(R^qp_*P(m))_{\bar y}=H^q(\Aaf^1_{S'},P(m))$, $S'=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{Y,\bar y}$, and the unit becomes $P(m)\to H^0$. Lemma [pur9-lem-fibre-reduction] identifies these groups with $H^q(\Aaf^1_k,P(m))$, compatibly with the constants, and Lemma [pur9-lem-curve-a1] computes them.
