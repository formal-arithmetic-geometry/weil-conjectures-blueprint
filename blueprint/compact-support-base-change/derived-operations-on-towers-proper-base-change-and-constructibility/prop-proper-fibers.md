+++
id = "prop-proper-fibers"
kind = "theorem"
title = "Proper base change on geometric fibers"
order = 3151
tags = ["latex:proposition"]
uses = ["cor-weil-pbc-geometric-fiber-finite", "def-exchange-projection", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "prop-weil-proet-finite-proper-base-change", "thm-weil-pbc-finite-level-proetale"]
+++
Fix a prime $\ell$, write $\Ql=\mathbf Q_\ell$, choose an algebraic
closure $\Qlb$ of $\Ql$, and fix a finite extension $E/\Ql$ contained in
$\Qlb$, with valuation ring $\mathcal O_E$ and a uniformizer
$\varpi_E$. Let $n\in\mathbf Z_{\geq1}$, and put
$A=A_{E,n}=\mathcal O_E/\varpi_E^n$. Let $\Omega$ be an
algebraically closed field with $\operatorname{char}(\Omega)\ne\ell$, let
$X,Y$ be
finite-type $\Omega$-schemes,
let $f:X\to Y$ be a
proper morphism, and let
$K\in D^b_c(X,A)$ be a bounded complex satisfying the
finite-torsion
constructibility condition on the
small pro-etale site. For every
geometric point
$\bar y:\operatorname{Spec}\Omega_y\to Y$, where $\Omega_y$ is an
algebraically closed extension of the residue field of the image of $\bar y$,
put
$X_{\bar y}=X\times_Y\operatorname{Spec}\Omega_y$. Let
$\bar g':X_{\bar y}\to X$ be the projection and
$a_{X_{\bar y}}:X_{\bar y}\to\operatorname{Spec}\Omega_y$ be the structure
morphism. The
exchange transformation on this fiber is
the base-change map for the
derived direct image. The symbols
$L\bar y^*$ and $L\bar g'^*$ below use the
derived pullback notation;
namely, the isomorphism

$$
L\bar y^*Rf_*K\xrightarrow{\sim}
R(a_{X_{\bar y}})_*L\bar g'^*K.
$$

(*Source: the finite-torsion proper base change theorem on the
small pro-etale sites: Stacks Project, Pro-etale Cohomology, Section
61.30 (Proper base change), Theorem 61.30.1, Tag `09C9`; the
geometric-fiber form is the restriction of loc. cit. to the geometric
point.*)

## Proof

This is the decomposed form of the classical input of the source note:
the geometric-fiber proper base change is proved in the proper-base-change chapter as
[cor-weil-pbc-geometric-fiber-finite] by specializing
[prop-weil-proet-finite-proper-base-change] to a geometric fiber, and the
pro-etale level transport is [thm-weil-pbc-finite-level-proetale].
