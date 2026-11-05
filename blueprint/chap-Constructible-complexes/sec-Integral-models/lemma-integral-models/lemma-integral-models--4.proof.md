+++
kind = "proof"
of = "lemma-integral-models--4"
order = 294005
uses = ["lemma-integral-models--3", "lemma-integral-models--5", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Use Noetherian induction on closed subsets. The empty case is zero. On a
nonempty scheme choose a nonempty open subset and a surjective closed
immersion onto it on which the cohomology sheaves of both complexes are
pro-étale locally finitely presented. Pullback preserves bounded
constructibility by [lemma-integral-models--3] and commutes with derived
tensor product. The second hypothesis therefore treats this open piece;
the closed immersion counit and preservation under closed direct image
transport the result back.

On the closed complement apply the induction hypothesis. The open--closed
localization triangle and the first hypothesis then give the result on
$X$. For $\mathcal O_E$, the integral lisse tensor calculation supplies the
second hypothesis, and the integral constructible category is
triangulated. The comparison of constructibility predicates identifies
this with the stated assertion about $\Dbc$.
