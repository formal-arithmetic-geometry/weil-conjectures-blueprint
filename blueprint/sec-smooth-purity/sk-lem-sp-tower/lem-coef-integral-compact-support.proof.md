+++
kind  = "proof"
of    = "lem-coef-integral-compact-support"
uses = ["def-pe-derived-complete"]
+++
The input reductions have a common Tor interval by
[lem-coef-integral-residue-tor]. The functor $Rf_!$ sends
$D^b_c(X,R)=D^b_{ctf}(X,R)$ into $D^b_c(Y,R)$ ([sk-thm-existence], (2)). The
canonical coefficient comparison
$(Rf_!K)\otimes^{\mathbf L}_RA_n\to Rf_{!,n}K_n$ along $R\to A_n$ is an
isomorphism ([sk-prop-scalar-six]). Alternatively, membership in
$D^b_c(Y,R)$ follows from the integral criterion
[sk-prop-integral-criterion]. $Rf_!K$ is derived complete [def-pe-derived-complete], because $R\bar f_*$
and $j_!$ commute with $R\varprojlim$ and $K\simeq R\varprojlim_nK_n$. Its
reduction modulo $\pi_E$ is $Rf_{!,1}K_1$, which is bounded constructible.

For the Tor interval, compute at finite level. On a compactification
$f=\bar f j$, replace the compactifying scheme by the
scheme-theoretic closure of $X$. Its dimension is at most
$d$. Extension by zero preserves constructibility and the
Tor interval. The proper direct-image theorem
[thm-sf-direct-image-tor-amplitude], with the bound of
[lem-sf-etale-direct-image-vanishing], therefore gives
$[a,b+2d]$ for $R\bar f_*j_!K_n$.
The finite compact-support site comparison is
[thm-cbc-finite-level-proetale]. The comparisons for the different $n$ are
compatible with the finite reductions $A_n\to A_m$
([lem-fix-compact-support-coefficient-change]), since all of them are
instances of the coefficient comparison of [sk-prop-scalar-six], which
respects composition.
