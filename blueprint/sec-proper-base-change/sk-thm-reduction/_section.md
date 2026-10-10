+++
id = "sk-thm-reduction"
kind = "section"
title = "Reduction to $\\Pone$"
order = 1184
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_of_projectiveLine_of_isProper"]
uses = ["sk-def-conv", "sk-def-pbc", "sk-thm-chow", "sk-thm-groth-ss", "sk-thm-iff", "sk-thm-p1"]
+++
*Theorem (sketch).*

Let $\Lambda$ be a commutative ring. Assume that $\Pone_S\to S$ satisfies
$\mathrm{PBC}$ with $\Lambda$-coefficients for every scheme $S$ (in the
sense of [sk-def-pbc]: the exchange morphism is an isomorphism, for every
base change, on every object of $\Dplus$ of $\Lambda$-module sheaves with
torsion cohomology sheaves). Then every proper morphism of schemes
satisfies $\mathrm{PBC}$ with $\Lambda$-coefficients.

## Proof

*Change of coefficients.* For $N\ge1$ put $\Lambda_N=\Lambda/N\Lambda$, a
ring which is torsion as an additive group. Restriction of scalars along
$\Lambda\to\Lambda_N$ is exact and conservative, commutes with $g^{-1}$ and
$f_*$, and commutes with $Rf_*$ (an injective sheaf of $\Lambda_N$-modules
is limp, hence $f_*$-acyclic as a sheaf of $\Lambda$-modules); it therefore
carries the exchange morphism over $\Lambda_N$ to the exchange morphism over
$\Lambda$. Since a complex of $\Lambda_N$-module sheaves has torsion
cohomology, the hypothesis $\mathrm{PBC}_\Lambda(\Pone_S\to S)$ gives
$\mathrm{PBC}_{\Lambda_N}(\Pone_S\to S)$ for every $S$ and every $N$.
Conversely, for proper $f$, $\mathrm{PBC}_{\Lambda_N}(f)$ for all $N$
implies $\mathrm{PBC}_\Lambda(f)$. Indeed, let $K\in\Dplus(X_{\Et},\Lambda)$
have torsion cohomology sheaves and fix a degree $m$. The triangle
$\tau_{\le m}K\to K\to\tau_{>m}K$ and the vanishing of
$\mathcal H^{j}$ of $g^{-1}Rf_*\tau_{>m}K$ and of
$Rf'_*g'^{-1}\tau_{>m}K$ for $j\le m$ show that $\mathcal H^m(\Ex_{\square,K})$
is $\mathcal H^m(\Ex_{\square,\tau_{\le m}K})$; as $\tau_{\le m}K$ is bounded,
induction on its number of nonzero cohomology sheaves (truncation triangles
and the five lemma) reduces to $K=F[-q]$ with $F$ a torsion sheaf of
$\Lambda$-modules. Then $F=\varinjlim_NF[N]$, and $g^{-1}$, $R^qf_*$ and
$R^qf'_*$ commute with filtered colimits ($f$, $f'$ are quasi-compact and
quasi-separated), so it suffices to treat each $F[N]$, a sheaf of
$\Lambda_N$-modules, where the exchange is an isomorphism by
$\mathrm{PBC}_{\Lambda_N}(f)$ and the compatibility of restriction of
scalars with exchange. Hence it suffices to prove the theorem for each
$\Lambda_N$; from now on $\Lambda$ is torsion as an additive group, so that
$\mathrm{PBC}_\Lambda$ and $\mathrm{IA}_\Lambda$ are equivalent for proper
morphisms by [sk-thm-iff], and every sheaf of $\Lambda$-modules is torsion.

We use the following elementary manipulations, each argued where it
occurs: finite morphisms satisfy PBC; PBC composes; PBC cancels
along a proper surjection; $\Pone$ gives $\Pqn$; PBC is étale
local on the target.

*Reduction to an affine base.* For quasi-compact
quasi-separated $f$, the restriction of $R^qf_*F$ to an étale
$V\to Y$ is the sheafification of
$U\mapsto H^q(X\times_YU,F|)$ (and likewise for the cohomology sheaves of
$Rf_*K$, with hypercohomology), compatible with exchange; exchange is
therefore an isomorphism iff it is one over the geometric points of
an étale cover of $Y$, and geometric stalks are conservative: PBC
is étale local on the target, so we may assume $Y$ affine.

