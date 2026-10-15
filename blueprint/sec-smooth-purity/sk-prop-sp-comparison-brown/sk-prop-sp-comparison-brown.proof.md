+++
kind = "proof"
of = "sk-prop-sp-comparison-brown"
uses = ["sk-thm-smooth-purity", "sk-prop-sp-integral-adjunction", "sk-prop-sp-rational", "sk-thm-sp-qbar", "sk-prop-sf-existence", "sk-thm-existence", "sk-prop-sp-unique-adjoint"]
+++
Both adjunctions live on $\Dctf(X,\Lambda)$ and $\Dctf(Y,\Lambda)$, and in both
$Rf_!$ is the composite $R\bar f_*\circ j_!$ of ordinary derived functors on
module sheaves for a compactification $f=\bar f\circ j$, independent of the
compactification. Finite purity ([sk-thm-smooth-purity]), the integral
adjunction ([sk-prop-sp-integral-adjunction]) and its rational extensions
([sk-prop-sp-rational] and [sk-thm-sp-qbar]) show, in the respective coefficient
cases, that $K\mapsto f_\Lambda^*K(d)[2d]$ is right adjoint to $Rf_{!,\Lambda}$. By
[sk-prop-sf-existence] and [sk-thm-existence], the restriction of $f^!$
is also right adjoint to $Rf_{!,\Lambda}$ on $\Dctf$. [sk-prop-sp-unique-adjoint]
gives the unique counit-preserving isomorphism from the explicit adjoint
$K\mapsto f_\Lambda^*K(d)[2d]$ to $f_\Lambda^!$.

For every admissible $\Lambda$ the exceptional inverse image of a smooth
morphism is therefore the twisted and shifted inverse image, normalized by
integration on the affine line, and the smooth trace is the counit of
$Rf_!\dashv f^!$ in this form, compatible with base change, composition, change
of coefficients and Frobenius.
