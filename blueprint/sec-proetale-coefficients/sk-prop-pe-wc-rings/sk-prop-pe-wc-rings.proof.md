+++
kind = "proof"
of = "sk-prop-pe-wc-rings"
uses = ["sk-prop-pe-stonean"]
+++
*Proof outline.* First refine $B$ by ind-Zariski operations so that its spectrum is
w-local and its closed points lie exactly above the closed points of
$\operatorname{Spec}(R)$ ([det-pe-wc-rings-w-local-refinement]). Here ind-Zariski means a
filtered colimit of local isomorphisms; these operations preserve local rings.

Over a closed point of $\operatorname{Spec}(R)$, strict henselianity implies that the
induced map of local rings for an ind-étale algebra is an isomorphism
([det-pe-wc-rings-local-iso]), so what remains is a choice of component. Stonean
projectivity [sk-prop-pe-stonean] splits the surjection of profinite component spaces.
Restriction to that closed set of components is realized by a filtered colimit of
localizations at idempotents; it produces an $R$-algebra isomorphic to $R$, hence a
retraction ([det-pe-wc-rings-retraction]). The algebraic realization of these refinements
is supplied by Stacks, Tags 097D and 09AZ; the resulting argument is Stacks, Tag 0982.
