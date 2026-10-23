+++
kind = "proof"
of = "lem-weil-pbc-cohomology-pullback-degree-zero-iso-factor"
uses = ["lem-sp-grothendieck-enough-injectives"]
+++
The category of abelian étale sheaves is Grothendieck abelian, hence has enough injectives ([lem-sp-grothendieck-enough-injectives]). Choose an injective resolution $R$ of $G$ in nonnegative degrees, extended by zero to all integer degrees. The incoming differential at degree zero vanishes in both $G[0]$ and $R$. Global sections are additive and left exact, and the incoming differentials vanish, so global sections preserve the homology in degree zero; therefore $H^0$ of $\Gamma(T,-)$ of the augmentation $\varepsilon\colon G[0]\to R$ is an isomorphism.

$R$ is bounded below and termwise injective, hence K-injective. Maps into the K-injective complex $I^\bullet$ in the derived category are maps in the homotopy category, so $Q(s)\,Q(\varepsilon)^{-1}$, where $Q$ is the localization functor, lifts to a chain map $a\colon R\to I^\bullet$, and $a\circ\varepsilon$ is homotopic to $s$. Its image $Q(a)$ is invertible, so $a$ is a quasi-isomorphism; between the two K-injective complexes it is a homotopy equivalence.

Apply $\Gamma(T,-)$ to this homotopy equivalence and to the homotopy $a\circ\varepsilon\simeq s$. The homotopy equivalence induces an isomorphism $H^0(\Gamma(T,a))$; homotopy invariance and functoriality of homology identify $H^0(\Gamma(T,s))$ with $H^0(\Gamma(T,a))\circ H^0(\Gamma(T,\varepsilon))$, hence it is an isomorphism.

In $\Gamma(T,G[0])$, the inclusion of cycles and the homology projection in degree zero are isomorphisms because both adjacent differentials are zero. Let $c$ be the identification of $\Gamma(T,G)$ with the degree-zero cycles of $\Gamma(T,G[0])$. Cancelling the monomorphism $i$, the hypothesis $i\circ z=\Gamma(T,s^0)$ identifies $z$ with $c$ followed by the map induced by $\Gamma(T,s)$ on degree-zero cycles. Naturality of the homology projection then writes $\pi\circ z$ as $c$, followed by the homology projection of $\Gamma(T,G[0])$ and by $H^0(\Gamma(T,s))$, a composite of isomorphisms.
