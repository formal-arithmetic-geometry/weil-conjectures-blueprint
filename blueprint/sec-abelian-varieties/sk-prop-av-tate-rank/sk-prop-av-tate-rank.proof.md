+++
kind  = "proof"
of    = "sk-prop-av-tate-rank"
uses = ["sk-prop-av-divisible"]
+++
By [sk-prop-av-ntorsion-etale] each level is
$A[\ell^n](k)\cong(\Z/\ell^n\Z)^{2g}$, and by [sk-prop-av-divisible]
the transition map $[\ell]:A[\ell^{n+1}](k)\to A[\ell^n](k)$ is
surjective. Choosing compatible bases through these surjections
identifies the inverse system defining $T_\ell A$
([sk-def-av-tate]) with the system
$(\Z/\ell^n\Z)^{2g}$ under reduction, whose limit is $\Z_\ell^{2g}$;
tensoring with $\Q_\ell$ gives $V_\ell A\cong\Q_\ell^{2g}$.
