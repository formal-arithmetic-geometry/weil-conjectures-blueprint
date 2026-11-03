+++
kind  = "proof"
of    = "prop-weight-purity-roots"
+++
By [def-weil-smooth-proper-cohomological-family], the polynomial
$P_{i,\ell}(T)=\det(1-TF_{i,\ell}\mid V_{i,\ell})$ records the
eigenvalues of the Frobenius operator $F_{i,\ell}$ on $V_{i,\ell}$,
and after scalar extension to $\Qlb$ that operator is the operator
$F_{\Qlb}$ on the module $H^i(X,\Qlb)$ of
[def-weil-frobenius-module-weights]. By
[prop-weight-purity-ordinary] that module is $\iota$-pure of
weight $i$, which by the same definition means that each of its
eigenvalues $\alpha$ satisfies $|\iota(\alpha)|=q^{i/2}$; by
[def-weil-ordinary-reciprocal-roots] the reciprocal roots of
$P_{i,\ell}$ are exactly these eigenvalues, counted with algebraic
multiplicity. This is the assertion, in the situation of
[prop-weight-purity].
