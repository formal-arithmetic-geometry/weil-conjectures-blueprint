+++
kind = "proof"
of = "sk-thm-restriction"
uses = ["sk-lem-sf-mate", "sk-prop-p1-adjunction-rational", "sk-lem-formal-closed-support", "sk-prop-open-coefficients", "sk-prop-diagonal-tower", "sk-thm-sf-pf-adic", "sk-lem-int-tensor", "sk-prop-proper-base-change-unbounded", "sk-prop-sf-comp-coherence"]
+++
Recall that $\Dctf=\Dbc$ for these $\Lambda$. Choose finite affine covers of $X$ and $Y$ and
closed immersions $U\hookrightarrow\mathbf A^d_V$; then $u^*f^!\simeq i^!p^!v^*$
([sk-lem-sf-mate]), and being in $\Dbc$ is local on $X$.

For $E$ and $\Qlb$, $p^!$ and $i^!$ preserve $\Dbc$. Indeed, for a projection
$p:\mathbf A^d_V\to V$, [sk-prop-p1-adjunction-rational], the adjunction $j_!\dashv j^*$ for
$\mathbf A^1_V\subset\mathbf P^1_V$ and [sk-lem-sf-mate] applied $d$ times give
$p^!\simeq p^*(d)[2d]$, which preserves $\Dbc$. For a closed immersion $i:Z\hookrightarrow X$
with complement $j$, the local cohomology functor $R\underline\Gamma_Z$ is right adjoint to
$i_*=Ri_!$ ([sk-lem-formal-closed-support] (1)), so $i^!\simeq R\underline\Gamma_Z$, and the
localization triangle

$$
i_*R\underline\Gamma_ZK\longrightarrow K\longrightarrow Rj_*j^*K
\longrightarrow i_*R\underline\Gamma_ZK[1]
$$

shows that $i^!K\in\Dbc(Z,\Lambda)$ for $K\in\Dbc(X,\Lambda)$, since the third term is in
$\Dbc$ by [sk-prop-open-coefficients] and $i^*i_*=\mathrm{id}$.

For $\mathcal O_E$ the same argument applies, with [sk-prop-diagonal-tower] for the projective
line, [sk-thm-sf-pf-adic] and [sk-lem-int-tensor] for the projection formula and inverse image,
and [sk-prop-open-coefficients] and [sk-prop-proper-base-change-unbounded]; derived completeness
is local on $X$. The adjunction restricts because $Rf_!$ preserves $\Dbc$
([sk-prop-sf-comp-coherence]).
