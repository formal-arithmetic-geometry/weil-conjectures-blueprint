+++
id = "det-pd-generic-direct-image"
kind = "lemma"
title = "Geometric generic restriction commutes with direct image"
uses = ["sbc-thm-bounded-below-derived-smooth-base-change", "lem-weil-pbc-derived-cohomology-continuity", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $B$ be a smooth integral curve over $k$, let
$\bar\eta=\operatorname{Spec}\overline{k(B)}$, and for a finite-type
$B$-scheme $T$ let $g_T\colon T_{\bar\eta}=T\times_B\bar\eta\to T$ be the
projection. Let $A$ be a finite coefficient ring, let $h\colon T\to X$ be a
separated finite-type $B$-morphism, and let $L\in D^b_c(T_{\mathrm{\acute et}},A)$.
Then the base change morphism

$$
g_X^*Rh_*L\longrightarrow Rh_{\bar\eta,*}g_T^*L
$$

is an isomorphism in $D(X_{\bar\eta,\mathrm{\acute et}},A)$.
