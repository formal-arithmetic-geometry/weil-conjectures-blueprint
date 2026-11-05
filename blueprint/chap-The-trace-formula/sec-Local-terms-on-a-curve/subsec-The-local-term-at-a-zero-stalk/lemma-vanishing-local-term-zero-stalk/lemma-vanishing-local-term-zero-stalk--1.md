+++
id = "lemma-vanishing-local-term-zero-stalk--1"
kind = "lemma"
title = "Vanishing of the supported restriction"
order = 990001
aliases = ["bp-r302-1"]
lean = ["AlgebraicGeometry.Etale.CurveLocalModel.sectionsWithSupportRestriction_eq_zero", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.upperStar_map_supportedRestriction_frobeniusGraph_eq_zero"]
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "definition-ind-etale-pro-etale-weakly--3", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--6", "lemma-stability--7", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "proposition-topos-functoriality--2", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "definition-w-local-w-strictly-local--4", "proposition-w-local-components--1", "example-locally-constant-functions-w-local--1", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "corollary-evaluation-weakly-contractible-objects--1", "proposition-exact-products--2", "proposition-milnor-sequence--2", "proposition-comparison-morphism-inverse-image--2", "theorem-classical-sheaves-essential-image--1", "lemma-acyclicity-pulled-back-injectives--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "theorem-comparison-direct-images--1", "proposition-comparison-immersions--1", "proposition-locally-constant-sheaves-finite-presentation--3", "proposition-pro-etale-site-separably-closed--3", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-inverse-image-coefficient-sheaves--4", "definition-derived-adic-completeness--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--2", "definition-constructible-sheaves--4", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "definition-lisse-sheaves--1", "proposition-integral-constructibility-criterion--1", "lemma-constructible-sheaves--8", "lemma-lattices-after-finite-stratification--1", "proposition-inverting-ell--2", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "lemma-identity-pasting--2", "proposition-proper-base-change-degree-zero--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "definition-torsion-pbc-property--1", "definition-injective-acyclicity--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "proposition-proper-base-change-projective-line--1", "lemma-finite-morphisms--1", "lemma-finite-cover-projective-space--1", "proposition-proper-base-change-etale-site--1", "corollary-cohomology-geometric-fibres--2", "proposition-proper-base-change-complete-integral--1", "proposition-proper-direct-image-constructible-complexes--2", "proposition-proper-direct-image-constructible-complexes--3", "proposition-proper-direct-image-constructible-complexes--8", "proposition-comparison-etale-derived-category--3", "proposition-comparison-etale-derived-category--5", "proposition-comparison-etale-derived-category--6", "lemma-inverse-image-tensor-product--1", "lemma-inverse-image-tensor-product--3", "lemma-inverse-image-tensor-product--4", "lemma-inverse-image-tensor-product--6", "proposition-forgetting-supports-composition--3", "proposition-composition-open-restriction-compactifications-f--1", "proposition-composition-open-restriction-compactifications-f--4", "proposition-exceptional-inverse-image-smooth-morphism--5", "corollary-open-direct-image-over-field--1", "definition-change-of-coefficients-maps--6", "lemma-change-coefficients-exceptional-inverse-image--4", "proposition-six-operations-change-coefficients--1", "proposition-six-operations-change-coefficients--2", "proposition-six-operations-change-coefficients--3", "proposition-six-operations-change-coefficients--9", "proposition-six-operations-change-coefficients--23", "proposition-dctf-x-qbar-2-colimit--2", "proposition-dctf-x-qbar-2-colimit--3", "proposition-sp-unique-adjoint--1", "definition-sp-scalar-extension--2", "definition-verdier-dual-evaluation--2", "definition-correspondence--1", "definition-correspondence--2", "definition-frobenius-correspondences-their-operators--1", "definition-frobenius-correspondences-their-operators--5", "lemma-kunneth-formula-compact-supports--2", "definition-compactification-refinement--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-uniqueness-maps-dense-open--1", "definition-admissible-blow-up--1", "theorem-extension-partial-section--1", "theorem-elimination-indeterminacy--1", "lemma-extending-graph-from-compactification--1", "lemma-separation-closures--1", "lemma-extending-isomorphism-over-closure-closed--1", "lemma-gluing-after-admissible-blow-ups--1", "lemma-affine-covers-dense-intersection--1", "theorem-chow-s-lemma-projective-form--2", "theorem-riemann-roch-coherent-serre-duality--6", "lemma-coherent-base-change-invertible-sheaves--1", "corollary-degree-jacobian--1", "corollary-torsion-jacobian-field-extension--5", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-cohomology-multiplicative-group--5", "lemma-cohomology-multiplicative-group--6", "proposition-p-torsion-smooth-proper-curve--1", "lemma-finite-morphisms-cohomology--2"]
+++
Let $k$ be algebraically closed, let $X/k$ be a separated, quasi-compact
smooth curve, and let $h:X\to X$ be a $k$-endomorphism fixing $y\in X(k)$
such that $h^\#\mathfrak m_y\subseteq\mathfrak m_y^2$. Let $\ell$ be a
prime invertible in $k$, let $A$ be a finite commutative $\ell$-primary
ring, and let $L,K\in D^b_{\mathrm{ctf}}(X,A)$ with $K_{\bar y}=0$.
On the strict localization $T$ of $X\times_k X$ at $(y,y)$, let
$\Gamma$ and $\Delta$ be the inverse images of the transposed graph
$(h,\operatorname{id}_X)$ and the diagonal, and put
$P=(L\boxtimes K)|_T$. Then the supported restriction

$$
\rho:R\Gamma_\Gamma(T,P)\longrightarrow R\Gamma_y(\Delta,\delta^*P)
$$

is zero in $D(A)$. In particular, this applies to $h=\Phi_X^m$, $m\geq1$,
and $L=\mathbb D_XK$ in Lemma [lemma-local-term-restriction-map].

There is also a $\Qbarl$-coefficient form. Let $k$ be an algebraically
closed extension of a finite field $k_0$ of characteristic different
from $\ell$, and let $X=X_0\times_{k_0}k$ be a separated smooth curve,
with $X_0$ of finite type over $k_0$. Let $m\geq1$ and
$K\in D^b_{\mathrm{ctf}}(X,\Qbarl)$. Use the graph convention $c=(\operatorname{id}_X,\Phi_X^m)$, put
$P'=K\boxtimes\mathbb D_XK$, and write $F=\Fix(c)$, with maps
$\iota:F\to X$ to the source of the graph and $d:F\to X$ to the
diagonal. If $z:\operatorname{Spec}k\to F$ has image $y\in X(k)$ and
$K_{\bar y}=0$, then the pullback along $z$ of

$$
\rho_{P'}:L\iota^*Rc^!P'\longrightarrow Rd^!L\delta^*P'
$$

is zero. Interchanging the two factors of $X\times_k X$ identifies
this convention with the transposed graph and
$\mathbb D_XK\boxtimes K$ of Lemma [lemma-local-term-restriction-map].
