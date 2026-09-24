+++
id = "prop-weil-proper-direct-image-constructibility"
kind = "theorem"
title = "Constructibility of the proper derived direct image"
order = 3154
tags = ["latex:proposition"]
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-direct-image", "def-weil-finite-torsion-constructibility", "def-weil-scheme-morphism-properties", "def-weil-small-proetale-site-detailed"]
+++
Fix a prime $\ell$, write $\Ql=\mathbf Q_\ell$, choose an algebraic
closure $\Qlb$ of $\Ql$, and fix a finite extension $E/\Ql$ contained in
$\Qlb$, with valuation ring $\mathcal O_E$ and a uniformizer
$\varpi_E$. Let $n\in\mathbf Z_{\geq1}$, and put
$A=A_{E,n}=\mathcal O_E/\varpi_E^n$. Let $S$ be a scheme on
which $\ell$ is invertible, let $X,Y$ be
finite-type $S$-schemes, and
let $f:X\to Y$ be a
proper $S$-morphism. On the
small pro-etale sites, for
every $K\in D^b_c(X,A)$ satisfying the
finite-torsion
constructibility condition, the
derived direct image preserves
constructibility: the
cohomology sheaves
$\mathcal H^m(Rf_*K)$ are constructible for every $m\in\mathbf Z$,
that is, $Rf_*K\in D^b_c(Y,A)$.
(*Source: the finiteness theorem for direct images of constructible
sheaves under proper morphisms: Deligne, SGA 4 1/2, Theoreme de
finiteness, Th. 1.1, in the finite-torsion coefficient form used here;
a Stacks form of the compact-support statement is Stacks Project, More
Etale Cohomology, Theorem 63.14.5, Tag
[0GL0](https://stacks.math.columbia.edu/tag/0GL0), with the
subquotient closure Tag
[03RZ](https://stacks.math.columbia.edu/tag/03RZ); the
etale-to-pro-etale transfer is the site comparison of the proper-base-change chapter.*)

## Proof

This is the recorded classical input named in the statement: the finiteness theorem for direct images of constructible sheaves under proper morphisms, Deligne, SGA 4 1/2, Theoreme de finiteness, Theoreme 1.1, in the finite-torsion form used here; the compact-support form with the subquotient closure is Stacks Project, More Etale Cohomology, Theorem 63.14.5 ([Tag 0GL0](https://stacks.math.columbia.edu/tag/0GL0)) with Lemma 59.71.6 ([Tag 03RZ](https://stacks.math.columbia.edu/tag/03RZ)), and the etale-to-pro-etale transfer is the site comparison of the proper-base-change chapter. No separate proof is given.
