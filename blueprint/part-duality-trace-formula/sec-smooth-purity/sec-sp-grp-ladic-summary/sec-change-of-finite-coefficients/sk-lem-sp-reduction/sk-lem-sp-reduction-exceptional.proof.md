+++
kind = "proof"
of = "det-sp-reduction-exceptional"
+++
*Existence, uniqueness, naturality.* The right-hand side of the defining
identity is a morphism $Rf_{!,B}((f_A^!K)_B)\to K_B$, using
$b(f_A^!K)$ of [det-sp-reduction-direct-image]. By the adjunction
$Rf_{!,B}\dashv f_B^!$ it has a unique transpose
$(f_A^!K)_B\to f_B^!(K_B)$, which is $c_{A,B}(K)$. Since $b$, $\varepsilon_A$,
$\varepsilon_B$ and extension of scalars are natural, so is $c_{A,B}$.

*Locality.* Whether a morphism in $\Dctf(X_{\mathrm{proét}},B)$ is an isomorphism
can be checked after restriction to the members of an open cover. The
restriction of $c_{A,B}$ to an open $U$ is the comparison for $f|_U$, because
for an open immersion $u:U\to X$ the adjunctions compose
($R(f u)_!=Rf_!u_!$, $(fu)^!=u^*f^!$), $b$ is compatible with $u_!$ (extension
by zero commutes with extension of scalars), and transposes of composites are
composites of transposes.

*Charts.* On a chart $f|_U=p_d\circ e$, the right adjoint over $A$ is
$e^*p_d^*(-)(d)[2d]$ and its counit is built from: summation over the
geometric fibres of $e$ (the counit of $e_!\dashv e^*$), the Kummer class of
$\mathcal O_{\mathbf P^1}(1)$, the diagonal class on
$\mathbf P^1\times\mathbf P^1$, and the splitting of $Rq_*$ of the constant
sheaf on $\mathbf P^1$ into two free summands of rank one with the projection
onto the twisted one (the iterated projective-line integration). Each of these
commutes with extension of coefficients: summation over fibres is defined
integrally; the Kummer and diagonal classes over $B$ are the images of those
over $A$ (they come from $\mathbf Z/\ell^n$); and the splitting consists of
free rank-one summands, whose derived extension is the ordinary one
([det-sp-scalar-extension-functor]). Hence $(\varepsilon_A(K))_B\circ
b^{-1}$ is the counit over $B$ evaluated at $K_B$, precomposed with $Rf_{!,B}$ of
the canonical isomorphism
$(e^*p_d^*K(d)[2d])_B\simeq e^*p_d^*(K_B)(d)[2d]$. By uniqueness of transposes,
$c_{A,B}(K)|_U$ is this canonical isomorphism, in particular an isomorphism.
Coordinate charts cover $X$, so $c_{A,B}(K)$ is an isomorphism.
