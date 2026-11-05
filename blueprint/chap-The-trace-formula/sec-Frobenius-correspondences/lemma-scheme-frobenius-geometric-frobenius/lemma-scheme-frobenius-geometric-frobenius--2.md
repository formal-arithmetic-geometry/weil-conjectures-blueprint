+++
id = "lemma-scheme-frobenius-geometric-frobenius--2"
kind = "lemma"
title = "Iterating a Weil structure as a coefficient morphism"
name_showing = false
order = 953002
aliases = ["bp-r290-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.iterateStr_hom_eq_frobeniusCoefficientIterate"]
uses = ["definition-weil-structure", "definition-frobenius-correspondences-their-operators"]
+++
Lean bypasses transport by $\kappa_m$ and uses a Weil structure for a single
endomorphism $\Phi$.

Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be prime, and let
$X/k$ be separated and of finite type. Let $\Phi:X\to X$ be a $k$-endomorphism
and let $K\in\Dbc(X,\Qbarl)$ in the condensed coefficient model carry an
isomorphism $\phi:\Phi^*K\xrightarrow{\sim}K$. Write
$\Phi_m=\Phi^m$, and let $\phi_m:\Phi_m^*K\xrightarrow{\sim}K$ be the
iterated Weil structure. Regard the underlying morphism of $\phi$ as a
coefficient morphism $\psi:\Phi^*K\to K$, with iterates as in
[definition-frobenius-correspondences-their-operators]. Then, for every
$m\geq0$, the underlying morphism of $\phi_m$ is $\psi_m$.

Here both iterations use the canonical identity and composition isomorphisms
of pullback; no properness or invertibility of $\Phi$ is required.
