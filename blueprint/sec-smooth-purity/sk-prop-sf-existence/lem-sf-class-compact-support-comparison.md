+++
id = "lem-sf-class-compact-support-comparison"
kind = "lemma"
title = "On the coefficient class the compact-support functor is computed on the étale site"
order = 2110
uses = ["def-amb-etale-compact-support", "def-compact-support-direct-image-detailed", "def-weil-compactifications-refinements", "def-weil-extension-by-zero", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-extension-by-zero", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-cbc-proetale-extension-zero-comparison", "prop-weil-pbc-comparison-direct-image"]
+++
Let $K_0$ be a field, let $X,Y$ be
finite-type
$K_0$-schemes, let $f:X\to Y$ be a
separated finite-type
$K_0$-morphism with a
compactification
$X\xrightarrow{j}\overline X\xrightarrow{p}Y$, and let $A=A_{E,n}$.
Write $Rf_{!,n}=Rp_*j_!$ for the pro-étale
compact-support functor
attached to that compactification, the extension by zero being the
pro-étale one and $Rp_*$ the
derived direct image, and write
$Rf_!^{\Et}=Rp_{\Et,*}j_!^{\Et}$ for the étale compact-support functor
attached to the same compactification, that of
[def-amb-etale-compact-support], its extension by zero being the
étale one and its proper
direct image $Rp_{\Et,*}$. Let $G\in\Dplus(X_{\Et},A)$ be a
bounded-below complex of $A$-module sheaves on $X_{\Et}$, and let
$K\in\Dplus(X_{\Proet},A)$ come from the étale site with
witness $(G,\alpha)$,
$\alpha:\nu_X^*G\xrightarrow{\sim}K$. Then the canonical comparison

$$
Rf_{!,n}K\xrightarrow{\ \sim\ }\nu_Y^*\bigl(Rf_!^{\Et}G\bigr)
$$

is an isomorphism, natural in the witness.
