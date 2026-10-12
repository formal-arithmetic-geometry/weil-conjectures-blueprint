+++
id = "sk-thm-dnc"
kind = "theorem"
title = "DNC invariance of the section dualizing line"
order = 2339
uses = ["sk-def-purity-conv", "sk-lem-geometry", "sk-prop-a1-inv", "sk-prop-an", "sk-prop-cohsm"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_sectionInvariant_normalCone"]
tags = ["sketch"]
+++
In the situation of [sk-lem-geometry] there is a unique isomorphism

$$
\mathcal C(g,s)\ \xrightarrow{\ \sim\ }\ \mathcal C(\pi_N,0_N)
$$

which, in coordinates carrying $(g,s)$ to $(\Aaf^d_B\to B,0)$, is the
identity on the standard section invariant. It is compatible with étale
localization and arbitrary base change in $B$.
