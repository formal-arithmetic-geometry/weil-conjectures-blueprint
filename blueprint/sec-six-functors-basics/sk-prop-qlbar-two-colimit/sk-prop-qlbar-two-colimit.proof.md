+++
kind  = "proof"
of    = "sk-prop-qlbar-two-colimit"
uses = ["sk-thm-sfb-qlbar-two-colimit", "sk-lem-constructible-ext-continuity"]
+++
The statement about objects is [sk-thm-sfb-qlbar-two-colimit](2). Its proof first descends the lisse
sheaves on the strata, together with their transition matrices, and then the connecting morphisms of a
finite Postnikov tower, so that the complexes themselves descend. The bijection on morphisms is
[sk-thm-sfb-qlbar-two-colimit](1) with $r=0$, since $\Dctf$ is a full subcategory. Its proof uses the
continuity of Ext out of a constructible complex ([sk-lem-constructible-ext-continuity]). Surjectivity says
that every morphism descends to a finite stage, and injectivity says that two morphisms with the same image
agree at a later finite stage. Now consider the category whose objects are the pairs $(E,K)$ with
$K\in\Dctf(X,E)$ and whose Hom sets are these colimits. Together with descent of objects, the statements
above say exactly that the functor from this category to $\Dctf(X,\Qlb)$ is fully faithful and essentially
surjective.
