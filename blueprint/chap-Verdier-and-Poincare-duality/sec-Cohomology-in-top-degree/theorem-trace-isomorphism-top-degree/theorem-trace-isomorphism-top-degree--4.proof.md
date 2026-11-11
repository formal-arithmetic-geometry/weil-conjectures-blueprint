+++
kind = "proof"
of = "theorem-trace-isomorphism-top-degree--4"
order = 866009
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "definition-ind-etale-pro-etale-weakly--3", "proposition-etale-implications--1", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "theorem-trace-isomorphism-top-degree--2"]
+++
Negative degrees vanish because $\mathcal C_A$ is a sheaf in degree zero. Each
$U_n$ is an open subgroup of the compact group $A$, so $A/U_n$ is finite. The
map $A\to\varprojlim_nA/U_n$ is continuous and injective because
$\bigcap_nU_n=0$. It has dense image, hence is surjective since $A$ is
compact, and it is a homeomorphism because the target is Hausdorff. Therefore
$C(V,A)=\varprojlim_nC(V,A/U_n)$ for every $V$, that is,
$\mathcal C_A=\varprojlim_n\mathcal C_{A/U_n}$, and $\mathcal C_{A/U_n}$ is the
constant sheaf with value $A/U_n$ by clause [proposition-pro-etale-site-separably-closed--3]. For
$A=\mathcal O_E$ and $U_n=\pi_E^n\mathcal O_E$, clause [lemma-comparison-completed-coefficients--1] then
identifies $\mathcal C_A$ with $\mathcal O_{E,S}$.

The transition maps $\mathcal C_{A/U_{n+1}}\to\mathcal C_{A/U_n}$ are
epimorphisms. Indeed, on an affine $V$ a continuous map $V\to A/U_n$ takes
finitely many values on a finite partition of $V$ into clopen subsets, and
lifting each value to $A/U_{n+1}$ gives a continuous lift. Their kernels are
the constant sheaves $\mathcal C_{U_n/U_{n+1}}$, with $U_n/U_{n+1}$ finite of
order invertible in $k'$. By clause [proposition-milnor-sequence--3],
$\mathcal C_A\simeq R\varprojlim_n\mathcal C_{A/U_n}$. By
clause [proposition-unbounded-functors-products--2], $R\Gamma(S,-)$ commutes with derived inverse limits, so
$R\Gamma(S,\mathcal C_A)\simeq R\varprojlim_nR\Gamma(S,\mathcal C_{A/U_n})$.
Countable products of abelian groups are exact, so the derived limit of this
tower of complexes of abelian groups is given by (2.1), and
the argument of clause [proposition-milnor-sequence--2] gives the Milnor sequence

$$
0\to R^1\varprojlim_nH^{i-1}(S,\mathcal C_{A/U_n})\to
H^i(S,\mathcal C_A)\to\varprojlim_nH^i(S,\mathcal C_{A/U_n})\to0.
$$

Let $i>2d$. The right term vanishes by clause [theorem-trace-isomorphism-top-degree--2]. If $i-1>2d$, so
does the left term. If $i-1=2d$, the long exact sequence for
$0\to\mathcal C_{U_n/U_{n+1}}\to\mathcal C_{A/U_{n+1}}\to\mathcal C_{A/U_n}\to0$
and the vanishing of $H^{2d+1}(S,\mathcal C_{U_n/U_{n+1}})$
(clause [theorem-trace-isomorphism-top-degree--2]) show that the transition maps
$H^{2d}(S,\mathcal C_{A/U_{n+1}})\to H^{2d}(S,\mathcal C_{A/U_n})$ are
surjective. For a tower of abelian groups with surjective transition maps,
$R^1\varprojlim$ vanishes: given $(a_n)$, choose $m_0$ arbitrarily and then
$m_{n+1}$ with $t_n(m_{n+1})=m_n-a_n$, as in the proof of
clause [proposition-milnor-sequence--3]. Hence $H^i(S,\mathcal C_A)=0$ for $i>2d$. The last
assertion is the case $S=X$, $k'=k$, $A=\mathcal O_E$.

*Source:* the proof of Theorem [theorem-trace-isomorphism-top-degree].
