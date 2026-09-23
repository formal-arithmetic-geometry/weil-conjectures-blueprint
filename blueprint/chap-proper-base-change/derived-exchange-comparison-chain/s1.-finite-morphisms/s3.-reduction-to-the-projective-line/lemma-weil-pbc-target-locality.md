+++
id = "lemma-weil-pbc-target-locality"
kind = "lemma"
title = "Target locality"
order = 1566
uses = ["def-weil-pbc-property"]
+++
For proper $f:X\to Y$, the property $\mathsf{PBC}(f)$ is local for the etale
topology on $Y$.

## Proof

For an etale $V\to Y$ and a torsion sheaf $F$, sections of $R^qf_*F$ on $V$
are the sheafification of $U\mapsto H^q(X\times_YU,F|)$ over etale
$U\to V$. This description is functorial in $V$ and commutes with further
etale localization. Therefore an exchange map is an isomorphism if and
only if it is so after an etale cover of $Y$ (and its pullback cover on
$Y'$), because geometric stalks form a conservative family. The section
description is the content located at Tag `03Q8`.
