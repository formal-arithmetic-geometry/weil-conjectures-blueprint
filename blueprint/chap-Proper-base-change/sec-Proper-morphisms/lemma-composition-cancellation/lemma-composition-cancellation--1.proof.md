+++
kind = "proof"
of = "lemma-composition-cancellation--1"
order = 389003
+++
Use Theorem [theorem-pbc-injective-acyclicity] to pass between the base-change and injective-acyclicity conditions.

*Part (i).* Let $J$ be an injective sheaf of $\Lambda$-modules on
$X$. We show $R^m(v'u')_*g_X^*J=0$ for $m>0$, which is
$\mathrm{IA}_\Lambda(vu)$. The $E_2$-terms of
(4.13) vanish except for $p=q=0$. Indeed,
$R^qu'_*g_X^*J=0$ for $q>0$ by $\mathrm{IA}_\Lambda(u)$. For $q=0$, proper
base change in degree zero
(Proposition [proposition-proper-base-change-degree-zero]) gives

$$
u'_*g_X^*J\simeq g_Y^*u_*J,
$$

and the sheaf $u_*J$ is injective, so $R^pv'_*g_Y^*u_*J=0$ for $p>0$ by
$\mathrm{IA}_\Lambda(v)$. The abutment therefore vanishes in positive
degrees.

*Source:* the proof of Lemma [lemma-composition-cancellation].
