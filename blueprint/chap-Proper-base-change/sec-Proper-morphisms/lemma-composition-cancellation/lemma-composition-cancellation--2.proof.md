+++
kind = "proof"
of = "lemma-composition-cancellation--2"
order = 389005
+++
Use Theorem [theorem-pbc-injective-acyclicity].

*Part (ii), the splitting.* Let $I$ be an injective sheaf of
$\Lambda$-modules on $Y$. Choose a monomorphism of sheaves

$$
u^*I\hookrightarrow J
$$

with $J$ injective on $X$, and let $\iota:I\to u_*J$ be its adjoint.
The map $\iota$ is a monomorphism. To see this, given a geometric point
$\bar y$, choose a geometric point $\bar x$ above it, which exists because
$u$ is surjective. The composite

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
splitting $s\iota=\mathrm{id}_I$. As $R^pv'_*$ is additive,
$R^pv'_*g_Y^*I$ is a direct summand of $R^pv'_*g_Y^*u_*J$. Hence
$R^pv'_*g_Y^*I=0$ for $p>0$, which is $\mathrm{IA}_\Lambda(v)$.

*Source:* the proof of Lemma [lemma-composition-cancellation].
