+++
id = "theorem-trace-formula-euler-product"
kind = "theorem"
title = "The trace formula as an Euler product"
order = 1037
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "lemma-logarithm-determinant", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Let $X_0$ be separated and of finite type over $\mathbf F_q$, let
$\Lambda\in\{\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}$, and let $K\in\Dbc(X,\Lambda)$ carry a Weil
structure, with stalk Frobenius maps $\operatorname{Frob}_{y,m}$ as in
Theorem [theorem-grothendieck-lefschetz-trace-formula]. For each closed
point $x\in|X_0|$, let $\deg(x)=[\kappa(x):\mathbf F_q]$ be its degree,
choose one of the $\deg(x)$ points $y\in X_0(\mathbf F_{q^{\deg(x)}})$ lying
over $x$, write $\bar x=\bar y$ for the corresponding geometric point,
and let $\operatorname{Frob}_x=\operatorname{Frob}_{y,\deg(x)}$ be its
action on $K_{\bar x}$. Another choice of $y$ replaces
$\operatorname{Frob}_x$ by a conjugate. Define

$$
L(X_0,K,T)
:=\prod_{x\in|X_0|}
\det\bigl(1-T^{\deg(x)}\operatorname{Frob}_x\mid K_{\bar x}\bigr)^{-1}.
\tag{12.6}
$$

For every $n$, only finitely many factors differ from $1$ modulo $T^n$,
so the product converges $T$-adically in $1+T\Lambda[[T]]$, and

$$
L(X_0,K,T)
=\prod_i\det\bigl(1-T\operatorname{Frob}_{X,K}\mid H_c^i(X_{\mathrm{pro}\acute{e}t},K)\bigr)^{(-1)^{i+1}}.
\tag{12.7}
$$

In particular, $L(X_0,K,T)$ is the expansion at zero of a rational
function in $\Lambda(T)$ with value $1$ at zero. If $X_0$ is proper, we
may replace $H_c^i$ by $H^i$.
