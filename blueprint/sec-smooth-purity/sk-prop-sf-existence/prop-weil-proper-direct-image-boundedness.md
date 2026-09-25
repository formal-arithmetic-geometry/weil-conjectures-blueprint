+++
id = "prop-weil-proper-direct-image-boundedness"
kind = "theorem"
title = "Boundedness of the proper derived direct image"
order = 1854
tags = ["latex:proposition"]
uses = ["def-weil-constructible-intervals", "def-weil-derived-cohomology-sheaves", "def-weil-derived-direct-image", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties"]
+++
Fix a prime $\ell$, write $\Ql=\mathbf Q_\ell$, choose an algebraic
closure $\Qlb$ of $\Ql$, and fix a finite extension $E/\Ql$ contained in
$\Qlb$, with valuation ring $\mathcal O_E$ and a uniformizer
$\varpi_E$. Let $n\in\mathbf Z_{\geq1}$, and put
$A=A_{E,n}=\mathcal O_E/\varpi_E^n$. Let $S$ be a scheme on
which $\ell$ is invertible, let $X,Y$ be
finite-type $S$-schemes, and
let $f:X\to Y$ be a
proper $S$-morphism
whose geometric fibers have
dimension at most $e\in\mathbf Z_{\geq0}$. Let
$K\in D^b_c(X,A)$ satisfy the
finite-torsion
constructibility condition on the
small pro-etale site, and let the
cohomological interval $[u,v]$
satisfy $\mathcal H^r(K)=0$ for every $r\notin[u,v]$, where
$\mathcal H^r$ is the
cohomology-sheaf functor.
Then the derived direct image
is bounded,

$$
\mathcal H^m(Rf_*K)=0\qquad\text{for every }m\notin[u,v+2e],
$$

i.e. the bounded class with interval $[u,v]$ is carried to the
bounded class with interval $[u,v+2e]$: the derived direct image of a
bounded complex is bounded.
(*Source: the fibre-dimension amplitude bound of the classical
finiteness package: Stacks Project, Etale Cohomology, Lemma 59.92.2,
Tag [095U](https://stacks.math.columbia.edu/tag/095U) (for a
proper morphism whose fibres have dimension at most $e$, $R^qf_*F=0$
for $q>2e$, the case of schemes of finite type over a base on which
$\ell$ is invertible being the reduction of loc. cit.).*)

## Proof

This is the recorded classical input named in the statement, Stacks Project, Etale Cohomology, Lemma 59.92.2 ([Tag 095U](https://stacks.math.columbia.edu/tag/095U)): for a proper morphism whose geometric fibres have dimension at most e, the higher direct images of a torsion sheaf vanish above degree 2e, which combined with the vanishing interval of K gives the displayed amplitude bound. No separate proof is given.
