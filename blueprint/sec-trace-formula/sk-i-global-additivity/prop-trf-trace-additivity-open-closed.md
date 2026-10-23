+++
id = "prop-trf-trace-additivity-open-closed"
kind = "theorem"
title = "Additivity of the Frobenius traces along an open–closed decomposition"
lean = ["AlgebraicGeometry.ProEtale.trace_globalOperator_eq_trace_add_trace"]
order = 3535
tags = ["latex:proposition"]
uses = ["def-exchange-projection", "def-trf-categorical-trace", "def-trf-frobenius-coefficient-morphism", "def-trf-frobenius-operators", "def-trf-iterated-weil-map", "def-trf-scheme-frobenius", "def-trf-strict-weil-complex", "def-trf-weil-extension-zero", "fix-lem-exchanges", "lem-trf-adjoint-mate", "lem-trf-frobenius-open-square", "lem-trf-frobenius-operator-compact-description", "lem-trf-open-square-exchange", "prop-functor-package", "prop-sf-open-closed-triangle-all-stages", "prop-trf-compact-support-perfectness", "prop-trf-graph-operator", "prop-trf-trace-formal-laws", "prop-weil-open-closed-recollement-adjunctions", "thm-sf-ctf-stability"]
+++
Fix the global finite-field datum
and the coefficient conventions, $A=A_{E,n}$. Let $X_0$ be a
separated finite-type $k_0$-scheme, let $i_0:Z_0\hookrightarrow X_0$
be a closed immersion with complementary open immersion
$j_0:U_0\hookrightarrow X_0$, and let $i:Z\hookrightarrow X$,
$j:U\hookrightarrow X$ be their base changes to $k$. Let
$(K,\varphi)\in D^b_{ctf,\mathrm W}(X,A)$ be a strict Weil complex
of [def-trf-strict-weil-complex].

1. For $h\in\{i,j\}$ with source $W\in\{Z,U\}$, one has
$h\,g_W=g_X\,h$, and the composite
$$
h^*\varphi:\;
Lg_W^*Lh^*K\xrightarrow{\ \sim\ }Lh^*Lg_X^*K
\xrightarrow{\ Lh^*\varphi\ }Lh^*K
$$
of the canonical pullback identification with $Lh^*\varphi$ makes
$(Lh^*K,h^*\varphi)$ a strict Weil complex on $W$; its iterates of
[def-trf-iterated-weil-map] are
$(h^*\varphi)^{[m]}=Lh^*\varphi^{[m]}\circ c_{h,m}$, with
$c_{h,m}:Lg_W^{m*}Lh^*\xrightarrow{\sim}Lh^*Lg_X^{m*}$ the canonical
identification.
1. For every $m\geq1$, with $F_{c,-}^{\,m}$ the global geometric
Frobenius operators of [def-trf-frobenius-operators] for these
Weil structures,
$$
\operatorname{tr}_A\bigl(F_{c,K}^{\,m}\mid R\Gamma_c(X,K)\bigr)
=
\operatorname{tr}_A\bigl(F_{c,j^*K}^{\,m}\mid R\Gamma_c(U,j^*K)\bigr)
+
\operatorname{tr}_A\bigl(F_{c,i^*K}^{\,m}\mid R\Gamma_c(Z,i^*K)\bigr)
$$
in $A$. These are categorical traces of perfect complexes in the
sense of [def-trf-categorical-trace]; no trace of an individual
cohomology module occurs.
1. *(Frobenius coefficient morphisms.)* Let instead
$K\in D^b_{ctf}(X,A)$ carry an arbitrary Frobenius coefficient
morphism $\psi:L\Phi_X^*K\to K$ of
[def-trf-frobenius-coefficient-morphism], with no Weil structure and no
invertibility. For $h\in\{i,j\}$ with source $W$ one has
$h\,\Phi_W=\Phi_X\,h$, the composite
$h^*\psi:L\Phi_W^*Lh^*K\xrightarrow{\sim}Lh^*L\Phi_X^*K
\xrightarrow{Lh^*\psi}Lh^*K$ is a Frobenius coefficient morphism on
$W$ with iterates $(h^*\psi)_m=Lh^*\psi_m\circ c'_{h,m}$, where
$c'_{h,m}:L\Phi_W^{m*}Lh^*\xrightarrow{\sim}Lh^*L\Phi_X^{m*}$ is the
canonical identification, and for every $m\geq1$ the global operators
$F_{c,m}$ of [def-trf-frobenius-coefficient-morphism] satisfy
$$
\operatorname{tr}_A\bigl(F_{c,m}(\psi)\mid R\Gamma_c(X,K)\bigr)
=
\operatorname{tr}_A\bigl(F_{c,m}(j^*\psi)\mid R\Gamma_c(U,j^*K)\bigr)
+
\operatorname{tr}_A\bigl(F_{c,m}(i^*\psi)\mid R\Gamma_c(Z,i^*K)\bigr).
$$

The proof below uses the Weil maps only as morphisms: the
invertibility of $\varphi$ is used only to stay inside the category
$D^b_{ctf,\mathrm W}$ on which $F_{c,-}^{\,m}$ is defined.
