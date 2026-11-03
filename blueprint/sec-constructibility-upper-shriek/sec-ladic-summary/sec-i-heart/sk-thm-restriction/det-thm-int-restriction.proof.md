+++
kind = "proof"
of    = "det-thm-int-restriction"
uses = ["sk-prop-diagonal-tower", "sk-thm-sf-pf-adic", "sk-prop-proper-base-change-unbounded", "sk-prop-p1-adjunction-rational", "det-cor-affine-space-rational", "sk-lem-int-tensor", "det-prop-closed-adjoint-constructible", "sk-prop-open-coefficients", "det-thm-restriction-local", "sk-prop-sf-existence"]
+++
*Projective line and affine space.* [sk-prop-diagonal-tower] constructs the
cycle class $\delta_{\mathcal O_E}$, the trace, and the two integration
identities directly over $\mathcal O_E$, as morphisms and equalities in
$D((-)_{\mathrm{proét}},\mathcal O_E)$. With the projection formula of [sk-thm-sf-pf-adic] and proper
base change ([sk-prop-proper-base-change-unbounded]), the unit, counit and triangle identities
in the proof of [sk-prop-p1-adjunction-rational] work over $\mathcal O_E$.
Together with the argument of [det-cor-affine-space-rational], this gives
isomorphisms of functors from $\Loc(\Dbc(Y,\mathcal O_E))$ to
$\Loc(\Dbc(\mathbf P^1_Y,\mathcal O_E))$, respectively
$\Loc(\Dbc(\mathbf A^d_Y,\mathcal O_E))$,

$$
q^!\simeq q^*(1)[2]\quad(q:\mathbf P^1_Y\to Y),\qquad
p^!\simeq p^*(d)[2d]\quad(p:\mathbf A^d_Y\to Y).
$$

These functors preserve $\Dbc(-,\mathcal O_E)$ by
[sk-lem-int-tensor].

*Closed immersions.* For a closed immersion $i:Z\hookrightarrow X$, the proof
of [det-prop-closed-adjoint-constructible] applies with
$\mathcal O_E$-coefficients, using [sk-prop-open-coefficients] for the finiteness of
$Rj_*$: for $K\in\Dbc(X,\mathcal O_E)$,
$i^!K\simeq R\underline\Gamma_ZK\in\Dbc(Z,\mathcal O_E)$.

*General $f$.* With finite affine covers and closed immersions
$U\hookrightarrow\mathbf A^d_V$ as in [det-thm-restriction-local],
composition of compactly supported direct images and uniqueness of right
adjoints give $u^*f^!\simeq i^!p^!v^*$ as functors
$\Loc(\Dbc(Y,\mathcal O_E))\to\Loc(\Dbc(U,\mathcal O_E))$, so
$u^*f^!K\in\Dbc(U,\mathcal O_E)$ for each open $U$ of the cover. The conditions
defining $\Dbc(-,\mathcal O_E)$ are local for a finite open cover. Boundedness
and constructibility of the reduction are local as in the rational case.
Derived completeness is local because restriction to an open commutes with
reduction modulo $\pi_E^n$ and with $R\varprojlim$, and restrictions to the
opens of a cover are jointly conservative. Hence
$f^!K\in\Dbc(X,\mathcal O_E)$. Since the inclusions
$\Dbc(-,\mathcal O_E)\subset\Loc(\Dbc(-,\mathcal O_E))$ are full, the adjunction
of [sk-prop-sf-existence] restricts to $\Dbc$. This completes the proof of the
existence theorem ([sk-thm-existence]) for $\Lambda=\mathcal O_E$.
