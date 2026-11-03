+++
kind  = "proof"
of    = "sbc-thm-algebraically-closed-invariance"
uses  = ["lem-sc-kummer-les", "lem-sc-primitive-root", "lem-sc-genus-invariant", "thm-sc-jacobian-representability", "thm-av-final", "def-sc-pic0", "lem-sc-pic-proper-decomposition"]
+++
A smooth separated curve over $k$ is a finite disjoint union of connected
components, each either a point (where both sides are the cohomology of a
separably closed field, and the map is an isomorphism) or a smooth separated
connected curve; cohomology takes the union to a product and the pullback map
respects it. For a connected curve the assertion is
[thm-sc-constant-invariance] of the Jacobian chapter (applied with $n=d$),
which proves it for the constant sheaf $\mathbf F_d$; this is the displayed
pullback map by the definition of the etale cohomology of
[def-weil-pbc-etale-cohomology].

*Compatibility in the proper case.* Let $C$ be proper and connected, of genus
$g$; then $C_{k'}$ has the same genus ([lem-sc-genus-invariant]), so
[thm-sc-proper-cohomology] gives $\mathbf Z/d$, $(\mathbf Z/d)^{2g}$,
$\mathbf Z/d$ on both sides. All maps below are canonical pullbacks, and the
Kummer sequence is natural in the base field. In degree $0$ the identification
is $\mu_d(k)=\mu_d(k')$: a primitive $d$-th root of unity of $k$ stays primitive
in $k'$ ([lem-sc-primitive-root]). In degree $1$ it is
$H^1(C,\mu_d)=\operatorname{Pic}(C)[d]$ ([lem-sc-kummer-les]; the units of $C$
are the $d$-divisible group $k^\times$) together with
$\operatorname{Pic}^0(C)=J_C(k)$ ([thm-sc-jacobian-representability]); the
pullback is $J_C[d](k)\to J_C[d](k')$, which is bijective because $J_C[d]$ is a
finite etale $k$-group scheme ([thm-av-final](b),(c)) and
$J_{C_{k'}}=(J_C)_{k'}$ ([thm-sc-jacobian-representability]). In degree $2$ it
is $\operatorname{Pic}(C)/d\to\operatorname{Pic}(C_{k'})/d$, where both sides
are $\mathbf Z/d$ via the degree ([def-sc-pic0],
[lem-sc-pic-proper-decomposition]), and the degree is preserved by base
change. So the three identifications are matched by the pullback maps.
