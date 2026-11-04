+++
kind = "proof"
of = "sk-thm-wft-curve-middle-upper"
uses = ["sk-l-dl-a1-endpoints", "sk-lem-wft-infinity-reduction"]
+++
Suppose first that $C_0$ is geometrically connected. We reduce to the
affine case. Choose a dense affine open
$v:V_0\hookrightarrow U_0$. Since $F$ is lisse on $U_0$, the unit
$F\to v_*F|_V$ is an isomorphism by the last assertion of
Lemma [sk-i-real-boundary]. Thus $j_*F$ is also the middle extension of
$F|_V$ from $V_0$ to $C_0$. By Theorem [sk-thm-wft-affine-curve-upper] and
Lemma [sk-l-dl-a1-endpoints], $H_c^r(V,F)$ has weights at most $w+r$
for every $r$, and $H_c^0(V,F)=0$. The restriction of $j_*F$ to
the finite set $C_0\setminus V_0$ has weights at most $w$ by
Proposition [sk-p-real-semi], and its cohomology is concentrated in degree zero.
Since $H_c^0(V,F)=0$, the localization sequence shows that $H_c^0(C,j_*F)$
injects into the cohomology of this boundary sheaf, that $H_c^1(V,F)$
surjects onto $H_c^1(C,j_*F)$, that the groups in degree two are
isomorphic, and that higher degrees vanish. The bounds follow.

In general, the connected components of $C$ are defined over a finite
extension $k_m$ of $k_0$, and over $k_m$ each of them is a smooth
geometrically connected curve. On such a component, $j_*F$ is the middle
extension of the restriction of $F$ to the dense open where the component
meets $U$, and this restriction is pure of weight $w$. The group
$H^r_c(C,j_*F)$ is the direct sum of the groups of these components,
compatibly with the $m$th power of Frobenius, so the bound holds over
$k_m$ by the first case, and by the first assertion of
Lemma [sk-lem-wft-infinity-reduction] it holds over $k_0$.
