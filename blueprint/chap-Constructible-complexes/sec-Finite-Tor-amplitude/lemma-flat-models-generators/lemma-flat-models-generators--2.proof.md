+++
kind = "proof"
of = "lemma-flat-models-generators--2"
order = 255005
uses = ["definition-lisse-sheaves"]
+++
When $X$ is nonempty, take a geometric stalk of
$F\simeq\underline M$. Finite local constancy makes $M$ finitely generated,
and flatness of $F$ makes $M$ flat. The finite ring $A$ is Noetherian, so
$M$ is finitely presented and hence projective. Thus $M$ is dualizable.

Choose an étale cover on which $F$ is constant. Pullback preserves flatness,
and the constant sheaf functor is symmetric monoidal, so the preceding
argument makes each pullback dualizable. Pullback along an étale morphism
also commutes with internal Hom. Consequently the comparison
$$
\mathcal{H}om_A(F,A_X)\otimes_A F\longrightarrow\mathcal{H}om_A(F,F)
$$
is an isomorphism on the cover and therefore on $X$. This gives the stated
duality with its usual evaluation.

On the same cover, $F^\vee$ is the constant sheaf associated to the dual
of a finite projective module. Its geometric stalks are again finitely
generated, so it is finite locally constant. On an empty scheme all the
sheaves in question are zero, and the assertions follow directly.
