+++
kind = "proof"
of = "corollary-trace-functions-direct-image-compact"
order = 1026
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-w-local-components", "lemma-extremally-disconnected-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "theorem-enough-affine-weakly-contractible-objects", "definition-weak-contractibility", "proposition-pro-etale-site-separably-closed", "definition-pro-etale-base-change-map", "lemma-naturality-pasting-comparison", "proposition-construction-independence-rf-shriek", "theorem-f-shriek-ell-adic-coefficients", "lemma-perfect-complexes-geometric-point", "definition-frobenius-operator", "definition-categorical-trace", "proposition-properties-trace", "definition-trace-class-local-terms", "definition-action-correspondence", "theorem-proper-pushforward-lefschetz-verdier", "definition-frobenius-correspondences-their-operators", "lemma-scheme-frobenius-geometric-frobenius", "lemma-frobenius-fixed-scheme", "proposition-frobenius-local-term-curve", "lemma-comparison-via-relative-frobenius", "theorem-nagata-s-compactification-theorem", "lemma-finite-direct-images"]
+++
The left side is a trace on a stalk of [$Rf_!K$](@proposition-construction-independence-rf-shriek). By base change that
stalk is the [compactly supported cohomology](@proposition-construction-independence-rf-shriek) of a fibre. Hence the corollary
is the [trace formula](@theorem-grothendieck-lefschetz-trace-formula) for the fibre, once we check that the [Frobenius
operators](@definition-frobenius-operator) correspond.

Fix $y$ and let $X_{0,y}$ be the fibre of $f_0$ over $y$. It is a separated
scheme of finite type over $\mathbf F_{q^m}$, and its rational points are
the $x\in X_0(\mathbf F_{q^m})$ with $f_0(x)=y$. Restrict $K$ to its
geometric fibre $X_{\bar y}$ and give the restriction the [Weil
structure](@definition-weil-structure) over $\mathbf F_{q^m}$ obtained from the $m$-th iterate of
$\phi$. By [base change for compact supports](@proposition-composition-base-change-rf-shriek), $(Rf_!K)_{\bar y}$ is
$R\Gamma_c(X_{\bar y},K|_{X_{\bar y}})$, and
[$\operatorname{Frob}_{y,m}$](@theorem-grothendieck-lefschetz-trace-formula) is the [geometric Frobenius operator](@definition-frobenius-operator) of
this [Weil complex](@definition-weil-structure). For finite $A$ this is part (4) of
Lemma [lemma-comparison-via-relative-frobenius], applied to the [Frobenius
correspondence](@definition-frobenius-correspondences-their-operators) $\phi\kappa_1$ and translated by
Lemma [lemma-scheme-frobenius-geometric-frobenius]. By the comparisons of
Proposition [proposition-six-operations-change-coefficients] it extends to the other
coefficient rings. Since the Frobenius acting on the stalk of the
[Weil complex](@definition-weil-structure) on the fibre at a rational point $x$ of $X_{0,y}$ is
[$\operatorname{Frob}_{x,m}$](@theorem-grothendieck-lefschetz-trace-formula), the stated identity is
Theorem [theorem-grothendieck-lefschetz-trace-formula] for
$X_{0,y}$ over $\mathbf F_{q^m}$, with exponent $1$.
