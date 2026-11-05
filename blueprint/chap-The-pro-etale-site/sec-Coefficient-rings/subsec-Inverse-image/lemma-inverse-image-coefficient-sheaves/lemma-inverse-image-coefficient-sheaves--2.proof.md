+++
kind = "proof"
of = "lemma-inverse-image-coefficient-sheaves--2"
order = 187007
uses = ["definition-tate-twists"]
+++
Put $S=\operatorname{Spec}\mathbf Z[1/N]$ and let $\pi_T:T\to S$ be the
canonical morphism for $T=X,Y$. On $S$, adjoining a primitive $N$th root
of unity trivializes $A_S(1)$, so its dual is a tensor inverse. Form the
integer tensor powers $A_S(d)$ of this invertible object. In the Lean
construction, $A_T(d)=\mathbf L\pi_T^*A_S(d)$.

Since $\pi_Y\circ f=\pi_X$, the composition isomorphism of derived étale
inverse images gives

$$
\mathbf Lf_{\acute{e}t}^*\mathbf L\pi_Y^*A_S(d)
\simeq\mathbf L\pi_X^*A_S(d)=A_X(d).
$$

Transporting this comparison through the defining identifications of the
twists proves the assertion for every integer $d$.
