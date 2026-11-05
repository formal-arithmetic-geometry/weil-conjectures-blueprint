+++
kind = "proof"
of = "lemma-integral-linear-character--2"
order = 1225005
uses = ["lemma-artin-schreier-character-sheaf", "proposition-composition-base-change-rf-shriek", "definition-projection-formula-map", "proposition-projection-formula-rational-coefficients", "definition-trace-function"]
+++
Put $K=\mathcal L_\psi((\pi^*a)s)\otimes\pi^*P$ and
$M=R\pi_!K$. On $Y\times_XY$, write $q_1,q_2$ for the projections
and $s_1,s_2$ for the two fibre coordinates. The shear

$$
\tau:(s_1,s_2)\longmapsto(s_1+a^{-1}s_2,s_2)
$$

is an automorphism over the second factor. By the multiplicativity
of the Artin–Schreier sheaf in [lemma-artin-schreier-character-sheaf],

$$
\tau^*q_1^*K\simeq q_2^*\mathcal L_\psi(s)\otimes q_1^*K.
$$

Compact-support base change for $\pi$ and for $\tau$, followed by the
projection formula for the lisse sheaf $\mathcal L_\psi(s)$, gives

$$
\pi^*M\simeq\mathcal L_\psi(s)\otimes\pi^*M.
$$

This is the intermediate isomorphism
`AlgebraicGeometry.WeilComplex.nonempty_iso_upperStar_derivedLowerShriek_tensorLisse_artinSchreierOf`.
Pullback and tensoring with this lisse sheaf commute with cohomology
sheaves. For every $j$, every $n\geq1$, every
$x\in X(\Fqn)$, and every $c\in\Fqn$, evaluate the resulting
isomorphism at the point $(x,c)$ of the trivial line bundle. The
Artin–Schreier trace formula gives

$$
t_{\mathcal H^j(M),n}(x)
=\psi\bigl(\operatorname{Tr}_{\Fqn/k_0}(c)\bigr)
 t_{\mathcal H^j(M),n}(x).
$$

Choose $d\in k_0$ with $\psi(d)\ne1$. Surjectivity of the field trace
gives a $c$ with trace $d$, so every trace function of every
$\mathcal H^j(M)$ vanishes. The criterion
`AlgebraicGeometry.WeilSheaf.isZero_of_traceFunction_eq_zero` now gives
$\mathcal H^j(M)=0$: at each closed point, the traces of all positive
powers of its invertible Frobenius vanish, which forces the stalk to
have dimension zero in characteristic zero. Thus all cohomology
sheaves of $M$ vanish and $M=0$.
