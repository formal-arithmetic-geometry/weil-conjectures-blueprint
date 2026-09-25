+++
id = "thm-pur-vector-triangular"
kind = "theorem"
title = "Thom trace and diagonal"
order = 2060
uses = ["def-coefficient-twists-detailed", "def-exchange-projection", "def-pur-conventions", "def-pur-td-datum", "def-pur-vector-bundle-thom-class", "def-pur-vector-bundle-zero-section", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "lem-pur-divisor-class", "lem-pur-kunneth-supported", "lem-pur-td-kernel", "lem-pur-vector-diagonal-class", "thm-pur-localized-top-chern", "thm-pur-rank-one-local-calculation", "thm-pur-td-criterion", "thm-pur-vector-bundle-thom"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $\pi:E\to B$ be a
vector bundle of constant
rank $r$. With the
trace $\operatorname{tr}_\pi$ of [thm-pur-vector-bundle-thom],
the diagonal class $\operatorname{cl}_{\Delta_\pi}$ of
[lem-pur-vector-diagonal-class], and the twist
$L_E=\Lambda_E(r)[2r]$ of [def-coefficient-twists-detailed], the two
triangular composites of
[def-pur-td-datum] for $(\pi,L_E)$ are the identity, naturally in
$A\in D^b_{ctf}(E,\Lambda)$ and $K\in D^b_{ctf}(B,\Lambda)$.
Consequently, by [thm-pur-td-criterion],

$$
R\pi^!K\;\cong\;L\pi^*K(r)[2r]
$$

for every $K\in D^b_{ctf}(B,\Lambda)$, the tensor and pullback operations
being those of
[def-weil-derived-pullback-tensor-hom], [def-weil-derived-tensor], and

$$
\omega_\pi=R\pi^!\Lambda_B\;\cong\;\Lambda_E(r)[2r].
$$

## Proof

*Step 0: locality.* Every ingredient is compatible with base change
and with étale localization: the Thom class and the trace by
[thm-pur-vector-bundle-thom], the diagonal class because it is the
pullback of the Thom class ([lem-pur-vector-diagonal-class]), and the
unit and the counit by their definitions in [def-pur-td-datum]
together with the kernel identification [lem-pur-td-kernel], whose
statement is a base-change isomorphism; the projection formula is the
canonical transformation of [def-exchange-projection]. Being an
identity is a local condition, so we may replace $B$ by an étale cover
over which $E$ is trivial and assume
$E=\mathbf A^r_B=\Spec\mathcal O_B[u_1,\dots,u_r]$ with zero section
$u=0$.

*Step 1: the two classes in coordinates.* The trivialization presents
$E$ as a direct sum of the coordinate line bundles, so the direct-sum
clause of [def-pur-vector-bundle-thom-class] and the rank-one case
[thm-pur-localized-top-chern](L1) with the divisor $\{u_i=0\}$ give

$$
\operatorname{thom}(E)=\prod_{i=1}^{r}\operatorname{thom}(\mathcal O_B)
=\prod_{i=1}^{r}\operatorname{cl}\bigl(\{u_i=0\}\bigr)
=\prod_{i=1}^{r}\kappa(u_i),
$$

the last equality being [lem-pur-divisor-class](a). The morphism
$\delta(v_1,v_2)=v_2-v_1$ carries the divisor $\{u_i=0\}$ to
$\{v_{2,i}-v_{1,i}=0\}$, so the pullback clause of
[lem-pur-divisor-class](b), applied factor by factor, together with
[lem-pur-vector-diagonal-class] gives

$$
\operatorname{cl}_{\Delta_\pi}
=\delta^*\operatorname{thom}(E)
=\prod_{i=1}^{r}\operatorname{cl}\bigl(\{v_{2,i}-v_{1,i}=0\}\bigr).
$$

*Step 2: the composites are the double integral of the diagonal
class.* This is the definitions read out, with [def-pur-td-datum] for
the shape of the maps, the twist $L_E=\Lambda_E(r)[2r]$ of
[def-coefficient-twists-detailed] for the coefficients, and
[lem-pur-td-kernel] for the identification
that converts them into integrals. At $A=\Lambda_E$ the unit is the
composite

$$
\Lambda_E\xrightarrow{\ \sim\ }
Rp_{2!}\bigl(p_1^*\Lambda_E\otimes\Delta_!\Lambda_E\bigr)
\xrightarrow{\ \operatorname{id}\otimes\operatorname{cl}_{\Delta_\pi}\ }
Rp_{2!}\bigl(p_1^*\Lambda_E\otimes p_2^*L_E\bigr)
\xrightarrow{\ \sim\ }
L\pi^*R\pi_!\Lambda_E\otimes L_E ,
$$

whose first arrow is the identification coming from
$p_2\Delta=\mathrm{id}_E$ and the projection formula of
[def-exchange-projection], and whose last arrow is
[lem-pur-td-kernel] with $K=\Lambda_E$; the counit is the projection
formula followed by $\operatorname{id}\otimes\operatorname{tr}_\pi$, as
in [def-pur-td-datum]. The first triangular composite of
[def-pur-td-datum] is therefore, after substituting Step 1, the
composite

$$
R\Gamma_c(E,L_E)
\xrightarrow{\ \smile\,\prod_{i}\operatorname{cl}(\{v_{2,i}-v_{1,i}=0\})\ }
R\Gamma_c(W,L_E\boxtimes L_E)
\xrightarrow{\ \sim\ }
R\Gamma_c(E,L_E)\otimes R\Gamma_c(E,L_E)
\xrightarrow{\ \operatorname{id}\otimes\operatorname{tr}_\pi\ }
R\Gamma_c(E,L_E),
$$

the middle arrow being the Künneth identification recorded in
[lem-pur-td-kernel]. The second composite is the same composite with
the roles of $v_1$ and $v_2$ interchanged: the two projections of
$W=E\times_BE$ are conjugate under the automorphism
$T(v_1,v_2)=(v_2,v_1)$, which interchanges the projections and
fixes the diagonal. Each defining equation in Step 1 is multiplied
by the unit $-1$; its supported Cartier class is unchanged by
[lem-pur-divisor-class]. Thus $T$ preserves
$\operatorname{cl}_{\Delta_\pi}$.

*Step 3: the integral of the diagonal class.* The divisors
$\{v_{2,i}-v_{1,i}=0\}$, $i=1,\dots,r$, are smooth over $B$ and meet
transversally in the diagonal, so [lem-pur-kunneth-supported] exhibits
$\prod_i\operatorname{cl}(\{v_{2,i}-v_{1,i}=0\})$ as the exterior product
of the $r$ rank-one divisor classes, one in each factor of
$W=\mathbf A^r_{v_1}\times_B\mathbf A^r_{v_2}$. Integrating out $v_2$
factor by factor therefore gives

$$
\int_{v_2}\ \prod_{i=1}^{r}\operatorname{cl}\bigl(\{v_{2,i}-v_{1,i}=0\}\bigr)
=\prod_{i=1}^{r}1=1 ,
$$

because each factor is a residue computation in the coordinate
$v_{2,i}-v_{1,i}$, which is a local coordinate at
$v_{2,i}=v_{1,i}$, and the residue is normalized to be $1$ by
[thm-pur-rank-one-local-calculation]; the same computation with
$v_1$ in place of $v_2$ gives $\int_{v_1}(\dots)=1$ as well.

*Step 4: the composites are the identity.* By Step 3 the composite of
Step 2 is the map induced by the unit of the Thom isomorphism: indeed
$\tau_E(\Lambda_B)=\operatorname{thom}(E)$ by
[def-pur-vector-bundle-thom-class], and
$\operatorname{tr}_\pi=\tau_E^{-1}$ by
[thm-pur-vector-bundle-thom], so that the composite is
$\operatorname{tr}_\pi\circ\tau_E=\operatorname{id}$. This proves the
first triangular identity in the trivial case, and Step 2 gives the second
by the symmetry $T$. For general $A$ and $K$ the two composites are
obtained from the case $A=\Lambda_E$, $K=\Lambda_B$ by the projection
formula: by [def-pur-td-datum] the unit is
$\operatorname{id}\otimes\operatorname{cl}_{\Delta_\pi}$ and the counit is
$\operatorname{id}\otimes\operatorname{tr}_\pi$ tensored with the
coefficient object along [def-exchange-projection], so that the
composites are $\operatorname{id}_A\otimes(\dots)$ and
$\operatorname{id}_K\otimes(\dots)$ of the composites already shown to be
the identity. Undoing the étale cover of Step 0 gives the identities over
the original $B$.

*Step 5: the conclusion.* By [thm-pur-td-criterion] the
trace–diagonal datum for $(\pi,L_E)$ gives $R\pi_!\dashv G_{L_E}$,
whence the identification $R\pi^!K\cong L\pi^*K(r)[2r]$ and
$\omega_\pi\cong\Lambda_E(r)[2r]$.
