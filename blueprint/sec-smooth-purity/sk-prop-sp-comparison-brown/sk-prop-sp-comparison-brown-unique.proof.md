+++
kind = "proof"
of = "det-sp-comparison-brown-unique"
+++
*Same left adjoint.* In both settings $Rf_!$ is $R\bar f_*\circ j_!$ for a
compactification $f=\bar f\circ j$, computed by the ordinary derived functors on
module sheaves, and it is independent of the compactification; so the left
adjoints coincide on $\Dctf(X,\Lambda)$.

*Restriction.* The Brown adjoint $f^!$ is right adjoint to $Rf_!$ on the
localizing hulls, and by the existence theorem it maps $\Dctf(Y,\Lambda)$ into
$\Dctf(X,\Lambda)$. Since $\Dctf(-,\Lambda)$ is a full subcategory of its
localizing hull, the bijection
$\operatorname{Hom}(Rf_!M,K)\simeq\operatorname{Hom}(M,f^!K)$ for $M\in\Dctf(X,\Lambda)$,
$K\in\Dctf(Y,\Lambda)$ is the restriction of the bijection on the hulls; so the
restricted $f^!$ is a right adjoint of $Rf_{!,\Lambda}$ on $\Dctf$, with the
restricted counit.

*Uniqueness.* By [det-sp-comparison-brown-explicit] the functor
$f^*_\Lambda(-)(d)[2d]$ is another right adjoint of $Rf_{!,\Lambda}$ on $\Dctf$. By
[det-sp-unique-right-adjoint] there is a unique natural isomorphism between the
two right adjoints compatible with the counits, and it is the stated one.
