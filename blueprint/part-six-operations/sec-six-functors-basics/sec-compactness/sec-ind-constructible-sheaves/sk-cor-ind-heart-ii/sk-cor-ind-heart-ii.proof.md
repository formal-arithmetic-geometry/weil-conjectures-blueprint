+++
kind = "proof"
of = "sk-cor-ind-heart-ii"
uses = ["sk-lem-constructible-ext-continuity", "sk-lem-uniform-constructible-ext"]
+++
Write $B$ as a filtered colimit of constructible sheaves. By
Lemma [sk-lem-constructible-ext-continuity], $\Ext^q(C,B)$ is the
colimit of the corresponding groups for the constructible terms, which
vanish for $q>d_C$ by Lemma [sk-lem-uniform-constructible-ext]. A
direct sum is the filtered colimit of its finite subsums, and $\Ext^q(C,-)$
commutes with finite direct sums, so
Lemma [sk-lem-constructible-ext-continuity] proves the second claim.
