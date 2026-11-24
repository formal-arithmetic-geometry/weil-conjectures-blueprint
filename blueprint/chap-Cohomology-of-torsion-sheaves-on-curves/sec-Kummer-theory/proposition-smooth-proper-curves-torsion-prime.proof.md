+++
kind = "proof"
of = "proposition-smooth-proper-curves-torsion-prime"
order = 1580
uses = ["lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve"]
+++
Pulling back the Kummer sequence of $C_{\acute{e}t}$ by [$\nu_C^*$](@proposition-comparison-morphism-inverse-image), we get
the exact sequence of sheaves on [$C_{\mathrm{pro}\acute{e}t}$](@definition-small-pro-etale-site)

$$
0\longrightarrow\mu_n\longrightarrow\href{@proposition-comparison-morphism-inverse-image}{\nu_C^*\mathbf G_m}
\xrightarrow{(\cdot)^n}\href{@proposition-comparison-morphism-inverse-image}{\nu_C^*\mathbf G_m}
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
0\longrightarrow \href{@theorem-picard-scheme-jacobian-over-separably}{J(C)(k)}\longrightarrow\operatorname{Pic}(C)
\xrightarrow{\deg}\mathbf Z\longrightarrow0.
$$

Multiplication by $n$ on [$J(C)(k)$](@theorem-picard-scheme-jacobian-over-separably) is surjective, with kernel
[$J(C)[n](k)$](@theorem-picard-scheme-jacobian-over-separably), and [$J(C)[n]$](@theorem-picard-scheme-jacobian-over-separably) is finite étale of rank $n^{2g}$
(Corollary [corollary-torsion-jacobian-field-extension]).  Applying the snake lemma to
multiplication by $n$ on this sequence, and using that $\mathbf Z$ is
torsion free, we obtain $\operatorname{Pic}(C)[n]=\href{@theorem-picard-scheme-jacobian-over-separably}{J(C)}\href{@definition-abelian-variety}{[n]}(k)$ and
$\operatorname{Pic}(C)/n=\mathbf Z/n$ via the degree. In particular,
$H^1(C,\mu_n)$ is noncanonically isomorphic to $(\mathbf Z/n)^{2g}$
[Stacks, [03RQ](https://stacks.math.columbia.edu/tag/03RQ)].

Under an algebraically closed extension $k'/k$, the schemes [$J(C)$](@theorem-picard-scheme-jacobian-over-separably) and [$J(C)[n]$](@theorem-picard-scheme-jacobian-over-separably)
base change to the corresponding objects for $C_{k'}$. The map
$\href{@theorem-picard-scheme-jacobian-over-separably}{J(C)}\href{@definition-abelian-variety}{[n]}(k)\to \href{@theorem-picard-scheme-jacobian-over-separably}{J(C)}\href{@definition-abelian-variety}{[n]}(k')$ is bijective by
Corollary [corollary-torsion-jacobian-field-extension]. The same argument
applies to the finite étale scheme $\mu_n$. Finally, pullback of line
bundles preserves the degree. Hence the pullback maps on cohomology are
isomorphisms.
