+++
kind = "proof"
of = "sk-thm-curveestimate"
+++
Pulling back the Kummer sequence of $C_{\acute{e}t}$ by $\nu_C^*$, we get
the exact sequence of sheaves on $C_{\mathrm{pro}\acute{e}t}$

$$
0\longrightarrow\mu_n\longrightarrow\nu_C^*\mathbf G_m
\xrightarrow{(\cdot)^n}\nu_C^*\mathbf G_m
\longrightarrow0.
$$

Surjectivity of the $n$th power map is a local question, and for a unit
$a$ the equation $T^n=a$ defines an étale cover, since its derivative
$nT^{n-1}$ is a unit. The global
units on the proper connected curve form the group $k^\times$, which is
$n$-divisible. Therefore Lemma [sk-thm-br] and the long exact
sequence show that

$$
H^1(C,\mu_n)=\operatorname{Pic}(C)[n],\qquad
H^2(C,\mu_n)=\operatorname{Pic}(C)/n,
$$

with all higher groups zero.

Corollary [sk-cor-picard-degree] gives the exact sequence

$$
0\longrightarrow J(C)(k)\longrightarrow\operatorname{Pic}(C)
\xrightarrow{\deg}\mathbf Z\longrightarrow0.
$$

Multiplication by $n$ on $J(C)(k)$ is surjective, with kernel
$J(C)[n](k)$, and $J(C)[n]$ is finite étale of rank $n^{2g}$
(Corollary [sk-cor-jacobian-torsion]). Applying the snake lemma to
multiplication by $n$ on this sequence, and using that $\mathbf Z$ is
torsion free, we obtain $\operatorname{Pic}(C)[n]=J(C)[n](k)$ and
$\operatorname{Pic}(C)/n=\mathbf Z/n$ via the degree. In particular
$H^1(C,\mu_n)$ is noncanonically isomorphic to $(\mathbf Z/n)^{2g}$
[Stacks, Tag 03RQ](https://stacks.math.columbia.edu/tag/03RQ).

Under an algebraically closed extension $k'/k$, the schemes $J(C)$ and $J(C)[n]$
base change to the corresponding objects for $C_{k'}$, and the map
$J(C)[n](k)\to J(C)[n](k')$ is bijective by
Corollary [sk-cor-jacobian-torsion]. The same argument applies to the
finite étale scheme $\mu_n$, and pullback of line bundles preserves
the degree. Hence the pullback maps on cohomology are isomorphisms.
