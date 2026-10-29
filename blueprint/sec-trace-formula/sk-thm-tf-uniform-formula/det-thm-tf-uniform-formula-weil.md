+++
id = "det-thm-tf-uniform-formula-weil"
kind = "theorem"
title = "Grothendieck–Lefschetz formula for Weil complexes over $E$ and $\\Qlb$"
lean = ["AlgebraicGeometry.WeilSheaf.sum_trace_compactlySupportedCohomology", "AlgebraicGeometry.WeilComplex.sum_trace_compactlySupportedCohomology_eq_sum_traceFunction", "AlgebraicGeometry.WeilComplex.finsum_trace_compactlySupportedCohomology_eq"]
order = 3848
uses = ["sk-thm-tf-uniform-formula", "def-weil-weil-sheaf-complex", "sk-def-sf-weil-complexes", "def-weil-global-geometric-frobenius", "sk-lem-tf-frobenius-convention", "sk-lem-finite", "sk-thm-sfb-qlbar-two-colimit", "det-prop-sfb-finite-extension-compatibility", "sk-p-trace"]
+++
Fix the finite-field datum $p,a,q,k_0,k$, where $q=p^a$, and a prime
$\ell\neq p$. Let $X_0$ be a separated finite-type $k_0$-scheme and put
$X=X_0\times_{k_0}k$. Let $\Lambda\in\{E,\Qlb\}$, with $E/\Ql$ finite in
$\Qlb$ (so $\Lambda=\Ql$ is included), regarded as a condensed ring, and let
$(K,\theta)$ be a Weil complex in the sense of
[def-weil-weil-sheaf-complex]: $K\in\Dbc(X,\Lambda)$ and
$\theta:g_X^*K\xrightarrow{\sim}K$ an isomorphism. For instance $(K,\theta)$
may be a Weil sheaf, or the pair $(\operatorname{For}(K),\theta_K)$ of an
object of $D^b_{c,\mathrm W}(X,\Lambda)$. Since $\Dctf=\Dbc$ for rational
coefficients, this is a Weil complex in the sense of
[sk-def-sf-weil-complexes].

Write $F$ for the global geometric Frobenius of
[def-weil-global-geometric-frobenius] on
$H_c^i(X,K)=H^i\RGammac(X_{\mathrm{pro\acute et}},K)$; it is the operator
$\operatorname{Frob}_{X,K}$ of [sk-thm-tf-uniform-formula]. For
$y\in X_0(\mathbf F_{q^m})$ with geometric point $\bar y$, write
$F_{y,m}=\operatorname{Frob}_{y,m}$ for the local operator on the stalk
$K_{\bar y}$, obtained by iterating $\theta$ $m$ times as in
[sk-thm-tf-uniform-formula]. Then:

1. The $\Lambda$-vector spaces $H_c^i(X,K)$ and $H^j(K_{\bar y})$ are
   finite-dimensional, and only finitely many of them are nonzero.
2. For every $m\geq1$, the operator induced on $H_c^i(X,K)$ by the $m$-th
   iterate of $\theta$ is $F^m$, and in $\Lambda$
   $$
   \boxed{
   \sum_{i\in\mathbf Z}(-1)^i
   \operatorname{Tr}\bigl(F^m\mid H_c^i(X,K)\bigr)
   =\sum_{y\in X_0(\mathbf F_{q^m})}
   \sum_{j\in\mathbf Z}(-1)^j
   \operatorname{Tr}\bigl(F_{y,m}\mid H^j(K_{\bar y})\bigr).}
   $$
3. Let $\Lambda=\Qlb$, and let $(K',\theta')$ be a Weil complex over a
   finite $E'\subset\Qlb$ whose extension of scalars is $(K,\theta)$; such a
   model exists by the descent paragraph of [def-weil-weil-sheaf-complex].
   Then $H_c^i(X,K)=H_c^i(X,K')\otimes_{E'}\Qlb$ and
   $H^j(K_{\bar y})=H^j(K'_{\bar y})\otimes_{E'}\Qlb$, compatibly with the
   operators. Every trace in (2) is the image along $E'\hookrightarrow\Qlb$
   of the corresponding $E'$-valued trace for $(K',\theta')$. The identity
   depends only on $(K,\theta)$, not on the model.
