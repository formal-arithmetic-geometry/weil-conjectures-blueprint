+++
kind = "proof"
of = "proposition-sp-unique-adjoint--1"
order = 762002
uses = []
+++
Conjugate the identity isomorphism of $F$ under the two adjunctions. The
conjugation equivalence `CategoryTheory.conjugateIsoEquiv` gives an isomorphism
$\rho:G\xrightarrow{\sim}J$; conjugating in the opposite direction gives its
inverse. On each object $K$, the map $\rho(K)$ is the $J$-transpose of
$\varepsilon^G(K)$. Applying the inverse adjunction bijection gives
$\varepsilon^J(K)\circ F(\rho(K))=\varepsilon^G(K)$.

If a natural transformation $\alpha:G\to J$ satisfies the same equation,
then $\alpha(K)$ and $\rho(K)$ have the same inverse transpose under
$F\dashv J$. Injectivity of this bijection gives $\alpha(K)=\rho(K)$ for
every $K$, hence $\alpha=\rho$.
