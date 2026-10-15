+++
kind = "proof"
of = "det-sp-rational-adjunction"
+++
(1) The first and last bijections are [det-sp-rational-localized-hom], using
$Rf_{!,E}M\simeq(Rf_{!,\mathcal O_E}M_0)[1/\ell]$ and
$f^*_EK(d)[2d]\simeq(f^*_{\mathcal O_E}K_0(d)[2d])[1/\ell]\simeq(f^!_{\mathcal O_E}K_0)[1/\ell]$,
the last by the integral purity isomorphism of
[det-sp-integral-adjunction-bijection]. The middle bijection is the integral
adjunction tensored with $E$. Two integral models of the same rational object
are related by a morphism that becomes invertible after inverting $\ell$
(e.g. multiplication by a power of $\ell$ composed with a lattice inclusion),
and all the bijections are natural with respect to such morphisms; after
$\otimes E$ these become isomorphisms, so the composite does not depend on the
models. Naturality in $M,K$: a morphism of rational objects is, after
multiplying by a power of $\ell$, the image of a morphism of models, and all
bijections are natural in integral morphisms and $E$-linear. An $E$-linear
natural bijection of Hom functors is an adjunction; its counit is the image of
the identity, which is the scalar extension of the integral counit transported
along $\gamma_{f,\mathcal O_E}$, and similarly for the unit; the triangle
identities are images of the integral ones.

(2) Both $f^*_E(-)(d)[2d]$ (by (1)) and $f^!_E$ (by construction) are right
adjoints of $Rf_{!,E}$ on $\Dbc(-,E)$. [det-sp-unique-right-adjoint] gives the
unique counit-compatible isomorphism between them; its inverse direction is
$\gamma_{f,E}$. Through $\gamma_{f,E}$ the unit $\eta_{f,E}$ and counit
$\varepsilon_{f,E}$ of the Brown adjunction are normalized by integral models.
