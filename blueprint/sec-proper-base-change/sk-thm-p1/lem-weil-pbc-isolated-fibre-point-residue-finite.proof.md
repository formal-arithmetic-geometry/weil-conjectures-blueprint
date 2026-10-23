+++
kind = "proof"
of = "lem-weil-pbc-isolated-fibre-point-residue-finite"
uses = ["def-weil-finite-type-morphism"]
+++
For a morphism locally of finite type, $f$ is quasi-finite at $x$ (i.e. the stalk map $\mathcal O_{S,s}\to\mathcal O_{X,x}$ is quasi-finite) if and only if the point of $X_s$ corresponding to $x$ is isolated in $X_s$. Applied to the isolated fibre point, the stalk map at $x$ is quasi-finite. ([def-weil-finite-type-morphism]).

The quotient map $\mathcal O_{X,x}\to\kappa(x)$ is surjective, hence finite and so quasi-finite. Its composite with the quasi-finite stalk map, $\mathcal O_{S,s}\to\mathcal O_{X,x}\to\kappa(x)$, is quasi-finite, and it equals the residue-field map $\kappa(s)\to\kappa(x)$ composed with the quotient $\mathcal O_{S,s}\to\kappa(s)$. If a composite $g\circ q$ is quasi-finite then so is $g$ when $q$ is surjective; therefore the residue-field map $\kappa(s)\to\kappa(x)$ is itself quasi-finite.

Regard $\kappa(x)$ as a $\kappa(s)$-algebra via the residue-field map, as in the statement. It is quasi-finite by the preceding step. A quasi-finite algebra over an Artinian ring is finite as a module, and the field $\kappa(s)$ is Artinian; so $\kappa(x)$ is a finite-dimensional $\kappa(s)$-vector space, giving precisely the required finite extension.
