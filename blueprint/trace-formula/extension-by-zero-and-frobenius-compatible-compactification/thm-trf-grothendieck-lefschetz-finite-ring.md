+++
id = "thm-trf-grothendieck-lefschetz-finite-ring"
kind = "theorem"
title = "Grothendieck–Lefschetz formula over a finite ring"
order = 3946
uses = ["def-trf-admissibility", "def-trf-coefficient-conventions", "def-trf-weil-extension-zero", "def-weil-compactifications-refinements", "def-weil-finite-field-fiber", "def-weil-pbc-etale-origin-witness", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "lem-trf-compactification-cohomology", "lem-trf-extension-zero-stalk-traces", "lem-trf-frobenius-degree-formula", "lem-trf-local-frobenius-conjugacy", "prop-trf-compactification-frobenius", "prop-trf-graph-frobenius-operator", "thm-nagata-compactification", "thm-trf-frobenius-fixed-points", "thm-trf-frobenius-local-term", "thm-trf-lefschetz-verdier"]
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

## Proof

Compactifications over $\mathbf F_q$ exist by
[thm-nagata-compactification]; choose
$j_0:X_0\hookrightarrow\bar X_0$ with the admissibility assumed
in the statement, and base change it to $j:X\hookrightarrow\bar X$.
The Weil extension $\bar K=j_!K$ remains in $D^b_{ctf}$ by
[def-trf-weil-extension-zero]. The comparison

$$
R\Gamma_c(X,K)\xrightarrow{\sim}R\Gamma(\bar X,\bar K)
$$

is [lem-trf-compactification-cohomology], and
[prop-trf-compactification-frobenius] identifies the two global
Frobenius operators for every $m\geq1$. Hence their traces agree.

On the proper scheme $\bar X$, the graph of $\Phi_{\bar X}^m$
has global operator equal to the $m$-th Frobenius by
[prop-trf-graph-frobenius-operator]. The
Lefschetz–Verdier comparison [thm-trf-lefschetz-verdier]
therefore expresses its trace as the sum of genuine local terms.
The fixed-scheme calculation [thm-trf-frobenius-fixed-points]
gives

$$
\operatorname{Fix}(\Phi_{\bar X}^m)
\cong\coprod_{y\in\bar X_0(\mathbf F_{q^m})}\Spec k.
$$

Apply the local-term theorem
[thm-trf-frobenius-local-term] to identify each of these
local terms with the ordinary Frobenius trace on the corresponding
stalk of $\bar K$. Only after this step may
[lem-trf-extension-zero-stalk-traces] be applied: the stalk
trace is zero on $\bar X_0\setminus X_0$, and equals the stated
trace of $K_{\bar y}$ at $y\in X_0(\mathbf F_{q^m})$.
The surviving sum is the boxed formula. Grouping the rational
points above a closed point and applying
[lem-trf-frobenius-degree-formula] and
[lem-trf-local-frobenius-conjugacy] gives the second formula.

The extension-by-zero Weil structure and compact-support comparison
have been proved above without a trace input. The two interfaces that an
earlier form of this proof recorded as conditional are discharged in this
chapter: the Lefschetz–Verdier comparison by
[thm-trf-lefschetz-verdier] and the identification of the local terms
with the ordinary Frobenius traces by
[thm-trf-frobenius-local-term]. The compactification used at the
beginning of the proof is [thm-nagata-compactification], whose own
status is recorded in the compactification chapter.
