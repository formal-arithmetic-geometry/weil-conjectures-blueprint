+++
kind = "proof"
of = "det-pe-weak-contractible-equivalences"
+++
*2 $\Leftrightarrow$ 3.* By the Yoneda lemma $\Hom(h_W,G)=G(W)$ naturally in $G$, so a lift
of $y\colon h_W\to G$ along $F\to G$ is exactly an element of $F(W)$ mapping to $y\in G(W)$.

*1 $\Rightarrow$ 2.* Given an epimorphism $F\to G$ and $y\colon h_W\to G$, the pullback
$F\times_Gh_W\to h_W$ is an epimorphism, since epimorphisms in a topos are stable under
pullback. A section of it composed with the projection to $F$ is a lift of $y$.

*2 $\Rightarrow$ 1.* Apply 2 to the epimorphism $F\to h_W$ and the map
$\mathrm{id}\colon h_W\to h_W$.

The last assertion is part 1 of [det-pe-wcb-projective].
