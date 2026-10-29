+++
id = "sk-prop-sf-comp-proper"
kind = "proposition"
title = "Proper coincidence"
order = 3205
uses = ["sk-prop-cohsm", "sk-prop-sf-comp-coherence", "sk-thm-properbasechange", "sk-prop-sf-existence"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_rightDerivedLowerStar"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be proper. Then $(\operatorname{id}_X,f)$ is an object of
$\operatorname{Comp}(f)$, and the resulting canonical identification

$$
Rf_!\ \xrightarrow{\ \sim\ }\ Rf_*
$$

is independent of the compactification. Under it the exchange
$\operatorname{Ex}_!$ of [det-def-sf-exchanges] is the proper-base-change
exchange $\operatorname{Ex}_*$; consequently [det-prop-sf-cbc] specializes to
[sk-thm-properbasechange] for proper $f$, and the two clauses of
[sk-thm-sf-package] (2) agree on proper morphisms.
