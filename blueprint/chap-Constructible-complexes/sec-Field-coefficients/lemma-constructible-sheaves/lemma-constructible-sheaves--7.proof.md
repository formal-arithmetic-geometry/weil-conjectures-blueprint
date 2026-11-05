+++
kind = "proof"
of = "lemma-constructible-sheaves--7"
order = 268016
uses = ["definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-topos-functoriality", "proposition-extension-zero-restriction-closed-subscheme"]
+++
The open-closed exact sequence of
[proposition-extension-zero-restriction-closed-subscheme] makes each
open counit monic. The empty prefix gives the zero subobject, and the
full prefix gives $F$.

For consecutive prefixes $V_r\subseteq V_{r+1}$, the stratum $S_r$ is
closed in $V_{r+1}$. Apply the open-closed sequence there and extend by
zero to $X$. Composition of the adjunctions identifies the resulting
map with the two counits to $F$, so their image subobjects are nested.
Its cokernel is the closed direct image from $S_r$ followed by open
extension from $V_{r+1}$. The support adjunctions identify this with
$a_{r!}a_r^*F$, using the canonical open-then-closed factorization
through the scheme-theoretic image. Since the counits are monic, this
cokernel is $F_{r+1}/F_r$.

Finally, the lisse restriction theorem applied to the given
stratification and its identity refinement makes every $a_r^*F$ lisse.
