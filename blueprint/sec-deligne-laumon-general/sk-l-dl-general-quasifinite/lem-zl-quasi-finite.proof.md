+++
kind = "proof"
of = "lem-zl-quasi-finite"
uses = ["def-weil-complex-weights", "def-weil-weil-sheaf-complex", "lem-zl-finite-pushforward", "prop-functor-package", "sk-cor-pe-wc-sections", "sk-def-sfb-module-lower-shriek", "sk-lem-coefficient-heart", "sk-prop-pe-condensed-point", "sk-thm-sf-ctf-stability", "sk-thm-sfb-proper-base-change", "thm-pqf-zmt-factorization"]
+++
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

*(1).* We work with $\QbarX$-modules on the pro-étale sites. Extension
by zero [sk-def-sfb-module-lower-shriek] along the open immersion $j_0$ is
exact on $\Mod(Z_{\mathrm{proét}},\Qlb)$ and preserves constructible
sheaves ([sk-lem-coefficient-heart]); its stalk at a geometric point of
$Z$ is the stalk of the input, and at a geometric point of the
complement it is $0$. For the finite morphism $\bar g$ and
$\mathcal G\in\Cons(\overline Z,\Qlb)$, the complex $R\bar g_*\mathcal G$
lies in $\Dbc(Y,\Qlb)$ ([sk-thm-sf-ctf-stability]). Let $\bar y$ be a
geometric point of $Y$. Since $\bar g$ is proper, proper base change
([sk-thm-sfb-proper-base-change]) gives
$(R\bar g_*\mathcal G)_{\bar y}\simeq R\Gamma(\overline Z_{\bar y},\mathcal G|_{\overline Z_{\bar y}})$.
The fibre $\overline Z_{\bar y}$ is finite over a separably closed field,
so up to nilpotents, to which the pro-étale topos is insensitive, it is
a finite disjoint union of spectra of separably closed fields. On each
of these the pro-étale topos is that of condensed sets
([sk-prop-pe-condensed-point]), and the affine is weakly contractible,
so taking sections is exact ([sk-cor-pe-wc-sections]). Hence
$\mathcal H^i(R\bar g_*\mathcal G)$ has zero stalks for $i>0$. A
constructible $\Qlb$-sheaf with zero stalks is zero: by
[sk-lem-coefficient-heart] (3) it has a finite filtration with
subquotients $a_!L$, $L$ lisse, i.e. locally free of rank equal to its
stalk dimension, and the stalks of the subquotients vanish since stalks
are exact. Thus $R\bar g_*=\bar g_*$ on constructible sheaves, and
$\bar g_*$ is exact on $\Cons(\overline Z,\Qlb)$ (a short exact sequence
gives a triangle whose long exact sequence has $\mathcal H^1=0$). Thus for a Weil
sheaf $\mathcal F$ we get $Rg_!\mathcal F\simeq\bar g_*j_{0!}\mathcal F$,
a complex concentrated in degree $0$, i.e. $R^ig_!\mathcal F=0$ for
$i\neq0$. Applying the exact functor $\bar g_*j_{0!}$ termwise gives
$\mathcal H^j(Rg_!K)=\bar g_*j_{0!}\mathcal H^j(K)=g_!\mathcal H^j(K)$.

*(2).* By (1) and the composition isomorphism it suffices to treat the
two pieces. For $j_0$: a closed point of $\overline Z_0$ either lies in
$Z_0$, where $j_{0!}K$ has the same stalk with the same local
Frobenius as $K$, or lies outside, where the stalk is $0$; so each
$\mathcal H^j(j_{0!}K)=j_{0!}\mathcal H^j(K)$ receives, from a
filtration of $\mathcal H^j(K)$ with punctually pure quotients of
weights $\le w+j$ as in [def-weil-complex-weights], the filtration
by the (exact) extensions by zero, whose quotients are again punctually
pure of the same weights. Hence $j_{0!}K\in D_{\le w}(\overline Z_0)$.
For $\bar g$: the finite pushforward bound [lem-zl-finite-pushforward]
gives $R\bar g_*j_{0!}K\in D_{\le w}(Y_0)$.

*In particular.* A mixed Weil sheaf $\mathcal F$ has a finite
filtration with punctually pure quotients; if $w$ is the largest of
their weights, then $\mathcal F\in D_{\le w}(Z_0)$ by
[def-weil-complex-weights]. By (2), $Rg_!\mathcal F\in D_{\le w}(Y_0)$,
and by (1) this complex is the sheaf $g_!\mathcal F$ in degree $0$;
so $g_!\mathcal F$ is mixed of weights $\le w$.
