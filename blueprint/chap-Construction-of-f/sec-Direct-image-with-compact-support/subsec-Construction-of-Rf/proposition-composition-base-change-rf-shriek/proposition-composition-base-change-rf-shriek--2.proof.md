+++
kind = "proof"
of = "proposition-composition-base-change-rf-shriek--2"
order = 516005
uses = ["proposition-proper-direct-image-constructible-complexes--8", "lemma-inverse-image-tensor-product--1", "definition-compactification-refinement--2", "definition-compactification-refinement--3", "theorem-nagata-s-compactification-theorem--1"]
+++
*Verification of canonicity and associativity.* Every map used is characterized by
its restriction to an open subscheme, since the refinement maps
(5.7) and the maps
(5.9) restrict to identities. For example,
replacing any of the chosen compactifications by a refinement commutes with
(5.9), because both composites restrict to
the same identity and are then equal by adjunction. For three composable
morphisms, we choose common refinements (by graph closure) of the finitely
many compactifications that occur in the composites of two of them. On
these, each of the two bracketings is built from composites of proper direct images,
composites of extensions by zero, and maps of the form
(5.9). The isomorphisms
$Rq_*Rr_*\simeq R(qr)_*$ are associative because they are the
isomorphisms of derived functors of composites of left exact functors
(equivalently, they are adjoint to the composition isomorphisms of the
inverse images), and composition of extensions by zero is associative by
adjunction. Interchanging two adjacent open and proper
steps in either order gives the same map by the uniqueness of
(5.9). So the two bracketings agree.
The unit conditions are the case where one compactification is the identity.
Transitivity of the refinement maps carries these equalities over to
the originally chosen compactifications.

*Source:* the proof of Proposition [proposition-composition-base-change-rf-shriek].
