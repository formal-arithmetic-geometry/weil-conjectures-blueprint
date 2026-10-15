+++
kind  = "proof"
of    = "thm-weil-pbc-idempotent-complete-triangulation"
+++
The scalar operation of [def-weil-pbc-qbar-category] is independent of $N$:
for two finite fields $N,N'$ containing $\Ql(\alpha)$ and the stage $M$, the
representatives $\alpha u_N$ and $\alpha u_{N'}$ transport to their
compositum and agree there, since $T_{P/N}$ and $T_{P/N'}$ are linear over
$N$ and $N'$ (hence over $N\cap N'$ containing $\Ql(\alpha)$); independence
of the representative of $f$ holds through the representative equivalence
relation of [def-weil-pbc-finite-stage-pair-category]: transport an equality
$u_P=v_P$, which survives scalar multiplication. The field laws and
bilinearity hold at a common stage by
[prop-weil-pbc-common-stage-calculus], so $\mathcal P_T$ is $\Qlb$-linear.
By [thm-weil-pbc-verdier-axioms], $\mathcal P_T=\Dbc(T,\Qlb)$ is
triangulated, and it is idempotent complete by
[thm-weil-pbc-qbar-idempotent-complete], so the canonical fully faithful
functor into the Karoubi envelope is an equivalence by that theorem, hence
exact. The composite $j_E$ is exact by [thm-weil-pbc-verdier-axioms], and
$E$-linear and $\Qlb$-linear by the displayed scalar definition.
