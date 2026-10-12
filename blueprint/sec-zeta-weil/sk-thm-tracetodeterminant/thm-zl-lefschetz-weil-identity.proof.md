+++
kind  = "proof"
of    = "thm-zl-lefschetz-weil-identity"
+++
Step 1: the point-count identity. The scheme $X_0$ is proper, so by
[cor-trf-point-counting] applied to the constant Weil sheaf
$(\Qlb)_X$, for every $n\geq1$,

$$
N_n:=\#X_0(\mathbf F_{q^n})
=\sum_{i\in\mathbf Z}(-1)^i\Tr\bigl(F^n\mid H^i(X,\Qlb)\bigr)
=\sum_{i=0}^{2d}(-1)^i\Tr(F_i^n\mid V_i),
$$

the second identity being the finite-dimensionality, the vanishing
outside $0\leq i\leq2d$, and the identification
$V_i=H^i(X,\Qlb)$, $F_i=F|_{V_i}$, supplied by
[def-weil-ordinary-compact-cohomology] (compactly supported
cohomology being the ordinary one for proper $X_0$, per that
definition) and by [def-weil-smooth-proper-cohomological-family]
after scalar extension to $\Qlb$.

Step 2: the logarithm of the zeta series. By
[def-weil-point-counts-zeta],

$$
Z(X_0,T)=\exp\left(\sum_{n\geq1}N_n\frac{T^n}{n}\right),
$$

so that, the formal logarithm and the exponential being mutually
inverse on $T\Qlb[[T]]$ and $1+T\Qlb[[T]]$,

$$
\log Z(X_0,T)=\sum_{n\geq1}N_n\frac{T^n}{n}.
$$

Step 3: substitution and interchange. Inserting Step 1 and using that
the sum over $i=0,\ldots,2d$ is finite while the coefficientwise sums
over $n$ are formal,

$$
\log Z(X_0,T)
=\sum_{n\geq1}\sum_{i=0}^{2d}(-1)^i\Tr(F_i^n\mid V_i)\frac{T^n}{n}
=\sum_{i=0}^{2d}(-1)^i
\left(\sum_{n\geq1}\Tr(F_i^n\mid V_i)\frac{T^n}{n}\right).
$$

Step 4: the per-degree logarithm. For every $i$, the pair
$(V_i,F_i)$ is a Frobenius module, so [lem-zl-log-det-identity]
gives

$$
\sum_{n\geq1}\Tr(F_i^n\mid V_i)\frac{T^n}{n}
=-\log P_{i,\ell}(T).
$$

Hence, by the additivity of the formal logarithm on finite products of
series with constant coefficient $1$,

$$
\log Z(X_0,T)
=\sum_{i=0}^{2d}(-1)^{i+1}\log P_{i,\ell}(T)
=\log\left(\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}\right).
$$

Step 5: exponentiation. Both sides of the identity of Step 4 have the
same logarithm and lie in $1+T\Qlb[[T]]$, so applying the formal
exponential, which is inverse to the logarithm on that set, gives the
displayed identity.
