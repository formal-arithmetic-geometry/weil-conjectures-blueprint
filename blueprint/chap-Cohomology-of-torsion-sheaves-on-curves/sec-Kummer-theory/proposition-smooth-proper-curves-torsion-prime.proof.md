+++
kind = "proof"
of = "proposition-smooth-proper-curves-torsion-prime"
order = 1575
uses = ["definition-constructible-sheaves", "definition-underived-base-change-map", "lemma-finite-morphisms", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Pulling back the Kummer sequence of $C_{\acute{e}t}$ by $\nu_C^*$, we get
the exact sequence of sheaves on $C_{\mathrm{pro}\acute{e}t}$

$$
0\longrightarrow\mu_n\longrightarrow\nu_C^*\mathbf G_m
\xrightarrow{(\cdot)^n}\nu_C^*\mathbf G_m
\longrightarrow0.
$$

Here surjectivity of the $n$th power map is a local question. For a
unit $a$ the equation $T^n=a$ defines an étale cover, since its
derivative $nT^{n-1}$ is a unit. Moreover, the global units on the proper connected curve form the group $k^\times$, which is
$n$-divisible because $k$ is algebraically closed. Hence the long exact
sequence starts with $H^0(C,\mu_n)=\mu_n(k)$. Since the map
$H^0(C,\mathbf G_m)\to H^0(C,\mathbf G_m)$ is onto, $H^1(C,\mu_n)$
injects into $H^1(C,\mathbf G_m)$. Using
Lemma [lemma-cohomology-multiplicative-group], we read off from the
long exact sequence that

$$
H^1(C,\mu_n)=\operatorname{Pic}(C)[n],\qquad
H^2(C,\mu_n)=\operatorname{Pic}(C)/n,
$$

with all higher groups zero.

Corollary [corollary-degree-jacobian] gives the exact sequence

$$
0\longrightarrow J(C)(k)\longrightarrow\operatorname{Pic}(C)
\xrightarrow{\deg}\mathbf Z\longrightarrow0.
$$

Multiplication by $n$ on $J(C)(k)$ is surjective, with kernel
$J(C)[n](k)$, and $J(C)[n]$ is finite étale of rank $n^{2g}$
(Corollary [corollary-torsion-jacobian-field-extension]).  Applying the snake lemma to
multiplication by $n$ on this sequence, and using that $\mathbf Z$ is
torsion free, we obtain $\operatorname{Pic}(C)[n]=J(C)[n](k)$ and
$\operatorname{Pic}(C)/n=\mathbf Z/n$ via the degree. In particular,
$H^1(C,\mu_n)$ is noncanonically isomorphic to $(\mathbf Z/n)^{2g}$
[Stacks, [03RQ](https://stacks.math.columbia.edu/tag/03RQ)].

Under an algebraically closed extension $k'/k$, the schemes $J(C)$ and $J(C)[n]$
base change to the corresponding objects for $C_{k'}$. The map
$J(C)[n](k)\to J(C)[n](k')$ is bijective by
Corollary [corollary-torsion-jacobian-field-extension]. The same argument
applies to the finite étale scheme $\mu_n$. Finally, pullback of line
bundles preserves the degree. Hence the pullback maps on cohomology are
isomorphisms.
