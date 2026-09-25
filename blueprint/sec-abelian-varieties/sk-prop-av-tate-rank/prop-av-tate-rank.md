+++
id = "prop-av-tate-rank"
kind = "theorem"
title = "The $\\ell$-adic Tate module is free of rank $2g$"
order = 594
uses = ["def-sc-abelian-variety", "def-wf-abelian-tate-module", "lem-sc-finite-flat-surj-points", "lem-sc-finite-nonempty-point", "lem-sc-isogeny-surjective", "lem-sc-ntorsion-etale", "rem-ptr-sc-abelian-variety-1"]
tags = ["latex:proposition"]
+++
Let $A$ be an abelian variety of dimension $g$ over an algebraically
closed field $k$ and let $\ell\ne\operatorname{char}k$. Then

$$
T_\ell A\cong\Z_\ell^{2g},\qquad V_\ell A\cong\Q_\ell^{2g}.
$$

## Proof

By [lem-sc-ntorsion-etale] each level is
$A[\ell^n](k)\cong(\Z/\ell^n\Z)^{2g}$, and by [lem-sc-finite-flat-surj-points], [lem-sc-finite-nonempty-point], [lem-sc-isogeny-surjective]
the transition map $[\ell]:A[\ell^{n+1}](k)\to A[\ell^n](k)$ is
surjective. Choosing compatible bases through these surjections
identifies the inverse system defining $T_\ell A$
([def-wf-abelian-tate-module]) with the system
$(\Z/\ell^n\Z)^{2g}$ under reduction, whose limit is $\Z_\ell^{2g}$;
tensoring with $\Q_\ell$ gives $V_\ell A\cong\Q_\ell^{2g}$.

Uses: [def-wf-abelian-tate-module], [def-sc-abelian-variety], [rem-ptr-sc-abelian-variety-1], [lem-sc-finite-flat-surj-points], [lem-sc-finite-nonempty-point], [lem-sc-isogeny-surjective], [lem-sc-ntorsion-etale]
