+++
kind = "proof"
of = "lemma-uniform-bounds-pro-etale-affines"
order = 163
uses = ["proposition-etale-implications", "proposition-topos-functoriality", "proposition-pro-etale-affines-form-basis", "definition-classical-pro-etale-sheaves", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "lemma-cohomological-dimension-base-field", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
We write both cohomologies as colimits of étale cohomology of
schemes of finite type over $k$ and bound these uniformly. Write
$U=\varprojlim_iU_i$ and $V=\varprojlim_iV_i$ with $U_i$ affine
étale over $X$ and $V_i$ affine étale over $Y$, and write
$F=\nu_X^*F_{\acute{e}t}$ (Theorem [theorem-classical-sheaves-essential-image]).
By Theorem [theorem-bounded-below-cohomology-comparison], applied
to the schemes $U$ and $X\times_YV$, the cohomology of $F$ on them is the
étale cohomology of $F_{\acute{e}t}$. As $U=\varprojlim_iU_i$ and
$X\times_YV=\varprojlim_iX\times_YV_i$ are limits of qcqs schemes with
affine transition maps, [Stacks, [03Q6](https://stacks.math.columbia.edu/tag/03Q6)] identifies this with the colimit of
the étale cohomology on the $U_i$, respectively on the $X\times_YV_i$.
Each $U_i$ is affine of finite
type over $k$ with $\dim(U_i)\leq\dim(X)$, so by [Stacks, [0F0V](https://stacks.math.columbia.edu/tag/0F0V)] we have
$\operatorname{cd}_\ell(U_i)\leq d$ for sheaves of $A$-modules. To bound
cohomology on $X\times_YV_i$ independently of $i$, we choose a finite
affine open cover of $X$, with $r$ members. Since $X$ and $Y$ are
separated over $k$, its intersections and their pullbacks to the affine
$V_i$ are affine; each pullback is étale over the corresponding
intersection and has dimension at most $\dim(X)$. The alternating
Čech complex has length $r-1$, so the Čech spectral sequence
gives the bound $c=d+r-1$. The last assertion is [Stacks, [0F10](https://stacks.math.columbia.edu/tag/0F10)], which
applies because $g$ is of finite type over a field with
$\operatorname{cd}_\ell(k)<\infty$
(Lemma [lemma-cohomological-dimension-base-field]).
