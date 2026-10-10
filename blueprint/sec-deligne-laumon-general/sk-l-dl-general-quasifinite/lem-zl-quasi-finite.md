+++
id = "lem-zl-quasi-finite"
kind = "lemma"
title = "Quasi-finite morphisms: exactness and upper-weight bound"
order = 2818
lean = ["AlgebraicGeometry.isZero_higherLowerShriek_of_quasiFinite", "AlgebraicGeometry.LAdicWeilSheaf.IsMixedOfWeightsAtMost.higherLowerShriek_zero_of_quasiFinite", "AlgebraicGeometry.LAdicWeilSheaf.HasWeightsAtMost.higherLowerShriek_zero_of_quasiFinite"]
uses = ["def-weil-complex-weights", "def-weil-extension-by-zero", "def-weil-pbc-qbar-category", "lem-zl-finite-pushforward", "lemma-weil-pbc-finite-direct-image-exact", "prop-functor-package", "thm-pqf-zmt-factorization"]
+++
Let $g:Z_0\to Y_0$ be a separated, quasi-finite morphism of finite type
of $k_0$-schemes, with $Y_0$ quasi-separated of finite type over $k_0$.
Let $\mathcal F$ be a constructible $\Qlb$-Weil sheaf on $Z_0$ and
$w\in\mathbf R$.

1. $R^ig_!\mathcal F=0$ for every $i>0$.
1. If $\mathcal F$ is $\iota$-mixed of weights at most $w$, then so is
   $g_!\mathcal F=R^0g_!\mathcal F$.
1. If every local Frobenius eigenvalue of $\mathcal F$ at every closed
   point has weight at most $w$, then the same holds for
   $g_!\mathcal F$.

## Proof

Since $Y_0$ is of finite type over a field, it is quasi-compact and
quasi-separated, so Zariski's main theorem in the form of the
quasi-finite factorization [thm-pqf-zmt-factorization] factors $g$
globally as

$$
Z_0\xrightarrow{\ j_0\ }\overline Z_0\xrightarrow{\ \bar g\ }Y_0
$$

with $j_0$ a quasi-compact open immersion and $\bar g$ finite; in
particular $\overline Z_0$ is again a separated finite-type
$k_0$-scheme. The factorization is defined over $k_0$, so it base
changes to $k$ and is compatible with the geometric Frobenius
automorphisms; all functors below therefore carry Weil structures. By
the composition isomorphism and the properness law of
[prop-functor-package] (clause 3), and since a finite morphism is
proper,

$$
Rg_!\simeq R\bar g_!\,j_{0!}\simeq R\bar g_*\,j_{0!}.
$$

*(1).* Extension by zero [def-weil-extension-by-zero] is exact: its
stalk at a geometric point of $Z$ is the stalk of the input, and at a
geometric point of the complement it is $0$. The finite direct image
$\bar g_*$ is exact by [lemma-weil-pbc-finite-direct-image-exact], so
$R\bar g_*=\bar g_*$. Both statements hold at every finite coefficient
stage and hence, by the common-stage construction of
[def-weil-pbc-qbar-category], for $\Qlb$-coefficients. Thus for a Weil
sheaf $\mathcal F$ we get $Rg_!\mathcal F\simeq\bar g_*j_{0!}\mathcal F$,
a complex concentrated in degree $0$, i.e. $R^ig_!\mathcal F=0$ for
$i\neq0$, and $g_!\mathcal F=R^0g_!\mathcal F=\bar g_*j_{0!}\mathcal F$.
More generally, applying the exact functor $\bar g_*j_{0!}$ termwise
gives $\mathcal H^j(Rg_!K)=\bar g_*j_{0!}\mathcal H^j(K)=g_!\mathcal H^j(K)$
for every Weil complex $K$ and every $j$.

*(2).* We first show the complex form: if $K\in D_{\le w}(Z_0)$, then
$Rg_!K\in D_{\le w}(Y_0)$. By (1) and the composition isomorphism it
suffices to treat the two pieces. For $j_0$: a closed point of
$\overline Z_0$ either lies in $Z_0$, where $j_{0!}K$ has the same stalk
with the same local Frobenius as $K$, or lies outside, where the stalk
is $0$; so each $\mathcal H^j(j_{0!}K)=j_{0!}\mathcal H^j(K)$ receives,
from a filtration of $\mathcal H^j(K)$ with punctually pure quotients of
weights $\le w+j$ as in [def-weil-complex-weights], the filtration by
the (exact) extensions by zero, whose quotients are again punctually
pure of the same weights. Hence $j_{0!}K\in D_{\le w}(\overline Z_0)$.
For $\bar g$: the finite pushforward bound [lem-zl-finite-pushforward]
gives $R\bar g_*j_{0!}K\in D_{\le w}(Y_0)$.

Now let $\mathcal F$ be $\iota$-mixed of weights at most $w$, i.e. it
has a finite filtration whose quotients are punctually $\iota$-pure of
weights $\le w$. Regarded as a complex in degree $0$, this says exactly
$\mathcal F\in D_{\le w}(Z_0)$ by [def-weil-complex-weights]. By the
complex form, $Rg_!\mathcal F\in D_{\le w}(Y_0)$, and by (1) this
complex is the sheaf $g_!\mathcal F$ in degree $0$; reading
[def-weil-complex-weights] in degree $0$, $g_!\mathcal F$ is
$\iota$-mixed of weights at most $w$.

*(3).* By (1), $g_!\mathcal F=\bar g_*(j_{0!}\mathcal F)$. The stalks of
$j_{0!}\mathcal F$ at closed points of $Z_0$ are those of $\mathcal F$,
with the same local Frobenius, and are $0$ at the other closed points
of $\overline Z_0$; so every local Frobenius eigenvalue of
$\mathcal G=j_{0!}\mathcal F$ at a closed point $x$ of $\overline Z_0$
satisfies $|\iota(\alpha)|\le q_x^{w/2}$. Let $y$ be a closed point of
$Y_0$. Since $\bar g$ is finite, the geometric stalk of
$\bar g_*\mathcal G$ at $\bar y$ is the direct sum of the stalks of
$\mathcal G$ at the finitely many geometric points $\bar x$ over
$\bar y$, and the geometric Frobenius at $y$ permutes these summands.
On an orbit of length $e$, belonging to a closed point $x$ over $y$
with $q_x=q_y^e$, the $e$-th power of the Frobenius at $y$ restricted
to the corresponding summand is the local Frobenius $F_x$. Hence if
$\beta$ is an eigenvalue of the Frobenius at $y$ on that orbit, then
$\beta^e$ is an eigenvalue of $F_x$ on $\mathcal G_{\bar x}$, and

$$
|\iota(\beta)|^e=|\iota(\beta^e)|\le q_x^{w/2}=(q_y^e)^{w/2},
$$

so $|\iota(\beta)|\le q_y^{w/2}$. Every eigenvalue of the Frobenius at
$y$ on $(g_!\mathcal F)_{\bar y}$ occurs on some orbit, which proves
(3).
