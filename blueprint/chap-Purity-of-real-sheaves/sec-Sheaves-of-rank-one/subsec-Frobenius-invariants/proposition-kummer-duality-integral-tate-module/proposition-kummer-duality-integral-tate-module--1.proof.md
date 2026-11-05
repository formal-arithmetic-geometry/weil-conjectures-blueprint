+++
kind = "proof"
of = "proposition-kummer-duality-integral-tate-module--1"
order = 1094004
uses = ["proposition-jacobian-over-ground-field", "corollary-degree-jacobian"]
+++
The Kummer sequence identifies the image of
$H^1(X,\mu_m)\to H^1(X,\mathbf G_m)=\operatorname{Pic}(X)$ with
$\operatorname{Pic}(X)[m]$. Properness makes $\Gamma(X,\mathcal O_X)$ a
finite-dimensional $k$-algebra. Its units have $m$-th roots because $k$
is algebraically closed and $m$ is invertible. Thus the preceding
Kummer boundary is zero, and the map in degree one is injective. This
is the construction of `AlgebraicGeometry.Scheme.kummerTorsionEquiv`.

For the second assertion, descend the Jacobian as in
[proposition-jacobian-over-ground-field]. The resulting identification
$J_0(k)\simeq\operatorname{Pic}^0(C)$ is Galois-equivariant.
Every $\ell^n$-torsion line bundle has degree zero, since its degree is
an integer killed by $\ell^n$
([corollary-degree-jacobian]). Restricting the identification to torsion
therefore gives $e_n$. Its compatibility with multiplication by $\ell$
follows from additivity. These are exactly the data constructed by
`AlgebraicGeometry.JacobianTorsionDatum.nonempty`.
