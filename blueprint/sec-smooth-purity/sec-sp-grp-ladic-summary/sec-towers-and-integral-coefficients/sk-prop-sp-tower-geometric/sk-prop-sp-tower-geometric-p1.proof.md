+++
kind = "proof"
of = "det-sp-tower-p1-adjunction"
+++
*Reduction of the triangle identities.* As in the finite case, proper base
change for the Cartesian square formed by $p_1,p_2$ over $q,q$ and the
projection formulas, which hold for towers ([det-sp-tower-shriek-levels]), rewrite
the two triangle composites
$\varepsilon_\bullet(Rq_{*,\bullet}M)\circ Rq_{*,\bullet}(\eta_\bullet M)$ and
$q^*_\bullet\varepsilon_\bullet(K)(1)[2]\circ\eta_\bullet(q^*_\bullet K(1)[2])$ as the
tensor product of the identity of $M_\bullet$, respectively $K_\bullet$, with the
morphisms

$$
\operatorname{Tr}_{p_i,\bullet}\circ Rp_{i*,\bullet}\delta_\bullet:\
\mathcal O_{E,\mathbf P^1_S}/\ell^\bullet\to\mathcal O_{E,\mathbf P^1_S}/\ell^\bullet
\qquad(i=1,2),
$$

where $\operatorname{Tr}_{p_i,\bullet}$ is the trace of the projective line
$p_i$ (the base change of $q$). So the triangle identities hold once these
two endomorphisms are the identity.

*Levelwise check.* Both $\operatorname{Tr}_{p_i,\bullet}\circ Rp_{i*,\bullet}\delta_\bullet$ and
the identity are endomorphisms of the tower sheaf
$\mathcal O_{E,\mathbf P^1_S}/\ell^\bullet$ placed in degree zero. Morphisms in the
derived category between objects concentrated in degree zero are morphisms of
towers of sheaves, i.e. compatible families of sheaf maps, and these are equal
iff they are equal at every level. At level $n$, by [det-sp-tower-classes] and
the levelwise computation of $Rp_{i*,\bullet}$, the morphism is the finite
composite $\operatorname{Tr}_{p_i}\circ Rp_{i*}\delta$, which is the identity by the
finite diagonal integrals (the diagonal integrates to $1$ along each factor).
Hence both endomorphisms are the identity and the adjunction holds.

*Levels.* Evaluation at $n$ is exact and commutes with all the functors
involved, and carries $\delta_\bullet$, $\operatorname{Tr}_{q,\bullet}$ to the finite
classes; so it carries $\eta_\bullet,\varepsilon_\bullet$ to the finite unit and
counit.
