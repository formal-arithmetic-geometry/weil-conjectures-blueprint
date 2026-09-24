+++
id = "lem-weil-proper-direct-image-cohomology-sheaf"
kind = "lemma"
title = "Constructibility of the cohomology sheaves of $Rf_*\\mathcal H^r(K)$"
order = 3155
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-direct-image", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "prop-weil-proper-direct-image-constructibility"]
+++
In the situation of
[prop-weil-proper-direct-image-constructibility], let
$K\in D^b_c(X,A)$ satisfy the
finite-torsion
constructibility condition. Then for all $j,r\in\mathbf Z$ the
sheaf $\mathcal H^j(Rf_*\mathcal H^r(K))$ is
constructible on
the small pro-etale site of
$Y$.

## Proof

Each cohomology sheaf $\mathcal H^r(K)$ of a complex satisfying the
finite-torsion constructibility condition is constructible, and the
shifted sheaf complex $\mathcal H^r(K)[-r]$ is again an object of
$D^b_c(X,A)$ satisfying that condition; applying
[prop-weil-proper-direct-image-constructibility] to it exhibits
$\mathcal H^j(Rf_*\mathcal H^r(K)[-r])=\mathcal H^{j-r}(Rf_*\mathcal H^r(K))$ as constructible for every $j\in\mathbf Z$. As $r$ and
$j$ are arbitrary this is the assertion.
