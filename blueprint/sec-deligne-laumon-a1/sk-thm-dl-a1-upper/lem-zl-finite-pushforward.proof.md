+++
kind  = "proof"
of    = "lem-zl-finite-pushforward"
+++
A finite morphism is proper, so $Rg_!=Rg_*$ by the properness law of
[prop-functor-package].

*Exactness and stalks.* Let $\mathcal F\in\Cons(Z,\Qlb)$ and let $\bar y$ be a
geometric point of $Y$. By proper base change ([sk-thm-sfb-proper-base-change])
$(Rg_*\mathcal F)_{\bar y}\simeq R\Gamma(Z_{\bar y},\mathcal F|_{Z_{\bar y}})$. The
fibre $Z_{\bar y}$ is finite over the separably closed field $\kappa(\bar y)$, so
its reduction is a finite disjoint union of geometric points $\bar x$ over
$\bar y$; on each of them sections are exact ([sk-prop-pe-condensed-point],
[sk-cor-pe-wc-sections]). Hence

$$
(Rg_*\mathcal F)_{\bar y}\simeq\bigoplus_{\bar x\mapsto\bar y}\mathcal F_{\bar x}
$$

in degree $0$. The sheaves $R^ig_*\mathcal F$ are constructible
([sk-thm-sf-ctf-stability]), and a constructible $\Qlb$-sheaf with vanishing
geometric stalks is zero, since on each stratum of [sk-lem-coefficient-heart](3)
it is locally free of rank equal to its stalk dimension. So $R^ig_*\mathcal F=0$
for $i>0$, $g_*$ is exact on $\Cons(Z,\Qlb)$, and
$\mathcal H^j(Rg_*K)=g_*\mathcal H^j(K)$. The stalk isomorphism is natural, so it
intertwines the Weil structures. Fix $j$ and choose a
finite Weil filtration of $\mathcal H^j(K)$ whose nonzero quotients
$\mathcal Q_i$ are punctually pure in the sense of
[def-weil-punctual-weights], of weights $u_i\le w+j$, as
provided by [def-weil-complex-weights]. Exactness pushes this
filtration forward. It remains to check that $g_*\mathcal Q_i$ is
punctually pure of weight $u_i$. Let $y$ be closed and use the stalk formula above. The geometric
Frobenius permutes the finitely many points $x$ over $y$; on an orbit
of length $f$, its $f$-th power on the corresponding summand is the
local Frobenius $F_x$. If $\mu$ is an eigenvalue on that orbit, then
$\mu^f$ is an eigenvalue of $F_x$. Since $\mathcal Q_i$ is pure,

$$
|\iota(\mu)|^f=|\iota(\mu^f)|
=q_x^{u_i/2}=(q_y^f)^{u_i/2},
$$

so $|\iota(\mu)|=q_y^{u_i/2}$. Thus each $g_*\mathcal Q_i$ is
punctually pure of weight $u_i$, and the pushed-forward filtration makes
$g_*\mathcal H^j(K)$ mixed of weights at most $w+j$. This holds for
every $j$, hence $Rg_*K\in D_{\le w}(Y_0)$ by
[def-weil-complex-weights].
