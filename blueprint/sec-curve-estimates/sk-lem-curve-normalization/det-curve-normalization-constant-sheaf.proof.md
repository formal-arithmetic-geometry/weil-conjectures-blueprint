+++
kind = "proof"
of = "det-curve-normalization-constant-sheaf"
+++
*Part 1.* For a one-dimensional component $C_i$, the normalization
$C_i^{\nu}\to C_i$ is finite, surjective and birational, and $C_i^{\nu}$ is
smooth over the perfect field $k$ ([lem-sc-normalization-properties]); a
zero-dimensional component is a reduced point, i.e. $\operatorname{Spec}k$,
and is its own normalization. Hence $a$ is finite and surjective. The set of
normal points of $C$ not lying on two components is open and dense in each
component, and $a$ is an isomorphism over it
([lem-sc-normalization-properties](b)); its complement $Z$ is a proper closed
subset of each one-dimensional component and contains no isolated point, so
it is a finite set of closed points.

*Part 2.* By the finite stalk formula ([lemma-weil-pbc-finite-stalk-formula])
$(a_*\underline M)_{\bar x}=\prod_{\bar y\mapsto\bar x}M=M^b$, the product
over the $b$ geometric points of the fibre, and the unit sends $m$ to
$(m,\dots,m)$, the germ of the pulled-back constant section. Surjectivity of
$a$ gives $b\geq1$, so the diagonal is injective, and injectivity on all
geometric stalks gives injectivity of $\eta$
([lemma-weil-pbc-geometric-stalk-conservative]). Over $C\setminus Z$ we have
$b=1$ and $\eta_{\bar x}$ is the identity, so $Q$ is supported on $Z$ with
the stated stalks.

*Part 3.* The direct image $a_*$ is exact
([lemma-weil-pbc-finite-direct-image-exact]), so the Leray spectral sequence
degenerates and $H^q(C,a_*\underline M)=H^q(C^{\mathrm{nor}},\underline M)$.
By [det-curve-finite-support-acyclic], $H^q(C,Q)=0$ for $q>0$ and
$H^0(C,Q)=\bigoplus_{z\in Z}Q_{\bar z}$. The long exact sequence of
$0\to\underline M\to a_*\underline M\to Q\to0$ gives the claims.

*Part 4.* By base change, $C^{\mathrm{nor}}_{k'}$ is a finite disjoint union
of smooth curves and points ([lem-sc-base-change-curve]), hence normal, and
$a_{k'}$ is finite; it is an isomorphism over the dense open
$(C\setminus Z)_{k'}$, hence birational. $C_{k'}$ is reduced because $C$ is
reduced and $k$ is perfect. A finite birational morphism from a normal scheme
is the normalization, so $a_{k'}$ is the normalization of $C_{k'}$. The
finite base change isomorphism ([lemma-weil-pbc-finite-exchange]) identifies
$\pi^{-1}a_*\underline M$ with $a_{k'*}\underline M$ for
$\pi:C_{k'}\to C$, compatibly with the units, and the geometric fibres of
$a_{k'}$ over $z\otimes k'$ are those of $a$ over $z$. So the pullback of the
sequence for $C$ is the sequence for $C_{k'}$, with the same cokernel stalks
$M^b/\Delta M$, and [det-curve-finite-support-acyclic] identifies the
cohomology of the cokernels.
