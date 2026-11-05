+++
kind = "proof"
of = "lemma-inverse-image-coefficient-sheaves"
order = 188
uses = ["proposition-etale-implications", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "proposition-comparison-morphism-inverse-image"]
+++
(1) For every condensed ring $\Lambda$, the identity $p_Y\circ f=p_X$
shows that

$$
f^{-1}\Lambda_Y=f^{-1}p_Y^*\Lambda\simeq p_X^*\Lambda=\Lambda_X,
$$

and this proves the assertion for the coefficient rings themselves.

For the twists, $\ell$ is invertible on $Y$, hence on $X$, as
Definition [definition-tate-twists] requires. The torsion twists
$\mu_{\ell^n}$ are then represented by finite étale group
schemes, and these commute with base change. Their inverse limit is
represented by the inverse limit of these schemes, so that its inverse image
is represented by the base change [Stacks, [09A5](https://stacks.math.columbia.edu/tag/09A5)]. This proves the
assertion for $\mathcal O_E(1)$. For a finite $A$ killed by
$\ell^n$, its twist is obtained from the twist at finite level by extending
scalars from $\mathbf Z/\ell^n\mathbf Z$, so inverse image
commutes with it as well. The other twists are obtained by inverting $\ell$,
extending scalars, and taking tensor powers and duals.

(2) An $\mathcal O_E$-basis of $\mathcal O_{E'}$ is an isomorphism of
topological $\mathcal O_E$-modules $\mathcal O_{E'}\simeq\mathcal O_E^{[E':E]}$,
hence of condensed modules
$\underline{\mathcal O_{E'}}\simeq\underline{\mathcal O_E}^{[E':E]}$. Pull it
back along $p_X$, and invert $\ell$ for the fields.
