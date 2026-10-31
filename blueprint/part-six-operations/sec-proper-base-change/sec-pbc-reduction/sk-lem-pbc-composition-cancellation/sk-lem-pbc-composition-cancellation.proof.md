+++
kind = "proof"
of = "sk-lem-pbc-composition-cancellation"
uses = ["sk-thm-iff", "sk-def-ia", "sk-prop-pbc-degree-zero", "sk-thm-picard-perfect"]
+++
By Theorem [sk-thm-iff] it suffices to treat the
condition $\mathrm{IA}_\Lambda$ of injective acyclicity. Fix an
arbitrary base change $Z'\to Z$. Write $g_X:X'\to X$ and $g_Y:Y'\to Y$
for the projections, and $u':X'\to Y'$, $v':Y'\to Z'$ for the induced
maps. Since the inverse image $u'^*$ of sheaves of $\Lambda$-modules
is exact, its right adjoint $u'_*$ preserves injectives. Therefore, for
every sheaf $J$ of $\Lambda$-modules on $X$, we have the
Grothendieck spectral sequence for the composite direct image
[Stacks, Tag 0734](https://stacks.math.columbia.edu/tag/0734):

$$
R^pv'_*R^qu'_*g_X^*J
\ \Longrightarrow\ R^{p+q}(v'u')_*g_X^*J.
\tag{4.12}
$$

For (i), let $J$ be an injective sheaf of $\Lambda$-modules on $X$.
By $\mathrm{IA}_\Lambda(u)$ we have
$R^qu'_*g_X^*J=0$ for $q>0$. By proper base change in degree zero
(Proposition [sk-prop-pbc-degree-zero]) we have

$$
u'_*g_X^*J\simeq g_Y^*u_*J.
$$

The sheaf $u_*J$ is injective, so $R^pv'_*g_Y^*u_*J=0$ for $p>0$ by
$\mathrm{IA}_\Lambda(v)$. Thus the $E_2$-terms of
(4.12) vanish except for $p=q=0$, and the abutment
gives $R^m(v'u')_*g_X^*J=0$ for $m>0$. This proves
$\mathrm{IA}_\Lambda(vu)$, and hence (i).

For (ii), let $I$ be an injective sheaf of $\Lambda$-modules on $Y$.
Choose a monomorphism of sheaves

$$
u^*I\hookrightarrow J
$$

with $J$ injective on $X$, and let $\iota:I\to u_*J$ be its adjoint.
We claim that $\iota$ is a monomorphism. To see this, for a geometric point
$\bar y$ choose a geometric point $\bar x$ above it, which exists by
surjectivity of $u$. The composite

$$
I_{\bar y}\xrightarrow{\iota_{\bar y}}(u_*J)_{\bar y}
\longrightarrow J_{\bar x}
$$

is the stalk of the chosen monomorphism, under
$(u^*I)_{\bar x}=I_{\bar y}$, so it is injective.
Since $I$ is an injective sheaf, there is a map of sheaves $s:u_*J\to I$ with
$s\iota=\mathrm{id}_I$, that is, $I$ is a direct summand of $u_*J$.

By $\mathrm{IA}_\Lambda(u)$ and $\mathrm{IA}_\Lambda(vu)$ we have

$$
R^qu'_*g_X^*J=0\quad(q>0),\qquad
R^m(v'u')_*g_X^*J=0\quad(m>0).
$$

The spectral sequence (4.12) therefore
collapses to its row $q=0$, so that
$R^pv'_*u'_*g_X^*J\simeq R^p(v'u')_*g_X^*J=0$ for $p>0$. Since
$u'_*g_X^*J\simeq g_Y^*u_*J$ by proper base change in degree zero, we get

$$
R^pv'_*g_Y^*u_*J
\simeq R^pv'_*u'_*g_X^*J=0\qquad(p>0).
$$

Applying $g_Y^*$ to the splitting $s\iota=\mathrm{id}_I$, we see that
$g_Y^*I$ is a direct summand of $g_Y^*u_*J$. Since $R^pv'_*$ is additive,
$R^pv'_*g_Y^*I$ is a direct summand of $R^pv'_*g_Y^*u_*J$, and hence
$R^pv'_*g_Y^*I=0$ for $p>0$. This proves
$\mathrm{IA}_\Lambda(v)$, and (ii) follows.
