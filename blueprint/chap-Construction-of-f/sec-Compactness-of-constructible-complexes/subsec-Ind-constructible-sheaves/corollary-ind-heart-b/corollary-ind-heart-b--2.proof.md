+++
kind = "proof"
of = "corollary-ind-heart-b--2"
order = 456004
uses = ["lemma-continuity-ext-out-constructible-complex", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--4", "lemma-continuity-ext-out-constructible-complex--1", "definition-relative-picard-functor--2"]
+++
For the second claim, let $(B_\lambda)$ be a family in
$\IndCons(X,\Lambda)$. Its direct sum is the filtered colimit of the
finite subsums, and $\Ext^q(C,-)$ commutes with finite direct sums
because it is additive. Applying
Lemma [lemma-continuity-ext-out-constructible-complex] once more, to the diagram
of finite subsums, we obtain
$\Ext^q(C,\bigoplus_\lambda B_\lambda)=\bigoplus_\lambda\Ext^q(C,B_\lambda)$.

*Source:* the proof of Corollary [corollary-ind-heart-b].
