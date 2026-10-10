+++
kind  = "proof"
of    = "lem-amb-closed-support-hom"
+++
The sequence
$0\to v_!A_V\to A_T\to i_*A_D\to0$ is exact:
at a geometric point of $V$ it is
$0\to A\xrightarrow{1}A\to0$, and at a point
of $D$ it is $0\to0\to A\xrightarrow{1}A\to0$.
This stalk computation uses exact closed direct image
from [lemma-weil-pbc-finite-direct-image-exact] and
conservativity from
[lemma-weil-pbc-geometric-stalk-conservative].
Apply derived Hom into $K$ to its triangle.
The open adjunction of
[lem-amb-etale-adjoint-locality] identifies
$R\operatorname{Hom}_T(v_!A_V,K)$ with
$R\Gamma(V,v^*K)$; both adjoints are exact, so
the derived identification holds on arbitrary complexes.
The resulting Hom triangle is exactly the asserted cone.
