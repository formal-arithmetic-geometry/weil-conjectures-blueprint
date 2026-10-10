+++
id = "def-weil-pbc-projection-compactification"
kind = "definition"
title = "Chosen compactification and compact-support image"
order = 1268
lean = ["AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactification"]
uses = ["def-nagata-compactification"]
+++
Let $f:X\to Y$ admit a chosen compactification

$$
X\xrightarrow{j}\overline X\xrightarrow{p}Y,
\qquad f=pj,
$$

with $j$ an open immersion and $p$ proper. For this datum and $E$ in the
derived category of sheaves on $X_{\Et}$ set

$$
Rf_!^{(j,p)}E:=Rp_*j_!E,
$$

where $j_!$ (extension by zero) is exact and so is applied termwise.

For proper $f$, its identity compactification is $(j,p)=(1_X,f)$.
