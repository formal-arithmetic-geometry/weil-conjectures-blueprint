+++
id = "prose-E-03"
kind = "hidden"
title = "Specialization to the normal cone (2)"
order = 1624
+++
For a morphism $g:\mathcal Y'\to\mathcal Y$ of separated
$S$-schemes of finite type, there is a base change map for pullback

$$
g_s^*R\Psi_{\mathcal Y}
\longrightarrow R\Psi_{\mathcal Y'}g_\eta^*,
$$

which is invertible for smooth $g$. For proper $g$
there is a base change map for proper direct image

$$
Rg_{s*}R\Psi_{\mathcal Y'}
\xrightarrow{\sim}R\Psi_{\mathcal Y}Rg_{\eta*}.
$$

These base change maps commute with composition and with the specialization
map defined below. Their invertibility follows from two base change
theorems for torsion coefficients. First, proper base change [Stacks, [095T](https://stacks.math.columbia.edu/tag/095T)] says that restriction to a fibre commutes with proper direct image.
Second, smooth base change [Stacks, [0F09](https://stacks.math.columbia.edu/tag/0F09)] (for sheaves [Stacks, [0EYU](https://stacks.math.columbia.edu/tag/0EYU)]) says that
pullback along a smooth map commutes with direct image along a qcqs
morphism, when the coefficients are torsion of order invertible on the
base. Suppose first that $g$ is proper. The two direct images on the
generic fibres agree because direct image is compatible with composition,
and $\bar i^*$ commutes with the proper direct image by proper base
change. Suppose next that $g$ is smooth. Since $R\bar j_*$ is direct
image along a qcqs morphism, we may apply smooth base change to it and
then restrict to the special fibre. Smooth base change applies because
the coefficients are annihilated by a power of $\ell$, which is
invertible on $S$. The same base change maps appear in
[sga7-2], Exposé XIII, (2.1.7.1)–(2.1.7.3).

We also use two calculations for a finite $A$-module $M$. The first is
$R\Psi_S(M_{\eta})=M$. It holds because the integral closure
$\bar S$ of $S$ in the separable closure is strictly henselian, so the
stalk of $R\bar j_*M$ at its closed point is
$R\Gamma(\bar\eta,M)=M$. The second is the usual calculation for the
affine line with coefficients prime to the characteristic:
$H^r(\mathbf A^1_k,M)=0$ for $r>0$ and $H^0(\mathbf A^1_k,M)=M$. It
follows from [Stacks, [03RR](https://stacks.math.columbia.edu/tag/03RR)] applied to the compactification
$\mathbf A^1\subset\mathbf P^1$, which has genus zero and one point at
infinity. To apply that result, note that every finite $M$ is a finite
direct sum of cyclic modules, and over the algebraically closed field $k$
the cyclic constant coefficients are isomorphic to the corresponding
roots of unity.
By truncation the two calculations extend to a bounded complex
$M^\bullet$ of finite $A$-modules, viewed as a constant complex:

$$
R\Psi_S(M^\bullet_\eta)\simeq M^\bullet,
\qquad R\Gamma(\mathbf A^1_k,M^\bullet_{\mathbf A^1_k})\simeq M^\bullet.
$$

Finally, all complexes stay bounded and constructible. By the finiteness
theorem for nearby cycles with torsion coefficients ([sga4-5],
*Théorèmes de finitude*, §3; [illusie94, §4.1,
pp. 44–45]), $R\Psi_{\mathcal Y}$ takes bounded
constructible complexes of finite Tor dimension to complexes of the same
kind. Finite Tor dimension is what we need when we take traces.
The same holds for an arbitrary bounded constructible complex, without
the Tor condition. To see this, we may forget the $A$-action, since the
underlying torsion sheaves of $A$-linear nearby cycles are the usual
nearby cycles. Bounded constructible complexes are stable under
extensions and truncation, so the filtration by powers of $\ell$ reduces
us to constructible $\mathbf F_\ell$-sheaves. These have finite Tor
dimension over $\mathbf F_\ell$, and the finiteness theorem applies.

For a separated $k$-scheme $Y$ of finite type, the constant family
$Y\times S$ has special fibre $Y$. For $L$ on $Y$, let $L_\eta$ be its
pullback to the generic fibre.  Restricting the adjunction unit of
$\bar j$ on the pullback of $L$ to the special fibre, we get the
specialization map $\sigma_Y(L)$ below.
