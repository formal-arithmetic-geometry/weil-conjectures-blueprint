+++
kind  = "proof"
of    = "sk-prop-reciprocity"
+++
By [sk-thm-poincare-duality] (5) the eigenvalues of $F$ on $V_{2d-i,\ell}$ are
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
$D_{2d-i}=q^{db_i}D_i^{-1}$, which is the second. By [sk-thm-intfactors]
the polynomials on both sides are the coefficientwise extensions of the
integral factors, so the identity holds in $\Q(T)$ and hence in $\Z[T]$ after
clearing.

For the parity of $d\chi$, pair $i$ with $2d-i$ and use
$b_i=b_{2d-i}$ of [sk-thm-poincare-duality] (3):

$$
\chi=\sum_{i=0}^{2d}(-1)^{i}b_i
=2\sum_{i<d}(-1)^{i}b_i+(-1)^{d}b_d,
\qquad\text{so}\qquad d\chi\equiv d\,b_d \pmod 2 .
$$

If $d$ is even this is $0$; if $d$ is odd then $b_d$ is even by
[sk-thm-poincare-duality] (3), whose sign rule
$\langle y,x\rangle_{2d-i}=(-1)^i\langle x,y\rangle_i$ makes the middle pairing
alternating for odd $d$, because a nondegenerate alternating form on a
finite-dimensional vector space has even dimension. Hence $d\chi$ is even in
both cases.
