+++
kind  = "proof"
of    = "sk-thm-wft-curve-middle-upper"
+++
Choose a dense affine open $v:V_0\hookrightarrow U_0$.
Since $F$ is lisse on $U_0$, the unit $F\to v_*F|_V$ is an
isomorphism; this follows from the surjectivity of fundamental groups
used above, or from the inertia invariants at the deleted points
([sk-i-real-boundary]).
Thus $j_*F$ is also the middle extension of $F|_V$ from $V_0$ to
$C_0$. By [sk-thm-wft-affine-curve-upper], $H_c^r(V,F)$ has
weights at most $w+r$. The restriction of $j_*F$ to the finite set
$C_0\setminus V_0$ has weights at most $w$ by boundary
semicontinuity ([sk-p-real-semi]), and its cohomology is concentrated
in degree zero. By localization ([sk-prop-sf-open-closed-triangle]),
$H_c^0(C,j_*F)$ injects into the cohomology of this
boundary sheaf, $H_c^1(V,F)$ surjects onto $H_c^1(C,j_*F)$, and the
groups in degree two are isomorphic, while higher degrees vanish. The
bounds follow.
