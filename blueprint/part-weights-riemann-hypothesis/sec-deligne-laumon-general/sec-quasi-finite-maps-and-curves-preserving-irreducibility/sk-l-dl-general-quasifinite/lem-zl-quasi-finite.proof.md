+++
kind = "proof"
of = "lem-zl-quasi-finite"
uses = ["def-weil-complex-weights", "def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "lem-fd-proetale-finite-pushforward-exact", "lem-zl-finite-pushforward", "prop-functor-package", "det-def-sfb-module-lower-shriek", "sk-lem-coefficient-heart", "sk-thm-sf-ctf-stability", "thm-pqf-zmt-factorization", "thm-sf-comp-composition", "sk-lem-pbc-finite"]
+++
Since $Y_0$ is of finite type over a field, it is quasi-compact and
quasi-separated, so Zariski's main theorem in the form of the
quasi-finite factorization [thm-pqf-zmt-factorization] factors $g$
globally as

$$
Z_0\xrightarrow{\ j_0\ }\overline Z_0\xrightarrow{\ \bar g\ }Y_0
$$

with $j_0$ a quasi-compact open immersion and $\bar g$ finite, hence
separated; as $Y_0$ is separated over $k_0$, $\overline Z_0$ is again a
separated finite-type $k_0$-scheme. The factorization is defined over $k_0$, so it base
changes to $k$ and is compatible with the geometric Frobenius
automorphisms; all functors below therefore carry Weil structures. By
the composition isomorphism and the properness law of
[prop-functor-package] (clause 3; for $\Qlb$-coefficients the
composition isomorphism is [thm-sf-comp-composition]), and since a
finite morphism is proper,

$$
Rg_!\simeq R\bar g_!\,j_{0!}\simeq R\bar g_*\,j_{0!}.
$$

*(1).* We work with $\QbarX$-modules on the pro-étale sites. Extension
by zero [det-def-sfb-module-lower-shriek] along the open immersion $j_0$ is
exact on $\Mod(Z_{\mathrm{proét}},\Qlb)$ and preserves constructible
sheaves ([sk-lem-coefficient-heart]); its stalk at a geometric point of
$Z$ is the stalk of the input, and at a geometric point of the
complement it is $0$. The finite morphism $\bar g$ is of finite
presentation, its target being of finite type over a field, so $\bar g_*$
is exact on $\QbarX$-modules and $R\bar g_*\simeq\bar g_*$ term by term
([lem-fd-proetale-finite-pushforward-exact] (2), the pro-étale form of
the exactness of finite direct images [sk-lem-pbc-finite]); since $\bar g_*$
preserves constructibility ([sk-thm-sf-ctf-stability]), it is exact on
$\Cons(\overline Z,\Qlb)$. Thus for a Weil
sheaf $\mathcal F$ we get $Rg_!\mathcal F\simeq\bar g_*j_{0!}\mathcal F$,
a complex concentrated in degree $0$, i.e. $R^ig_!\mathcal F=0$ for
$i\neq0$. Applying the exact functor $\bar g_*j_{0!}$ termwise gives
$\mathcal H^j(Rg_!K)=\bar g_*j_{0!}\mathcal H^j(K)=g_!\mathcal H^j(K)$.

*(2).* Let $K\in D_{\le w}(Z_0)$. By (1) and the composition
isomorphism it suffices to treat the two pieces. For $j_0$: a closed point of $\overline Z_0$ either lies in
$Z_0$, where $j_{0!}K$ has the same stalk with the same local
Frobenius as $K$, or lies outside, where the stalk is $0$; so each
$\mathcal H^j(j_{0!}K)=j_{0!}\mathcal H^j(K)$ receives, from a
filtration of $\mathcal H^j(K)$ with punctually pure quotients of
weights $\le w+j$ as in [def-weil-complex-weights], the filtration
by the (exact) extensions by zero, whose quotients are again punctually
pure of the same weights. Hence $j_{0!}K\in D_{\le w}(\overline Z_0)$.
For $\bar g$: the finite pushforward bound [lem-zl-finite-pushforward]
gives $R\bar g_*j_{0!}K\in D_{\le w}(Y_0)$.

*(3).* A Weil sheaf $\mathcal F$ that is mixed of weights at most $w$
has a finite filtration with punctually pure quotients of weights at
most $w$, so $\mathcal F\in D_{\le w}(Z_0)$ by
[def-weil-complex-weights]. By (2), $Rg_!\mathcal F\in D_{\le w}(Y_0)$,
and by (1) this complex is the sheaf $g_!\mathcal F$ in degree $0$;
so $g_!\mathcal F$ is mixed of weights at most $w$.

*(4) and (5).* Let $y$ be a closed point of $Y_0$ and $\bar y$ a
geometric point over it. By (1), $(g_!\mathcal F)_{\bar y}=
(\bar g_*j_{0!}\mathcal F)_{\bar y}$. Since $\bar g$ is finite, this
stalk is the direct sum of the stalks of $j_{0!}\mathcal F$ at the
finitely many geometric points of the fibre of $\overline Z$ over
$\bar y$ ([sk-lem-pbc-finite]); the summands at points outside $Z$
vanish. Hence $(g_!\mathcal F)_{\bar y}=\bigoplus_{\bar z}\mathcal
F_{\bar z}$, the sum over the geometric points $\bar z$ of $Z$ above
$\bar y$. A nonreduced fibre causes no trouble, since nilpotents do not
change the category of sheaves. The geometric Frobenius $F_y$ permutes
these summands. The geometric points above a closed point $z$ of $Z_0$
with $e=[\kappa(z):\kappa(y)]$ form one cycle of length $e$; the $e$th
power of $F_y$ preserves each summand of this cycle and is conjugate
there to the local Frobenius $F_z$. Hence each eigenvalue $\beta$ of
$F_y$ on this cycle satisfies $\beta^e=\alpha$ for an eigenvalue
$\alpha$ of $F_z$ on $\mathcal F_{\bar z}$. Since $q_z=q_y^e$, the bound
$|\iota(\alpha)|\le q_z^{w/2}$ gives $|\iota(\beta)|\le q_y^{w/2}$,
and the equality $|\iota(\alpha)|=q_z^{w/2}$ gives
$|\iota(\beta)|=q_y^{w/2}$:

$$
|\iota(\beta)|^e=|\iota(\alpha)|=q_z^{w/2}=q_y^{ew/2}.
$$

This proves (4) and, with [def-weil-punctual-weights], (5). For a finite
map $g$ one may take $j_0=\mathrm{id}$, and $g_!=g_*$.
