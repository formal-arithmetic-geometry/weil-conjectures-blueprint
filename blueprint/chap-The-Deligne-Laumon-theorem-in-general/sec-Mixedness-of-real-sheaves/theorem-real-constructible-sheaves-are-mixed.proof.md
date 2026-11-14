+++
kind = "proof"
of = "theorem-real-constructible-sheaves-are-mixed"
order = 1345
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "lemma-integral-models", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-proper-direct-image-constructible-complexes", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "corollary-open-direct-image-over-field", "proposition-six-operations-dctf", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "lemma-weil-sheaves-point-mixed", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "proposition-lattices-representations-normal-scheme", "theorem-purity-real-sheaves-curves", "lemma-finite-quasi-finite-direct-images", "lemma-curve-preserving-finite-cover", "lemma-mixedness-open-closed", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
We join a fixed point $x_*$ to an arbitrary point $x$ by a
curve on which the geometrically irreducible constituents stay
irreducible. On that curve each constituent is pure by
Theorem [theorem-purity-real-sheaves-curves]. Its weight can be
read off at $x_*$, so it does not depend on the curve. This handles a
lisse sheaf on a smooth affine scheme, and stratifying handles an
arbitrary constructible sheaf. Descent along constant extensions and
gluing of strata preserve mixedness
(Lemmas [lemma-mixedness-descends-constant-extension]
and [lemma-mixedness-open-closed]), so nothing about curves is used
beyond Theorem [theorem-purity-real-sheaves-curves].

*The lisse case.* Suppose that $X_0$ is smooth, geometrically
connected and affine, and that the sheaf $G$ is lisse. Since the curves
of Corollary [corollary-curve-preserving-geometric-irreducibility]
preserve geometric irreducibility, we first split $G$ into
geometrically irreducible pieces. To do so, we make the constant
extension of
Lemma [lemma-geometric-constituents-after-constant-extension] and
write $S_1,\ldots,S_r$ for the quotients of its Weil filtration. Note that the
sheaf $G$ remains real after this extension, because the powers of a
conjugation-stable multiset of eigenvalues again form a
conjugation-stable multiset.

Fix a closed point $x_*$ of $X_0$, and let $x$ be any other closed
point. By Corollary [corollary-curve-preserving-geometric-irreducibility], there is a curve
through chosen geometric points above $x_*$ and $x$ on which every
$S_j$ remains irreducible. The restriction of $G$ to this curve is
real, and Theorem [theorem-purity-real-sheaves-curves] says that the
irreducible constituents of a real sheaf on a curve are pure. Since the
restriction of $S_j$ is irreducible, it is one of them, and so
it is pure. Let $\alpha$ be an eigenvalue of $S_j$ at $x_*$, and let
$e$ be the residue degree over $\kappa(x_*)$ of the point of the curve
above $x_*$. At that point, then, the corresponding eigenvalue is $\alpha^e$
and the residue cardinality is $q_{x_*}^e$. If the restriction is pure
of weight $u$, then $|\iota(\alpha)|^e=q_{x_*}^{eu/2}$, so the weight of
the restriction of $S_j$ must be

$$
w_j=2\log_{q_{x_*}}|\iota(\alpha)|,
$$

which does not depend on the curve. In particular, all eigenvalues of $S_j$ at $x_*$
have this modulus. At $x$, the same calculation with powers
shows that $S_j$ is pure of weight $w_j$. As $x$ was arbitrary, each
$S_j$ is pure of weight $w_j$ on $X_0$. The chosen Weil filtration then
shows that $G$ is mixed after the constant extension, and by
Lemma [lemma-mixedness-descends-constant-extension], $G$ is mixed.

*The general case.* Now let $G$ be an arbitrary constructible
real sheaf. Since nilpotents do not change the étale site, we may
assume that $X_0$ is reduced. In each irreducible component, choose a
dense smooth affine open on which $G$ is lisse and which avoids the
other components. Since the complement has smaller dimension, iterating we
obtain a finite chain of closed subschemes whose differences are
disjoint unions of smooth connected affine pieces on which $G$ is
lisse. After one finite constant extension these pieces are
geometrically connected, and such an extension is allowed by
Lemma [lemma-mixedness-descends-constant-extension], and it keeps
$G$ real. The lisse case then applies
to the positive-dimensional pieces, while at a zero-dimensional piece a
Frobenius-stable full flag of each stalk has quotients of rank one,
which are pure. The restriction of $G$ to every piece is therefore mixed,
and Lemma [lemma-mixedness-open-closed], applied successively along
the chain of closed subschemes, shows that $G$ is mixed.
