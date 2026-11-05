+++
id = "proposition-pro-etale-affines-form-basis"
kind = "proposition"
title = "Pro-étale affines form a basis"
order = 66
lean = ["AlgebraicGeometry.Scheme.AffineProEt", "AlgebraicGeometry.Scheme.AffineProEt.toProEt", "AlgebraicGeometry.Scheme.AffineProEt.topology", "AlgebraicGeometry.Scheme.AffineProEt.isCoverDense_toProEt", "AlgebraicGeometry.Scheme.AffineProEt.isEquivalence_sheafPushforwardContinuous_toProEt"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site"]
+++
Every object of $X_{\mathrm{pro}\acute{e}t}$ has a pro-étale covering by
pro-étale affines over $X$. These form a full subsite whose category of
sheaves, of sets or of abelian groups, is equivalent to $\Sh(X_{\mathrm{pro}\acute{e}t})$
by restriction.
