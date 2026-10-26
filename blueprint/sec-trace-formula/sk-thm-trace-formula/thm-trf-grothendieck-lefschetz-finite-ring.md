+++
id = "thm-trf-grothendieck-lefschetz-finite-ring"
kind = "theorem"
title = "Grothendieck–Lefschetz formula over a finite ring"
order = 3524
uses = ["def-trf-admissibility", "def-trf-coefficient-conventions", "def-trf-frobenius-coefficient-morphism", "def-trf-frobenius-operators", "def-trf-iterated-weil-map", "def-weil-compactifications-refinements", "def-weil-finite-field-fiber", "def-weil-pbc-etale-origin-witness", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "lem-trf-frobenius-degree-formula", "lem-trf-iterated-weil-cocycle", "lem-trf-local-frobenius-conjugacy", "prop-trf-graph-frobenius-operator", "prop-trf-scheme-galois-comparison", "thm-trf-coefficient-morphism-trace-formula", "thm-trf-frobenius-fixed-points"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, and the
coefficient conventions,
$A=A_{E,n}$. Let $X_0$ be a
separated finite-type
$k_0$-scheme, put $X=X_0\times_{k_0}k$, let
$(K,\varphi)\in D^b_{ctf,\mathrm W}(X,A)$ be a
strict Weil complex whose
underlying $K$ has an
explicit etale-origin
witness, and assume
the exceptional-adjoint admissibility
hypotheses of [def-trf-admissibility] for the structure morphism
and the fixed-point base changes, including those on a chosen
compactification
defined over $k_0$. For every integer $m\geq1$,

$$
\boxed{
\operatorname{tr}_A\bigl(F_{c,K}^{\,m}\mid R\Gamma_c(X,K)\bigr)
=
\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_A\bigl(F_{y,m}\mid K_{\bar y}\bigr).}
$$

Equivalently, in the closed-point form,

$$
\operatorname{tr}_A\bigl(F_{c,K}^{\,m}\mid R\Gamma_c(X,K)\bigr)
=
\sum_{\substack{x\in|X_0|\\d_x\mid m}}
d_x\,\operatorname{tr}_A
\bigl(F_x^{\,m/d_x}\mid K_{\bar x}\bigr).
$$

Both sides lie in $A$, and both sums are finite.
