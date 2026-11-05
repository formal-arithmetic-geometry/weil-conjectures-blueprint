+++
kind = "proof"
of = "proposition-twisting-weight-zero-adding-dual--7"
order = 1194014
uses = ["proposition-twisting-weight-zero-adding-dual--3"]
+++
The first inclusion and first projection of
$\mathcal E=\mathcal F^0\oplus(\mathcal F^0)^\vee$ have composite
$\operatorname{id}_{\mathcal F^0}$. In Lean this is the categorical
biproduct used to define `AlgebraicGeometry.WeilSheaf.realEnvelope`.
The inclusion `CategoryTheory.Limits.biprod.inl` is used to prove that
the envelope of a nonzero sheaf is nonzero, and after applying a higher
lower-shriek functor it gives the monomorphism used to descend mixedness
from the envelope to the twisted sheaf.
