+++
id = "sbc-def-strict-localization"
kind = "definition"
title = "Strict localization"
order = 5228
lean = ["AlgebraicGeometry.Scheme.strictLocalization"]
uses = ["def-weil-pbc-strict-henselization-limit"]
+++
Let $a:Z\to S$ and let $\bar z$ be a geometric point of $Z$, with image
$\bar s=a(\bar z)$ in $S$. The strict henselizations
$\mathcal O^{\mathrm{sh}}_{Z,\bar z}$ and
$\mathcal O^{\mathrm{sh}}_{S,\bar s}$ are those of
[def-weil-pbc-strict-henselization-limit]; put
$$
Z_{(\bar z)}=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{Z,\bar z},\qquad
S_{(\bar s)}=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}.
$$
A *geometric point of $S_{(\bar s)}$* is a morphism $\bar t\to S_{(\bar s)}$
with $\bar t$ a geometric point.

Unresolved dependencies: def:weil-pbc-scheme-conventions
