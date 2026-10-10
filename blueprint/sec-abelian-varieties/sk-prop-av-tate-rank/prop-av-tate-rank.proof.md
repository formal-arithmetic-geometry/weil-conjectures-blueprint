+++
kind  = "proof"
of    = "prop-av-tate-rank"
uses = ["lem-sc-isogeny-surjective", "lem-sc-ntorsion-etale"]
+++
By [lem-sc-ntorsion-etale] each level is
$A[\ell^n](k)\cong(\Z/\ell^n\Z)^{2g}$, and the transition map $[\ell]:A[\ell^{n+1}](k)\to A[\ell^n](k)$ is
surjective, since $A(k)$ is divisible by [lem-sc-isogeny-surjective]
(an $\ell$-th root of a point of $A[\ell^n](k)$ lies in $A[\ell^{n+1}](k)$). Choosing compatible bases through these surjections
identifies the inverse system defining $T_\ell A$
([def-wf-abelian-tate-module]) with the system
$(\Z/\ell^n\Z)^{2g}$ under reduction, whose limit is $\Z_\ell^{2g}$;
tensoring with $\Q_\ell$ gives $V_\ell A\cong\Q_\ell^{2g}$.
