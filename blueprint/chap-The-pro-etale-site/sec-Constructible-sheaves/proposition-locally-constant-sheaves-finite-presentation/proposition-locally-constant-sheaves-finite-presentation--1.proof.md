+++
kind = "proof"
of = "proposition-locally-constant-sheaves-finite-presentation--1"
order = 146004
uses = ["proposition-locally-constant-sheaves-finite-presentation--2", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image"]
+++
Choose the étale trivializing covering of
[proposition-locally-constant-sheaves-finite-presentation--2] and put
$G=\nu_{X,*}F$. Restriction to an étale member commutes with
$\nu_{X,*}$. The comparison unit and the comparison of constant
sheaves therefore identify $G$ on that member with the same finite
constant module. Thus $G$ is locally constant with finitely generated
geometric stalks.

On each member the restriction of $F$ is a constant sheaf, hence is in
the essential image of the local comparison functor. By
[theorem-classical-sheaves-essential-image], its comparison counit is
invertible. Compatibility of the counit with restriction identifies
these local counits with the restrictions of
$\nu_X^*\nu_{X,*}F\to F$. Restrictions along a covering detect
isomorphisms, so the global counit is invertible. This gives
$\nu_X^*G\simeq F$ and proves classicality.
