+++
id = "lemma-fourier-transform-boundary-sequence--1"
kind = "lemma"
title = "The Fourier correction sequence"
order = 1276001
aliases = ["bp-r393-1"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.fourierTransformExtensionByZeroIso", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.nonempty_fourierCorrection"]
uses = ["proposition-pro-etale-affines-form-basis", "lemma-descent-finite-coefficient-field", "definition-derived-base-change-map", "lemma-finite-cover-projective-space", "proposition-fourier-transform-middle-extension", "theorem-picard-scheme-jacobian-over-separably", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "definition-ind-etale-pro-etale-weakly--3", "proposition-etale-implications--1", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "proposition-topos-functoriality--2", "definition-w-local-w-strictly-local--4", "example-locally-constant-functions-w-local--1", "lemma-extremally-disconnected-covers--3", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "theorem-pro-etale-refinements-weakly-etale--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "lemma-acyclicity-pulled-back-injectives--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "lemma-comparison-direct-images-compatibilities--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "proposition-pro-etale-site-separably-closed--3", "lemma-comparison-completed-coefficients--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-derived-adic-completeness--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--2", "definition-constructible-sheaves--4", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "proposition-integral-constructibility-criterion--1", "lemma-constructible-sheaves--8", "lemma-descent-finite-coefficient-field--3", "lemma-descent-finite-coefficient-field--2", "lemma-lattices-after-finite-stratification--1", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "lemma-finite-morphisms--1", "lemma-finite-cover-projective-space--1", "theorem-proper-base-change-classical-pro--1", "corollary-cohomology-geometric-fibres--2", "proposition-proper-base-change-complete-integral--1", "proposition-comparison-etale-derived-category--5", "corollary-open-direct-image-over-field--1", "definition-change-of-coefficients-maps--4", "proposition-sp-unique-adjoint--1", "definition-middle-extension--1", "lemma-artin-schreier-character-sheaf--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "lemma-uniqueness-maps-dense-open--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2", "theorem-riemann-roch-coherent-serre-duality--6", "lemma-coherent-base-change-invertible-sheaves--1", "corollary-torsion-jacobian-field-extension--5", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-cohomology-multiplicative-group--3", "lemma-cohomology-multiplicative-group--5", "lemma-cohomology-multiplicative-group--6", "proposition-p-torsion-smooth-proper-curve--1", "lemma-finite-morphisms-cohomology--2"]
+++
Let $\psi$ be nontrivial, let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$
be a dense open, put $U=U_0\otimes_{k_0}\bar k_0$, and let $M$ be a nonzero irreducible lisse Weil
$\overline{\mathbf Q}_\ell$-sheaf on $U_0$ with no geometric irreducible
constituent of the form $\mathcal L_{\psi(ax)}|_{U}$ for $a\in\bar k_0$.
Fix a dense open $j':U'_0\hookrightarrow\mathbf A^{1\vee}_{k_0}$,
a lisse Weil sheaf $M'$ on $U'_0$, and an isomorphism
$\operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1]$, as in
[proposition-fourier-transform-middle-extension]. No assumption on the
weights of $M$ is needed here; in [lemma-fourier-transform-boundary-sequence--2], $M$ is moreover pure of weight $w$.

Put $B=j_*M/j_!M$. There are Weil sheaves $G$ and $B'$ on the dual line
and isomorphisms
$\operatorname{FT}_\psi(j_!M)\simeq G$ and
$\operatorname{FT}_\psi(B)\simeq B'[1]$, together with a short exact sequence

$$
0\longrightarrow B'\longrightarrow G
\overset{g}{\longrightarrow} j'_*M'\longrightarrow0.
$$

Under the corresponding isomorphisms
$\operatorname{FT}_\psi(j_!M[1])\simeq G[1]$ and
$\operatorname{FT}_\psi(j_*M[1])\simeq(j'_*M')[1]$, the map $g[1]$
is the Fourier transform of the canonical map $j_!M[1]\to j_*M[1]$.