*Chow's factorization.* By [sk-thm-chow] there are
$\pi:\widetilde X\to X$ proper surjective and a closed immersion
$i_Y:\widetilde X\hookrightarrow\Pqn_Y$ with $f\pi=q_Yi_Y$; the
graph map $i_X=(\pi,i_Y):\widetilde X\hookrightarrow\Pqn_X$ is a
closed immersion over $X$, so $\pi=q_Xi_X$.

*Closed immersions are finite, and finite morphisms satisfy
PBC.* After base change to the strict henselization at a geometric
point $\bar y$ the finite fibre is a finite disjoint union of
strictly henselian local schemes, whence
$(f_*F)_{\bar y}=\prod_{\bar x\to\bar y}F_{\bar x}$ as a finite
product; $f_*$ is exact, $R^qf_*=0$ for $q>0$, exchange is the
identity summand-wise, and the same holds after every base change.
As $f_*$ and $f'_*$ are exact, $Rf_*K$ and $Rf'_*g'^{-1}K$ are computed
termwise, and the derived exchange on a complex $K$ is the termwise
underived one, an isomorphism. Thus $\mathrm{PBC}(i_X)$ and
$\mathrm{PBC}(i_Y)$ hold.

*From $\Pone$ to $\Pqn$.* The symmetric-product morphism

$$
\sigma_n:(\Pone_S)^n\to\Pqn_S,\quad
([x_i:y_i])_i\mapsto[F_0:\dots:F_n],\ \
\textstyle\prod_{i=1}^n(x_it+y_i)=\sum_jF_jt^j,
$$

is finite (each $z_i=x_i/y_i$ is integral over the elementary
symmetric subring) and surjective (over an algebraically closed
field every binary form of degree $n$ factors into linear forms).
The projection $(\Pone_T)^n\to T$ is a composite of $n$
projective-line projections over successive bases: by the
hypothesis (for $\Lambda_N$-coefficients, after the change of coefficients
above; [sk-thm-p1] verifies it) and the composition step below it
satisfies PBC;
$\sigma_n$ being finite satisfies PBC; and since the composite
$(\Pone_T)^n\to\Pqn_T\to T$ is the product projection, cancellation
along the surjective $\sigma_n$ (below) gives PBC for
$\Pqn_T\to T$.

*Composition.* If $f,h$ are proper with $\mathrm{PBC}(f)$,
$\mathrm{PBC}(h)$, then $\mathrm{PBC}(hf)$: convert both to
$\mathrm{IA}$ via [sk-thm-iff]; $f_*I$ is injective for $I$
injective ($f_*$ is right adjoint to the exact $f^{-1}$), the
$q>0$ higher direct images of $a^{-1}I$ along $f'$ vanish, and the
conjugates are identified by the degree-zero exchange used in
[sk-thm-iff]; in the spectral sequence [sk-thm-groth-ss] for
the composite only the $q=0$ row survives, killed in positive
degrees by $\mathrm{IA}(h)$; convert back. Hence
$\mathrm{PBC}(\pi)$ ($\pi=q_Xi_X$) and $\mathrm{PBC}(f\pi)$
($f\pi=q_Yi_Y$).

*Cancellation.* If $f$ is proper surjective with
$\mathrm{PBC}(f)$, $\mathrm{PBC}(hf)$, then $\mathrm{PBC}(h)$:
convert to $\mathrm{IA}$; an injective $I$ on $Y$ embeds
$I_{\bar y}\hookrightarrow J_{\bar x}$ into an injective $J$ on $X$
over the fibre, so $I\to f_*J$ splits and $I$ is a direct summand
of $f_*J$; by the spectral sequence [sk-thm-groth-ss] together
with $\mathrm{IA}(f)$ and $\mathrm{IA}(hf)$ the higher direct
images of $b^{-1}f_*J\cong f'_*a^{-1}J$ vanish, and vanishing passes
to direct summands; convert back. Cancelling the surjective $\pi$ in
$f\pi$ gives $\mathrm{PBC}_{\Lambda_N}(f)$ for every $N$, hence
$\mathrm{PBC}_\Lambda(f)$ by the change of coefficients.
