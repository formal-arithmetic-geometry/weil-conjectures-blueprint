+++
kind  = "proof"
of    = "det-prop-reciprocity"
+++
By the complement of [sk-cor-tf-functional-equation] the eigenvalues of $F$ on $V_{2d-i,\ell}$ are
$q^{d}\alpha^{-1}$ for $\alpha$ ranging over the eigenvalues of $F$ on
$V_{i,\ell}$, each with multiplicity. Passing to determinants,

$$
P_{2d-i,\ell}(T)=\det(1-TF\mid V_{2d-i,\ell})
=\prod_\alpha\bigl(1-q^{d}\alpha^{-1}T\bigr)
=c_i\,T^{b_i}P_{i,\ell}\bigl(q^{-d}T^{-1}\bigr)
$$

for a constant $c_i$ determined by the leading coefficients. Indeed
$T^{b_i}P_{i,\ell}(q^{-d}T^{-1})=\prod_\alpha(T-\alpha q^{-d}) =(-1)^{b_i}q^{-db_i}\bigl(\prod_\alpha\alpha\bigr)\prod_\alpha (1-q^{d}\alpha^{-1}T)$, and $\prod_\alpha\alpha=\det(F\mid V_{i,\ell})=D_i$
because $[T^{b_i}]P_{i,\ell}=(-1)^{b_i}\det(F\mid V_{i,\ell})$ and $D_i$ is
defined with the sign $(-1)^{b_i}$; hence
$c_i=(-1)^{b_i}q^{db_i}D_i^{-1}$. Substituting $T\mapsto q^{-d}T^{-1}$ in the
resulting identity gives the first displayed formula, and putting $2d-i$ in
place of $i$ and comparing leading coefficients gives
$D_{2d-i}=q^{db_i}D_i^{-1}$, which is the second. By [thm-wweil-integral-factors]
the polynomials on both sides are the coefficientwise extensions of the
integral factors, so the identity holds in $\Q(T)$ and hence in $\Z[T]$ after
clearing.

The parity of $d\chi$ is part of the complement of
[sk-cor-tf-functional-equation]: $b_i=b_{2d-i}$ gives
$\chi\equiv b_d\pmod 2$, and for odd $d$ the middle pairing is perfect and
alternating, so $b_d$ is even.
