+++
kind = "proof"
of = "sk-thm-sfb-rationalization-comparison"
uses = ["sk-lem-integral-models"]
+++
Both assertions are [bhatt-scholze15, Proposition 6.8.14(2)]. What we use from
the equivalence is that for $K,L\in\Dbc(X,\mathcal O_E)$ every morphism
$E_X\otimes K\to E_X\otimes L$ is $\ell^{-c}$ times the image of a
morphism $K\to L$ for some $c\geq0$, and that a morphism $K\to L$ becomes
zero after extension of scalars only if some power of $\ell$ kills it.
For essential
surjectivity, Lemma [sk-lem-integral-models](4) provides
generators that come from $\Dbc(X,\mathcal O_E)$. By the description of the Hom groups, a connecting
morphism between them lifts to an integral one after multiplication by a
power of $\ell$, so finite cones of the generators also have integral
models.
