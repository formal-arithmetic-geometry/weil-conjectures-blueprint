+++
kind = "proof"
of = "sk-cor-tf-trace-function-pushforward"
uses = ["sk-i-relative-frob", "sk-lem-tf-frobenius-convention", "sk-prop-scalar-six", "sk-thm-tf-uniform-formula"]
+++
Fix $y$ and let $X_{0,y}$ be the fibre of $f_0$ over $y$, a separated
scheme of finite type over $\mathbf F_{q^m}$ whose rational points are
the $x\in X_0(\mathbf F_{q^m})$ with $f_0(x)=y$. Restrict $K$ to its
geometric fibre $X_{\bar y}$ and give the restriction the Weil
structure over $\mathbf F_{q^m}$ obtained from the $m$-th iterate of
$\phi$. Base change for compact supports identifies $(Rf_!K)_{\bar y}$ with
$R\Gamma_c(X_{\bar y},K|_{X_{\bar y}})$, and identifies
$\operatorname{Frob}_{y,m}$ with the geometric Frobenius operator of
this Weil complex. For finite $A$ this is part (4) of
Lemma [sk-i-relative-frob], applied to the Frobenius
correspondence $\phi\kappa_1$ and translated by
Lemma [sk-lem-tf-frobenius-convention], and the comparisons of
Proposition [sk-prop-scalar-six] extend it to the other
coefficient rings. Since the Frobenius acting on the stalk of the
Weil complex on the fibre at a rational point $x$ of $X_{0,y}$ is
$\operatorname{Frob}_{x,m}$, the stated identity is
Theorem [sk-thm-tf-uniform-formula] for
$X_{0,y}$ over $\mathbf F_{q^m}$, with exponent $1$.
