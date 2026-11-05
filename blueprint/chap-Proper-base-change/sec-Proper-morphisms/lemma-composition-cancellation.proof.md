+++
kind = "proof"
of = "lemma-composition-cancellation"
order = 390
uses = ["definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "definition-injective-acyclicity", "lemma-acyclic-resolutions"]
+++
Theorem [theorem-pbc-injective-acyclicity] reduces both parts to the
condition $\mathrm{IA}_\Lambda$ of injective acyclicity, and we read off
this vanishing from the Leray spectral sequence of the base-changed
composite. For (ii) the hypotheses do not apply directly to an injective
sheaf on $Y$, so we first realize it as a direct summand of $u_*J$ with
$J$ injective on $X$.

To set up the spectral sequence, fix an
arbitrary base change $Z'\to Z$. Write $g_X:X'\to X$ and $g_Y:Y'\to Y$
for the projections, and $u':X'\to Y'$, $v':Y'\to Z'$ for the induced
maps. The direct image $u'_*$ preserves injectives, because its left
adjoint $u'^*$ on sheaves of $\Lambda$-modules is exact. Hence for every
sheaf $J$ of $\Lambda$-modules on $X$ we have the
Grothendieck spectral sequence for the composite direct image
[Stacks, [0734](https://stacks.math.columbia.edu/tag/0734)]:

$$
R^pv'_*R^qu'_*g_X^*J
\ \Longrightarrow\ R^{p+q}(v'u')_*g_X^*J.
\tag{4.13}
$$

*Part (i).* Let $J$ be an injective sheaf of $\Lambda$-modules on
$X$. We show $R^m(v'u')_*g_X^*J=0$ for $m>0$, which is
$\mathrm{IA}_\Lambda(vu)$. For this it suffices that the $E_2$-terms of
(4.13) vanish except for $p=q=0$, and they do. Indeed,
$R^qu'_*g_X^*J=0$ for $q>0$ by $\mathrm{IA}_\Lambda(u)$. For $q=0$, proper
base change in degree zero
(Proposition [proposition-proper-base-change-degree-zero]) gives

$$
u'_*g_X^*J\simeq g_Y^*u_*J,
$$

and the sheaf $u_*J$ is injective, so $R^pv'_*g_Y^*u_*J=0$ for $p>0$ by
$\mathrm{IA}_\Lambda(v)$. The abutment therefore vanishes in positive
degrees.

*Part (ii), the splitting.* Let $I$ be an injective sheaf of
$\Lambda$-modules on $Y$. Choose a monomorphism of sheaves

$$
u^*I\hookrightarrow J
$$

with $J$ injective on $X$, and let $\iota:I\to u_*J$ be its adjoint.
The map $\iota$ is a monomorphism. To see this, given a geometric point
$\bar y$, choose a geometric point $\bar x$ above it, which exists because
$u$ is surjective. Then the composite

$$
I_{\bar y}\xrightarrow{\iota_{\bar y}}(u_*J)_{\bar y}
\longrightarrow J_{\bar x}
$$

is the stalk of the chosen monomorphism, under
$(u^*I)_{\bar x}=I_{\bar y}$, so it is injective.
As $I$ is an injective sheaf, there is then a map of sheaves
$s:u_*J\to I$ with $s\iota=\mathrm{id}_I$. In other words, $I$ is a direct
summand of $u_*J$.

*Part (ii), the vanishing.* We first show
$R^pv'_*g_Y^*u_*J=0$ for $p>0$. The hypotheses $\mathrm{IA}_\Lambda(u)$
and $\mathrm{IA}_\Lambda(vu)$ give

$$
R^qu'_*g_X^*J=0\quad(q>0),\qquad
R^m(v'u')_*g_X^*J=0\quad(m>0),
$$

so the spectral sequence (4.13)
collapses to its row $q=0$. This means that
$R^pv'_*u'_*g_X^*J\simeq R^p(v'u')_*g_X^*J=0$ for $p>0$. Since
$u'_*g_X^*J\simeq g_Y^*u_*J$ by proper base change in degree zero, we
obtain

$$
R^pv'_*g_Y^*u_*J
\simeq R^pv'_*u'_*g_X^*J=0\qquad(p>0).
$$

Now $g_Y^*I$ is a direct summand of $g_Y^*u_*J$, by applying $g_Y^*$ to the
splitting $s\iota=\mathrm{id}_I$, and as $R^pv'_*$ is additive,
$R^pv'_*g_Y^*I$ is a direct summand of $R^pv'_*g_Y^*u_*J$. Hence
$R^pv'_*g_Y^*I=0$ for $p>0$, which is $\mathrm{IA}_\Lambda(v)$.
