+++
kind = "proof"
of = "lemma-local-terms-point"
order = 920
uses = ["proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-sp-unique-adjoint", "definition-verdier-dual-evaluation", "lemma-external-duality-trace-morphism", "definition-trace-morphism", "lemma-kunneth-formula-compact-supports", "theorem-nagata-s-compactification-theorem", "lemma-passing-schematic-closure"]
+++
On the point each step of the construction of the trace class is a
step of the categorical trace. Here $\omega_s=A_s$, so $\mathbb D_sP=P^\vee$, and $P_s=P\boxtimes
P^\vee=P\otimes^{\mathbf L}P^\vee$. First, under the first isomorphism of Lemma [lemma-external-duality-trace-morphism], the map $u$ becomes the element of
$P\otimes^{\mathbf L}P^\vee$ obtained by applying $u\otimes1$ to the
coevaluation. Next, the diagonal of $s$ is the identity, so the trace morphism is the evaluation $P\otimes^{\mathbf L}P^\vee\to A$, taken
after the symmetry that puts the factors in the order
$P^\vee\otimes P$. That symmetry is precisely the symmetry in
Definition [definition-categorical-trace], and integration over $s$ is the
identity of $A$. The composite is therefore the categorical trace.
