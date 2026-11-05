+++
kind = "proof"
of = "theorem-f-shriek-ell-adic-coefficients--1"
order = 616003
uses = ["proposition-direct-image-along-open-immersion--1", "proposition-ell-adic-cycle-class-diagonal"]
+++
In the geometric argument reproduced below, take $\Lambda=\mathcal O_E$; the final paragraph supplies precisely the integral inputs needed by the factorization.

Choose finite affine covers of $X$ and $Y$ and closed immersions
$U\hookrightarrow\mathbf A^d_V$. Here $u:U\to X$ and $v:V\to Y$ are the
inclusions of the affine opens, and $i:U\hookrightarrow\mathbf A^d_V$ and
$p:\mathbf A^d_V\to V$ are the two factors. Then $u^*f^!\simeq i^!p^!v^*$
(Proposition [proposition-composition-open-restriction-compactifications-f]), and being in $\Dbc$ is local
on $X$, so it suffices to show that $p^!$ and $i^!$ preserve $\Dbc$.

For $E$ and $\overline{\mathbf Q}_\ell$ we argue as in Section [sec-Finite-coefficients-2]. We use
Proposition [proposition-projective-line-rational-coefficients], the
adjunction $j_!\dashv j^*$ for $\mathbf A^1_V\subset\mathbf P^1_V$, and
Proposition [proposition-composition-open-restriction-compactifications-f]
applied $d$ times. They give $p^!\simeq p^*(d)[2d]$, which preserves
$\Dbc$. For $i$, let $j'$ be the inclusion of the open complement of $U$ in
$\mathbf A^d_V$. The localization triangle before
Example [example-closed-support], with $j'$ in place of $j$, shows that
$i^!K\in\Dbc(U,\Lambda)$ for $K\in\Dbc(\mathbf A^d_V,\Lambda)$. Indeed, its
third term $Rj'_*j'^*K$ is in $\Dbc$ by
Proposition [proposition-direct-image-along-open-immersion], and
$i^*i_*=\mathrm{id}$.

For $\mathcal O_E$ that argument applies once its ingredients are
available with integral coefficients. They are as follows. The adjunction
for the projective line comes from
Proposition [proposition-ell-adic-cycle-class-diagonal], with the
triangle identities verified as in
Proposition [proposition-projective-line-rational-coefficients]. The
projection formula is
Lemma [lemma-projection-formula-integral-coefficients]. Inverse
image and tensor product preserve $\Dbc(-,\mathcal O_E)$ by
Lemma [lemma-inverse-image-tensor-product]. The finiteness of $Rj_*$
and proper base change are
Propositions [proposition-direct-image-along-open-immersion]
and [proposition-proper-base-change-localizing-categories]. We also
use that derived completeness is local on $X$; it is part of the criterion
for $\Dbc$ with $\mathcal O_E$-coefficients. Finally, $Rf_!$ preserves
$\Dbc$ (Proposition [proposition-construction-independence-rf-shriek]),
and so the adjunction restricts to $\Dbc$.

*Source:* the proof of Theorem [theorem-f-shriek-ell-adic-coefficients].
