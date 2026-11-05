+++
kind = "proof"
of = "corollary-trace-functions-direct-image-compact"
order = 1026
uses = ["proposition-w-local-components", "theorem-enough-affine-weakly-contractible-objects", "proposition-milnor-sequence", "proposition-inverting-ell", "lemma-identity-pasting", "definition-pro-etale-base-change-map", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-pbc-property", "definition-injective-acyclicity", "proposition-proper-base-change-etale-site", "lemma-inverse-image-tensor-product", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "definition-frobenius-operator", "definition-categorical-trace", "proposition-properties-trace", "definition-correspondence", "definition-trace-class-local-terms", "definition-action-correspondence", "theorem-proper-pushforward-lefschetz-verdier", "definition-frobenius-correspondences-their-operators", "lemma-scheme-frobenius-geometric-frobenius", "lemma-frobenius-fixed-scheme", "proposition-frobenius-local-term-curve"]
+++
The left side is a trace on a stalk of $Rf_!K$. By base change that
stalk is the compactly supported cohomology of a fibre. Hence the corollary
is the trace formula for the fibre, once we check that the Frobenius
operators correspond.

Fix $y$ and let $X_{0,y}$ be the fibre of $f_0$ over $y$. It is a separated
scheme of finite type over $\mathbf F_{q^m}$, and its rational points are
the $x\in X_0(\mathbf F_{q^m})$ with $f_0(x)=y$. Restrict $K$ to its
geometric fibre $X_{\bar y}$ and give the restriction the Weil
structure over $\mathbf F_{q^m}$ obtained from the $m$-th iterate of
$\phi$. By base change for compact supports, $(Rf_!K)_{\bar y}$ is
$R\Gamma_c(X_{\bar y},K|_{X_{\bar y}})$, and
$\operatorname{Frob}_{y,m}$ is the geometric Frobenius operator of
this Weil complex. For finite $A$ this is part (4) of
Lemma [lemma-comparison-via-relative-frobenius], applied to the Frobenius
correspondence $\phi\kappa_1$ and translated by
Lemma [lemma-scheme-frobenius-geometric-frobenius]. By the comparisons of
Proposition [proposition-six-operations-change-coefficients] it extends to the other
coefficient rings. Since the Frobenius acting on the stalk of the
Weil complex on the fibre at a rational point $x$ of $X_{0,y}$ is
$\operatorname{Frob}_{x,m}$, the stated identity is
Theorem [theorem-grothendieck-lefschetz-trace-formula] for
$X_{0,y}$ over $\mathbf F_{q^m}$, with exponent $1$.
